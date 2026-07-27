import SwiftUI

/// „Easy Reading": digitale Nachbildung der EASY-Reading-Leseschablone
/// (20 × 8 cm, blaue Karte mit vier farbigen Eckfenstern). Bei „Lesen/Read"
/// gleitet die Karte von links nach rechts, das Wort wird durch das linke
/// obere Fenster sichtbar und anschließend vorgelesen. Darunter steht das
/// Wort groß in Schwarz; „ABC" buchstabiert es Buchstabe für Buchstabe.
struct EasyReadingView: View {
    @EnvironmentObject var store: AppStore
    @Environment(\.dismiss) private var dismiss

    @State private var words: [WordEntry] = []
    @State private var index = 0
    @State private var spellIndex: Int? = nil
    @State private var spellTask: Task<Void, Never>? = nil
    @State private var readTask: Task<Void, Never>? = nil
    @State private var cardSlid = false

    private var settings: ProfileSettings { store.current.settings }
    private var language: String { store.listLanguage(forKey: settings.selectedList) }
    private var textColor: Color { .black }
    private var entry: WordEntry? { words.indices.contains(index) ? words[index] : nil }

    // Farben der Original-Schablone
    private let cardBlue = Color(red: 0.42, green: 0.58, blue: 0.86)
    private let logoNavy = Color(red: 0.12, green: 0.12, blue: 0.47)
    private let winLavender = Color(red: 0.85, green: 0.86, blue: 0.92)
    private let winPink = Color(red: 0.91, green: 0.83, blue: 0.87)
    private let winCream = Color(red: 0.92, green: 0.91, blue: 0.81)
    private let winGrey = Color(red: 0.88, green: 0.88, blue: 0.88)

    var body: some View {
        ZStack {
            Color.white.ignoresSafeArea()
            VStack(spacing: 0) {
                header
                Spacer()
                cardArea
                wordDisplay
                    .padding(.top, 30)
                Spacer()
                navRow
                    .padding(.bottom, 18)
                bottomButtons
            }
            .padding()
        }
        .onAppear(perform: load)
        .onDisappear(perform: stopAll)
    }

    private var header: some View {
        HStack {
            Button {
                stopAll()
                dismiss()
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .font(.title)
                    .foregroundColor(textColor.opacity(0.5))
            }
            .accessibilityLabel(loc("Schließen", "Close"))
            Spacer()
            Text("Easy Reading")
                .font(.headline)
                .foregroundColor(textColor.opacity(0.7))
            Spacer()
            Text(words.isEmpty ? "" : "\(index + 1) / \(words.count)")
                .font(.headline.monospacedDigit())
                .foregroundColor(textColor.opacity(0.7))
        }
        .padding(.top, 8)
    }

    // MARK: - Schablone

    /// Wort + darübergleitende Schablone. Am Ende der Bewegung liegt das
    /// linke obere Fenster genau über dem Wort.
    private var cardArea: some View {
        GeometryReader { geo in
            let w = geo.size.width
            let cardW = w * 1.45
            let cardH = cardW / 2.5          // 20 × 8 cm
            let winW = cardW * 0.26
            let winH = cardH * 0.17
            let slideOffset: CGFloat = cardSlid ? 8 : 8 - w * 0.5

            ZStack(alignment: .topLeading) {
                if let e = entry {
                    Text(e.display(swiss: settings.swissSpelling))
                        .font(Theme.wordFont(choice: settings.fontChoice, size: winH * 0.62))
                        .foregroundColor(.black)
                        .minimumScaleFactor(0.3)
                        .lineLimit(1)
                        .frame(width: winW - 20, height: winH)
                        .offset(x: 16, y: 0)
                }
                overlayCard(cardW: cardW, cardH: cardH, winW: winW, winH: winH)
                    .offset(x: slideOffset, y: 0)
            }
        }
        .aspectRatio(1 / 0.58, contentMode: .fit)   // Höhe = cardH
    }

    /// Die Karte selbst: blauer Körper, vier durchscheinende Eckfenster, Logo.
    private func overlayCard(cardW: CGFloat, cardH: CGFloat,
                             winW: CGFloat, winH: CGFloat) -> some View {
        ZStack {
            VStack(spacing: 0) {
                HStack(spacing: 0) {
                    Rectangle().fill(winLavender.opacity(0.55)).frame(width: winW)
                    Rectangle().fill(cardBlue)
                    Rectangle().fill(winPink.opacity(0.85)).frame(width: winW)
                }
                .frame(height: winH)
                Rectangle().fill(cardBlue)
                HStack(spacing: 0) {
                    Rectangle().fill(winCream.opacity(0.85)).frame(width: winW)
                    Rectangle().fill(cardBlue)
                    Rectangle().fill(winGrey.opacity(0.85)).frame(width: winW)
                }
                .frame(height: winH)
            }
            Text("EASY - Reading™")
                .font(.system(size: cardH * 0.15, weight: .heavy).italic())
                .foregroundColor(logoNavy)
        }
        .frame(width: cardW, height: cardH)
        .clipShape(RoundedRectangle(cornerRadius: cardH * 0.12))
        .shadow(color: .black.opacity(0.15), radius: 6, y: 3)
    }

