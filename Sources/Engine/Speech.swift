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

    /// accent gilt nur für Englisch: "us" (Ava) oder "gb" (Sonia).
    func speak(_ text: String, language: String, accent: String = "us") {
        stop()
        let prefix = language == "en" ? "en_\(accent == "gb" ? "gb" : "us")_" : "de_"
        if let url = clipURL(for: text, prefix: prefix),
           let p = try? AVAudioPlayer(contentsOf: url) {
            player = p
            p.play()
            return
        }
        let utterance = AVSpeechUtterance(string: text)
        let voice = language == "en" ? (accent == "gb" ? "en-GB" : "en-US") : "de-DE"
        utterance.voice = AVSpeechSynthesisVoice(language: voice)
        utterance.rate = 0.42
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
