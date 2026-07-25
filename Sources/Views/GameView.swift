import SwiftUI

/// Die eigentliche Blitzlese-Runde.
///
/// Timing-Garantie (Original-Bug: Wiederholung kürzer als eingestellt):
/// Jede Darbietung — auch die Wiederholung — läuft über dieselbe present()-Funktion
/// mit exakt der konfigurierten Dauer.
struct GameView: View {
    @EnvironmentObject var store: AppStore
    @Environment(\.dismiss) private var dismiss

    enum Phase {
        case countdown(Int)
        case flashing
        case answering
        case feedback(Bool)
        case summary
    }

    @State private var plan = RoundPlan(words: [], listKey: "", listName: "")
    @State private var index = 0
    @State private var phase: Phase = .countdown(3)
    @State private var flashTime: Double = 1.0
    @State private var streak = 0
    @State private var correctCount = 0
    @State private var wrongWords: [WordEntry] = []
    @State private var typed = ""
    @State private var seqIndex = -1 // dynamische Silbenhervorhebung
    @State private var flashTask: Task<Void, Never>? = nil
    @FocusState private var inputFocused: Bool

    private var settings: ProfileSettings { store.current.settings }
    private var language: String { store.listLanguage(forKey: plan.listKey) }
    private var darkBG: Bool { Theme.isDarkBackground(settings.background) }
    private var textColor: Color { darkBG ? .white : .primary }
    private var entry: WordEntry? { index < plan.words.count ? plan.words[index] : nil }

    var body: some View {
        ZStack {
            Theme.background(settings.background).ignoresSafeArea()
            content
        }
        .onAppear(perform: start)
        .onDisappear { flashTask?.cancel(); Speech.shared.stop() }
    }

    @ViewBuilder private var content: some View {
        switch phase {
        case .countdown(let n):
            VStack(spacing: 24) {
                MascotImage(pose: "laufend", height: 160)
                Text("\(n)")
                    .font(.system(size: 90, weight: .bold, design: .rounded))
                    .foregroundColor(textColor)
            }
        case .summary:
            summaryView
        default:
            gameBody
        }
    }

    // MARK: - Spielfläche

    private var gameBody: some View {
        VStack(spacing: 0) {
            header
            Spacer()
            wordArea
            Spacer()
            controls
                .padding(.bottom, 24)
        }
        .padding(.horizontal)
    }

    private var header: some View {
        HStack {
            Button {
                dismiss()
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .font(.title2)
                    .foregroundColor(textColor.opacity(0.5))
            }
            .accessibilityLabel(loc("Runde beenden", "End round"))
            Spacer()
            Text(loc("Wort \(min(index + 1, plan.words.count)) von \(plan.words.count)",
                     "Word \(min(index + 1, plan.words.count)) of \(plan.words.count)"))
                .font(.headline)
                .foregroundColor(textColor.opacity(0.8))
            Spacer()
            Label("\(store.current.stars)", systemImage: "star.fill")
                .font(.headline)
                .foregroundColor(.orange)
        }
        .padding(.top, 8)
    }

    @ViewBuilder private var wordArea: some View {
        switch phase {
        case .flashing:
            wordDisplay
                .accessibilityLabel(loc("Wort wird gezeigt", "Word is shown"))
        case .answering:
            if settings.teacherMode {
                Text("?")
                    .font(Theme.wordFont(choice: settings.fontChoice, size: settings.fontSize))
                    .foregroundColor(textColor.opacity(0.25))
            } else {
                typingArea
            }
        case .feedback(let ok):
            VStack(spacing: 16) {
                wordDisplay
                if ok {
                    MascotImage(pose: "jubelnd", height: 110)
                    Text(loc("Richtig!", "Correct!"))
                        .font(.title.bold())
                        .foregroundColor(Theme.correct)
                } else {
                    Text(loc("Das Wort war:", "The word was:"))
                        .font(.headline)
                        .foregroundColor(textColor.opacity(0.7))
                }
            }
        default:
            EmptyView()
        }
    }

