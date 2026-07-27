import SwiftUI

/// „Easy Reading": ruhiges Lesen ohne Zeitdruck — ein Wort pro Seite,
/// unten „Vorlesen" (ganzes Wort) und „Buchstabieren" (Buchstabe für
/// Buchstabe; der gerade gesprochene Buchstabe wird im Wort hervorgehoben).
struct EasyReadingView: View {
    @EnvironmentObject var store: AppStore
    @Environment(\.dismiss) private var dismiss

    @State private var words: [WordEntry] = []
    @State private var index = 0
    @State private var spellIndex: Int? = nil
    @State private var spellTask: Task<Void, Never>? = nil

    private var settings: ProfileSettings { store.current.settings }
    private var language: String { store.listLanguage(forKey: settings.selectedList) }
    private var darkBG: Bool { Theme.isDarkBackground(settings.background) }
    private var textColor: Color { darkBG ? .white : .primary }
    private var entry: WordEntry? { words.indices.contains(index) ? words[index] : nil }

    var body: some View {
        ZStack {
            Theme.background(settings.background).ignoresSafeArea()
            VStack(spacing: 0) {
                header
                Spacer()
                wordDisplay
                Spacer()
                navRow
                    .padding(.bottom, 18)
                bottomButtons
            }
            .padding()
        }
        .onAppear(perform: load)
        .onDisappear { stopSpelling() }
    }

    private var header: some View {
        HStack {
            Button {
                stopSpelling()
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

    /// Wort mit Hervorhebung des gerade buchstabierten Buchstabens.
    private var wordDisplay: some View {
        Group {
            if let e = entry {
                let chars = Array(e.display(swiss: settings.swissSpelling))
                chars.indices.reduce(Text("")) { acc, i in
                    acc + Text(String(chars[i]))
                        .foregroundColor(i == spellIndex
                            ? (darkBG ? .orange : Theme.accent)
                            : (spellIndex == nil ? textColor : textColor.opacity(0.35)))
                }
                .font(Theme.wordFont(choice: settings.fontChoice, size: settings.fontSize, bold: true))
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
        .foregroundColor(darkBG ? .white : Theme.accent)
    }

    private var bottomButtons: some View {
        HStack(spacing: 14) {
            Button {
                stopSpelling()
                if let e = entry {
                    Speech.shared.speak(e.word, language: language, accent: settings.englishAccent)
                }
            } label: {
                Label(loc("Vorlesen", "Speak"), systemImage: "speaker.wave.2.fill")
                    .font(.title3.bold())
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
            }
            .buttonStyle(.borderedProminent)

            Button(action: spell) {
                Label(loc("Buchstabieren", "Pronounce"), systemImage: "textformat.abc")
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

    private func load() {
        let pool = RoundEngine.filtered(store.entries(forKey: settings.selectedList),
                                        settings: settings)
        words = store.isOrdered(forKey: settings.selectedList) ? pool : pool.shuffled()
        index = 0
    }

    private func move(_ delta: Int) {
        stopSpelling()
        index = min(max(0, index + delta), max(0, words.count - 1))
    }

    /// Buchstabe für Buchstabe sprechen, das Wort läuft farblich mit.
    private func spell() {
        stopSpelling()
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

    private func stopSpelling() {
        spellTask?.cancel()
        spellTask = nil
        spellIndex = nil
        Speech.shared.stop()
    }
}
