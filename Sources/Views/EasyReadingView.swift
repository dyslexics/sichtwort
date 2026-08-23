import SwiftUI

/// „Easy Reading": digitale Nachbildung der EASY-Reading-Leseschablone
/// (20 × 8 cm, blaue Karte mit vier farbigen Eckfenstern). Bei „Lesen/Read"
/// gleitet die Karte von links nach rechts, das Wort wird durch das linke
/// obere Fenster sichtbar und anschließend vorgelesen. Bei „ABC" wandert
/// das Fenster Buchstabe für Buchstabe mit und jeder Buchstabe wird
/// gesprochen (immer klein: w-e-i-n). Schrift: immer OpenDyslexic.
struct EasyReadingView: View {
    @EnvironmentObject var store: AppStore
    @Environment(\.dismiss) private var dismiss

    /// Pause zwischen zwei Buchstaben beim Buchstabieren, gemessen ab Clipende.
    /// Zusammen mit der Stille am Clipende ergibt das rund 0,45 s Atem und einen
    /// Takt von etwa 0,77 s — der Rhythmus der Vorlage auf
    /// h15.drcag.com/STIMMEN/BUCHSTABIEREN/ („D, E, U, T, L, I, C, H — deutlich.").
    private static let letterGapSeconds: TimeInterval = 0.31
    /// Nur für Sprachen ohne Clip, wo das System-TTS spricht und die Dauer
    /// vorab unbekannt ist.
    private static let fallbackLetterSeconds: TimeInterval = 0.55

    @State private var words: [WordEntry] = []
    @State private var index = 0
    @State private var spellIndex: Int? = nil
    @State private var spellTask: Task<Void, Never>? = nil
    @State private var readTask: Task<Void, Never>? = nil
    /// x-Offset der Schablone; nil = Startposition links außerhalb.
    @State private var cardX: CGFloat? = nil
    @State private var containerW: CGFloat = 0
    @State private var letterFrames: [Int: CGRect] = [:]

    private var settings: ProfileSettings { store.current.settings }
    private var language: String { store.listLanguage(forKey: settings.selectedList) }
    private var textColor: Color { .black }
    private var entry: WordEntry? { words.indices.contains(index) ? words[index] : nil }

    // Geometrie der Schablone, abgeleitet aus der Containerbreite.
    // Deutlich größer als der Bildschirm und leicht nach links geschoben —
    // wie die echte Karte, die man übers Blatt schiebt.
    private var cardW: CGFloat { containerW * 2.2 }
    private var cardH: CGFloat { cardW / 2.5 }        // 20 × 8 cm
    private var winW: CGFloat { cardW * 0.26 }
    private var winH: CGFloat { cardH * 0.17 }
    private var startX: CGFloat { -20 - containerW * 0.5 }
    private var endX: CGFloat { -20 }

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
                Spacer()
                wordDisplay
                    .padding(.bottom, 10)
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

    /// Wort + darübergleitende Schablone. Das linke obere Fenster liegt am
    /// Ende der Lese-Bewegung bzw. während des Buchstabierens genau über
    /// dem aktuellen Buchstaben.
    private var cardArea: some View {
        GeometryReader { geo in
            ZStack(alignment: .topLeading) {
                hiddenWord
                overlayCard
                    .offset(x: cardX ?? (8 - geo.size.width * 0.5), y: 0)
            }
            .coordinateSpace(name: "easyCard")
            .onAppear { containerW = geo.size.width }
            .onChange(of: geo.size.width) { containerW = $0 }
        }
        .aspectRatio(1 / 0.88, contentMode: .fit)   // Höhe = cardH (2,2 / 2,5)
        .onPreferenceChange(LetterFramesKey.self) { letterFrames = $0 }
    }

    /// Das Wort unter der Schablone, Buchstabe für Buchstabe vermessen,
    /// damit das Fenster beim Buchstabieren exakt mitwandern kann.
    @ViewBuilder private var hiddenWord: some View {
        if let e = entry {
            let chars = Array(e.display(swiss: settings.swissSpelling))
            HStack(spacing: 0) {
                ForEach(chars.indices, id: \.self) { i in
                    Text(String(chars[i]))
                        .font(.system(size: winH * 0.55, weight: .black))
                        .foregroundColor(i == spellIndex ? Theme.accent : .black)
                        .background(GeometryReader { g in
                            Color.clear.preference(key: LetterFramesKey.self,
                                                   value: [i: g.frame(in: .named("easyCard"))])
                        })
                }
            }
            .lineLimit(1)
            .frame(height: winH)
            .padding(.leading, 16)
        }
    }