    /// Wortdarstellung mit optionaler Silbenvisualisierung.
    private var wordDisplay: some View {
        Group {
            if let e = entry {
                let sylls = e.displaySyllables(swiss: settings.swissSpelling)
                switch settings.syllableMode {
                case "colored":
                    sylls.enumerated().reduce(Text("")) { acc, pair in
                        acc + Text(pair.element)
                            .foregroundColor(darkBG
                                ? (pair.offset % 2 == 0 ? .white : .orange)
                                : Theme.syllableColors[pair.offset % 2])
                    }
                    .font(Theme.wordFont(choice: settings.fontChoice, size: settings.fontSize, bold: true))
                case "sequential":
                    sylls.enumerated().reduce(Text("")) { acc, pair in
                        acc + Text(pair.element)
                            .foregroundColor(pair.offset <= seqIndex
                                ? (darkBG ? .orange : Theme.accent)
                                : textColor.opacity(0.35))
                    }
                    .font(Theme.wordFont(choice: settings.fontChoice, size: settings.fontSize, bold: true))
                default:
                    Text(e.display(swiss: settings.swissSpelling))
                        .font(Theme.wordFont(choice: settings.fontChoice, size: settings.fontSize, bold: true))
                        .foregroundColor(textColor)
                }
            }
        }
        .minimumScaleFactor(0.3)
        .lineLimit(1)
        .padding(.horizontal)
    }

    private var typingArea: some View {
        VStack(spacing: 12) {
            TextField(loc("Wort eintippen …", "Type the word …"), text: $typed)
                .font(Theme.wordFont(choice: settings.fontChoice, size: min(settings.fontSize, 44)))
                .multilineTextAlignment(.center)
                .autocorrectionDisabled(true)
                .textInputAutocapitalization(.never)
                .focused($inputFocused)
                .submitLabel(.done)
                .onSubmit(checkTyped)
                .padding()
                .background(RoundedRectangle(cornerRadius: 16).fill(Color(UIColor.systemBackground).opacity(0.9)))
                .frame(maxWidth: 420)
            Button(action: checkTyped) {
                Text(loc("Prüfen", "Check"))
                    .font(.title3.bold())
                    .frame(maxWidth: 420)
                    .padding(.vertical, 10)
            }
            .buttonStyle(.borderedProminent)
            .disabled(typed.trimmingCharacters(in: .whitespaces).isEmpty)
        }
    }

    // MARK: - Bedienleiste

    @ViewBuilder private var controls: some View {
        switch phase {
        case .answering where settings.teacherMode:
            VStack(spacing: 16) {
                HStack(spacing: 40) {
                    Button { mark(false) } label: {
                        smiley(ok: false)
                    }
                    .accessibilityLabel(loc("Falsch gelesen", "Read incorrectly"))
                    Button { mark(true) } label: {
                        smiley(ok: true)
                    }
                    .accessibilityLabel(loc("Richtig gelesen", "Read correctly"))
                }
                helperRow
            }
        case .answering:
            helperRow
        case .feedback:
            Button(action: advance) {
                Text(loc("Weiter", "Next"))
                    .font(.title3.bold())
                    .frame(maxWidth: 420)
                    .padding(.vertical, 10)
            }
            .buttonStyle(.borderedProminent)
        default:
            EmptyView()
        }
    }

    private var helperRow: some View {
        HStack(spacing: 28) {
            Button {
                present() // Wiederholen: exakt gleiche Dauer (Original-Bug behoben)
            } label: {
                Label(loc("Nochmal zeigen", "Show again"), systemImage: "arrow.counterclockwise")
            }
            if settings.tts {
                Button {
                    if let e = entry { Speech.shared.speak(e.display(swiss: settings.swissSpelling), language: language) }
                } label: {
                    Label(loc("Vorsprechen", "Speak"), systemImage: "speaker.wave.2.fill")
                }
                .accessibilityLabel(loc("Wort vorsprechen", "Speak the word"))
            }
        }
        .font(.body.weight(.medium))
        .foregroundColor(darkBG ? .white : Theme.accent)
    }

    private func smiley(ok: Bool) -> some View {
        Image(systemName: ok ? "face.smiling.fill" : "xmark.circle.fill")
            .font(.system(size: 64))
            .foregroundColor(ok ? Theme.correct : Theme.wrong)
            .background(Circle().fill(.white).padding(6))
    }

    // MARK: - Zusammenfassung

