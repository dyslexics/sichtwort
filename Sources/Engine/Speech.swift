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
    func speak(_ text: String, language: String, accent: String = "us") {
        stop()
        // 1. Gebündelte Clips (de, en)
        if language == "de" || language == "en" {
            let prefix = language == "en" ? "en_\(accent == "gb" ? "gb" : "us")_" : "de_"
            if let url = clipURL(for: text, prefix: prefix),
               let p = try? AVAudioPlayer(contentsOf: url) {
                player = p
                p.play()
                return
            }
        }
        // 2. Clips aus heruntergeladenem Sprachpaket
        if let data = PackManager.shared.clipData(language: language, word: text),
           let p = try? AVAudioPlayer(data: data) {
            player = p
            p.play()
            return
        }
        // 3. Fallback: System-TTS (eigene Listen, fehlende Clips)
        let utterance = AVSpeechUtterance(string: text)
        var code = Self.fallbackVoice[language] ?? "de-DE"
        if language == "en" && accent == "gb" { code = "en-GB" }
        utterance.voice = AVSpeechSynthesisVoice(language: code)
        utterance.rate = 0.42
        synth.speak(utterance)
    }

    /// Buchstabiert einen einzelnen Buchstaben (immer System-TTS —
    /// Buchstabennamen wie „Be", „eS", „Eszett" liefert nur der Synthesizer).
    func speakLetter(_ letter: String, language: String, accent: String = "us") {
        player?.stop()
        player = nil
        synth.stopSpeaking(at: .immediate)
        var code = Self.fallbackVoice[language] ?? "de-DE"
        if language == "en" && accent == "gb" { code = "en-GB" }
        let utterance = AVSpeechUtterance(string: letter.uppercased())
        utterance.voice = AVSpeechSynthesisVoice(language: code)
        utterance.rate = 0.35
        synth.speak(utterance)
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