    /// Die Karte selbst: blauer Körper, vier durchscheinende Eckfenster, Logo.
    /// Das Lesefenster links oben glänzt (Verlauf + weiße Kante + Funkeln).
    private var overlayCard: some View {
        ZStack {
            VStack(spacing: 0) {
                HStack(spacing: 0) {
                    readingWindow.frame(width: winW)
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

    /// Linkes oberes Fenster: durchscheinendes Lavendel wie beim Original.
    private var readingWindow: some View {
        Rectangle().fill(winLavender.opacity(0.55))
    }

    // MARK: - Wort klein über den Pfeilen

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
                .font(.system(size: 20, weight: .semibold))
            } else {
                Text(loc("Keine Wörter in dieser Liste.", "No words in this list."))
                    .font(.headline)
                    .foregroundColor(textColor.opacity(0.7))
            }
        }
        .minimumScaleFactor(0.5)
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
        cardX = nil
        letterFrames = [:]
        index = min(max(0, index + delta), max(0, words.count - 1))
    }

    /// Schablone gleitet von links nach rechts über das Wort, danach Audio.
    private func read() {
        stopAll()
        cardX = startX
        guard let e = entry else { return }
        readTask = Task {
            try? await Task.sleep(nanoseconds: 200_000_000)
            guard !Task.isCancelled else { return }
            await MainActor.run {
                withAnimation(.easeInOut(duration: 1.6)) { cardX = endX }
            }
            try? await Task.sleep(nanoseconds: 1_900_000_000)
            guard !Task.isCancelled else { return }
            await MainActor.run {
                Speech.shared.speak(e.word, language: language, accent: settings.englishAccent, german: settings.germanVoice)
            }
        }
    }

    /// Buchstabiert klein (w-e-i-n); das Lesefenster gibt pro Schritt genau
    /// einen Buchstaben mehr frei (rechte Fensterkante wandert Buchstabe für
    /// Buchstabe nach rechts), das Wort unten läuft farblich mit.
    private func spell() {
        stopAll()
        guard let e = entry else { return }
        let chars = Array(e.display(swiss: settings.swissSpelling))
        spellTask = Task {
            for i in chars.indices {
                guard !Task.isCancelled else { return }
                let clip = await MainActor.run { () -> TimeInterval? in
                    spellIndex = i
                    if let f = letterFrames[i] {
                        withAnimation(.easeInOut(duration: 0.35)) {
                            cardX = f.maxX + 10 - winW
                        }
                    }
                    return Speech.shared.speakLetter(String(chars[i]), language: language,
                                                     accent: settings.englishAccent, german: settings.germanVoice)
                }
                // Nach dem Clip immer dieselbe Pause — nicht ein fester Takt.
                // Sonst hängt die Pause an der Cliplänge und „Ypsilon" (0,74 s)
                // ginge fast ohne Atem in den nächsten Buchstaben über, während
                // kurze Buchstaben zu lange stehen.
                let wait = (clip ?? Self.fallbackLetterSeconds) + Self.letterGapSeconds
                try? await Task.sleep(nanoseconds: UInt64(wait * 1_000_000_000))
            }
            guard !Task.isCancelled else { return }
            // Zum Abschluss das ganze Wort einmal am Stück, Fenster zum Wortanfang.
            await MainActor.run {
                spellIndex = nil
                withAnimation(.easeInOut(duration: 0.5)) { cardX = endX }
                Speech.shared.speak(e.word, language: language, accent: settings.englishAccent, german: settings.germanVoice)
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

/// Buchstaben-Positionen im Koordinatenraum "easyCard".
private struct LetterFramesKey: PreferenceKey {
    static var defaultValue: [Int: CGRect] = [:]
    static func reduce(value: inout [Int: CGRect], nextValue: () -> [Int: CGRect]) {
        value.merge(nextValue()) { _, new in new }
    }
}