    private var summaryView: some View {
        ScrollView {
            VStack(spacing: 20) {
                MascotImage(pose: correctCount == plan.words.count ? "tanzend" : "jubelnd", height: 150)
                Text(loc("Runde geschafft!", "Round finished!"))
                    .font(.largeTitle.bold())
                    .foregroundColor(textColor)
                HStack(spacing: 8) {
                    Image(systemName: "star.fill").foregroundColor(.orange)
                    Text(loc("\(correctCount) von \(plan.words.count) richtig",
                             "\(correctCount) of \(plan.words.count) correct"))
                        .font(.title2)
                        .foregroundColor(textColor)
                }
                if !wrongWords.isEmpty {
                    VStack(alignment: .leading, spacing: 8) {
                        Text(loc("Diese Wörter üben wir wieder:", "We'll practice these again:"))
                            .font(.headline)
                            .foregroundColor(textColor.opacity(0.8))
                        ForEach(wrongWords) { w in
                            HStack {
                                Text(w.display(swiss: settings.swissSpelling))
                                    .font(Theme.wordFont(choice: settings.fontChoice, size: 28))
                                Spacer()
                                if settings.tts {
                                    Button {
                                        Speech.shared.speak(w.display(swiss: settings.swissSpelling), language: language)
                                    } label: {
                                        Image(systemName: "speaker.wave.2.fill")
                                    }
                                }
                            }
                            .padding(10)
                            .background(RoundedRectangle(cornerRadius: 12).fill(Color(UIColor.systemBackground).opacity(0.85)))
                        }
                    }
                    .padding(.horizontal)
                }
                VStack(spacing: 12) {
                    Button {
                        start()
                    } label: {
                        Text(loc("Noch eine Runde", "One more round"))
                            .font(.title3.bold())
                            .frame(maxWidth: 420)
                            .padding(.vertical, 10)
                    }
                    .buttonStyle(.borderedProminent)
                    Button {
                        dismiss()
                    } label: {
                        Text(loc("Fertig", "Done"))
                            .frame(maxWidth: 420)
                    }
                    .buttonStyle(.bordered)
                }
                .padding(.top, 8)
            }
            .padding()
        }
    }

    // MARK: - Ablauf

    private func start() {
        var profile = store.current
        plan = RoundEngine.buildRound(store: store, profile: &profile)
        store.current = profile
        index = 0
        correctCount = 0
        wrongWords = []
        streak = 0
        flashTime = settings.flashTime
        guard !plan.words.isEmpty else { dismiss(); return }
        runCountdown(3)
    }

    private func runCountdown(_ n: Int) {
        phase = .countdown(n)
        flashTask?.cancel()
        flashTask = Task {
            try? await Task.sleep(nanoseconds: 800_000_000)
            guard !Task.isCancelled else { return }
            await MainActor.run {
                if n > 1 { runCountdown(n - 1) } else { present() }
            }
        }
    }

    /// Zeigt das aktuelle Wort für exakt `flashTime` Sekunden.
    private func present() {
        guard entry != nil else { return }
        typed = ""
        seqIndex = -1
        phase = .flashing
        flashTask?.cancel()

        let duration = flashTime
        let sylCount = entry?.syllableCount ?? 1

        flashTask = Task {
            if settings.syllableMode == "sequential" && sylCount > 1 && duration >= 0.5 {
                let step = duration / Double(sylCount)
                for i in 0..<sylCount {
                    guard !Task.isCancelled else { return }
                    await MainActor.run { seqIndex = i }
                    try? await Task.sleep(nanoseconds: UInt64(step * 1_000_000_000))
                }
            } else {
                await MainActor.run { seqIndex = sylCount }
                try? await Task.sleep(nanoseconds: UInt64(duration * 1_000_000_000))
            }
            guard !Task.isCancelled else { return }
            await MainActor.run {
                phase = .answering
                if !settings.teacherMode { inputFocused = true }
            }
        }
    }

    private func checkTyped() {
        guard let e = entry else { return }
        let expected = e.display(swiss: settings.swissSpelling)
            .lowercased().trimmingCharacters(in: .whitespaces)
        let given = typed.lowercased().trimmingCharacters(in: .whitespaces)
        guard !given.isEmpty else { return }
        mark(given == expected)
    }

    private func mark(_ correct: Bool) {
        guard let e = entry else { return }
        inputFocused = false
        var profile = store.current
        RoundEngine.mark(profile: &profile, entry: e, correct: correct)
        store.current = profile

        if correct {
            correctCount += 1
            streak += 1
        } else {
            wrongWords.append(e)
            streak = 0
        }
        if settings.adaptive {
            flashTime = RoundEngine.adaptedTime(current: flashTime, streak: streak, lastCorrect: correct)
        }
        if settings.tts && !correct {
            Speech.shared.speak(e.display(swiss: settings.swissSpelling), language: language)
        }
        phase = .feedback(correct)

        // Bei "Richtig" im Alleine-Modus automatisch weiter (Original-Kritik: manuelles Löschen)
        if correct {
            flashTask?.cancel()
            flashTask = Task {
                try? await Task.sleep(nanoseconds: 1_100_000_000)
                guard !Task.isCancelled else { return }
                await MainActor.run { advance() }
            }
        }
    }

    private func advance() {
        flashTask?.cancel()
        if index + 1 < plan.words.count {
            index += 1
            present()
        } else {
            var profile = store.current
            RoundEngine.finishRound(profile: &profile, plan: plan, correct: correctCount, flashTime: flashTime)
            store.current = profile
            phase = .summary
        }
    }
}
