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

    func speak(_ text: String, language: String) {
        stop()
        if language == "de", let url = clipURL(for: text),
           let p = try? AVAudioPlayer(contentsOf: url) {
            player = p
            p.play()
            return
        }
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = AVSpeechSynthesisVoice(language: language == "en" ? "en-US" : "de-DE")
        utterance.rate = 0.42
        synth.speak(utterance)
    }

    private func clipURL(for word: String) -> URL? {
        let digest = Insecure.MD5.hash(data: Data(word.utf8))
        let hex = digest.map { String(format: "%02x", $0) }.joined()
        return Bundle.main.url(forResource: "de_" + hex, withExtension: "mp3")
    }

    func stop() {
        synth.stopSpeaking(at: .immediate)
        player?.stop()
        player = nil
    }
}
