import AVFoundation
import CryptoKit

/// Sprachausgabe — komplett offline, die größte funktionale Lücke des Originals.
/// Deutsche Wörter: gebündelte Seraphina-Clips (edge-tts, de-DE-SeraphinaMultilingualNeural),
/// Dateiname de_<md5(wort)>.mp3 (md5 wegen Case-Kollisionen wie Weg/weg).
/// Fallback (eigene Listen, Englisch): AVSpeechSynthesizer.
final class Speech {
    static let shared = Speech()
    private let synth = AVSpeechSynthesizer()
    private var player: AVAudioPlayer?

    private init() {
        try? AVAudioSession.sharedInstance().setCategory(.playback, options: [.duckOthers])
    }

    /// BCP-47-Fallback-Stimmen für alle Paket-Sprachen (nur wenn kein Clip da ist).
    private static let fallbackVoice: [String: String] = [
        "de": "de-DE", "en": "en-US", "es": "es-ES", "mx": "es-MX", "fr": "fr-FR",
        "it": "it-IT", "tr": "tr-TR", "el": "el-GR", "hu": "hu-HU", "ar": "ar-SA",
        "bs": "hr-HR", "ro": "ro-RO", "sq": "sq-AL", "uk": "uk-UA", "af": "af-ZA",
        "nl": "nl-NL", "pt": "pt-PT", "br": "pt-BR", "da": "da-DK", "no": "nb-NO",
        "pl": "pl-PL",
    ]

    /// accent gilt nur für Englisch: "us" (Ava) oder "gb" (Sonia).
    /// Gibt die Länge des abgespielten Clips zurück, oder nil beim System-TTS
    /// (dessen Dauer steht vorab nicht fest). Aufrufer, die den Takt danach
    /// richten wollen — etwa das Buchstabieren — brauchen diesen Wert.
    @discardableResult
    func speak(_ text: String, language: String, accent: String = "us") -> TimeInterval? {
        stop()
        // 1. Gebündelte Clips (de, en)
        if language == "de" || language == "en" {
            let prefix = language == "en" ? "en_\(accent == "gb" ? "gb" : "us")_" : "de_"
            if let url = clipURL(for: text, prefix: prefix),
               let p = try? AVAudioPlayer(contentsOf: url) {
                player = p
                p.play()
                return p.duration
            }
        }
        // 2. Clips aus heruntergeladenem Sprachpaket
        if let data = PackManager.shared.clipData(language: language, word: text),
           let p = try? AVAudioPlayer(data: data) {
            player = p
            p.play()
            return p.duration
        }
        // 3. Fallback: System-TTS (eigene Listen, fehlende Clips)
        let utterance = AVSpeechUtterance(string: text)
        var code = Self.fallbackVoice[language] ?? "de-DE"
        if language == "en" && accent == "gb" { code = "en-GB" }
        utterance.voice = AVSpeechSynthesisVoice(language: code)
        utterance.rate = 0.42
        synth.speak(utterance)
        return nil
    }

    /// Buchstabiert einen einzelnen Buchstaben — dieselbe Clip-Kette wie
    /// speak() (gebündelter Clip → Sprachpaket → System-TTS), damit Wort und
    /// Buchstaben mit derselben Stimme gesprochen werden. Immer kleingeschrieben:
    /// „Wein" wird w-e-i-n buchstabiert, unabhängig von der Schreibweise.
    @discardableResult
    func speakLetter(_ letter: String, language: String, accent: String = "us") -> TimeInterval? {
        speak(letter.lowercased(), language: language, accent: accent)
    }

    private func clipURL(for word: String, prefix: String) -> URL? {
        let digest = Insecure.MD5.hash(data: Data(word.utf8))
        let hex = digest.map { String(format: "%02x", $0) }.joined()
        return Bundle.main.url(forResource: prefix + hex, withExtension: "mp3")
    }

    func stop() {
        synth.stopSpeaking(at: .immediate)
        player?.stop()
        player = nil
    }
}