    // MARK: - Wort unterhalb der Karte

    private var wordDisplay: some View {
        Group {
            if let e = entry {
                let chars = Array(e.display(swiss: settings.swissSpelling))
                chars.indices.reduce(Text("")) { acc, i in
                    acc + Text(String(chars[i]))
                        .foregroundColor(i == spellIndex
                            ? Theme.accent
                            : (spellIndex == nil ? textColor : textColor.opacity(0.35)))
                }
                .font(Theme.wordFont(choice: settings.fontChoice, size: 58, bold: true))
            } else {
                Text(loc("Keine Wörter in dieser Liste.", "No words in this list."))
                    .font(.headline)
                    .foregroundColor(textColor.opacity(0.7))
            }
        }
        .minimumScaleFactor(0.3)
        .lineLimit(1)
        .padding(.horizontal)
    }

    private var navRow: some View {
        HStack(spacing: 60) {
            Button(action: { move(-1) }) {
                Image(systemName: "chevron.left.circle.fill")
                    .font(.system(size: 44))
            }
            .disabled(index == 0)
            .accessibilityLabel(loc("Vorheriges Wort", "Previous word"))
            Button(action: { move(1) }) {
                Image(systemName: "chevron.right.circle.fill")
                    .font(.system(size: 44))
            }
            .disabled(index >= words.count - 1)
            .accessibilityLabel(loc("Nächstes Wort", "Next word"))
        }
        .foregroundColor(Theme.accent)
    }

    private var bottomButtons: some View {
        HStack(spacing: 14) {
            Button(action: read) {
                Label(loc("Lesen", "Read"), systemImage: "speaker.wave.2.fill")
                    .font(.title3.bold())
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
            }
            .buttonStyle(.borderedProminent)

            Button(action: spell) {
                Text("ABC")
                    .font(.title3.bold())
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
            }
            .buttonStyle(.borderedProminent)
            .tint(Theme.correct)
        }
        .frame(maxWidth: 420)
        .disabled(entry == nil)
    }

    // MARK: - Logik

    private func load() {
        let pool = RoundEngine.filtered(store.entries(forKey: settings.selectedList),
                                        settings: settings)
        words = store.isOrdered(forKey: settings.selectedList) ? pool : pool.shuffled()
        index = 0
    }

    private func move(_ delta: Int) {
        stopAll()
        cardSlid = false
        index = min(max(0, index + delta), max(0, words.count - 1))
    }

    /// Schablone gleitet von links nach rechts über das Wort, danach Audio.
    private func read() {
        stopAll()
        cardSlid = false
        guard let e = entry else { return }
        readTask = Task {
            try? await Task.sleep(nanoseconds: 200_000_000)
            guard !Task.isCancelled else { return }
            await MainActor.run {
                withAnimation(.easeInOut(duration: 1.6)) { cardSlid = true }
            }
            try? await Task.sleep(nanoseconds: 1_900_000_000)
            guard !Task.isCancelled else { return }
            await MainActor.run {
                Speech.shared.speak(e.word, language: language, accent: settings.englishAccent)
            }
        }
    }

    /// Buchstabe für Buchstabe sprechen, das Wort läuft farblich mit.
    private func spell() {
        stopAll()
        guard let e = entry else { return }
        let chars = Array(e.display(swiss: settings.swissSpelling))
        spellTask = Task {
            for i in chars.indices {
                guard !Task.isCancelled else { return }
                await MainActor.run {
                    spellIndex = i
                    Speech.shared.speakLetter(String(chars[i]), language: language,
                                              accent: settings.englishAccent)
                }
                try? await Task.sleep(nanoseconds: 900_000_000)
            }
            guard !Task.isCancelled else { return }
            // Zum Abschluss das ganze Wort einmal am Stück.
            await MainActor.run {
                spellIndex = nil
                Speech.shared.speak(e.word, language: language, accent: settings.englishAccent)
            }
        }
    }

    private func stopAll() {
        spellTask?.cancel()
        spellTask = nil
        spellIndex = nil
        readTask?.cancel()
        readTask = nil
        Speech.shared.stop()
    }
}
