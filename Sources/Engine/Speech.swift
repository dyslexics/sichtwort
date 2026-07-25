import AVFoundation

/// Sprachausgabe on-device via AVSpeechSynthesizer — komplett offline,
/// die größte funktionale Lücke des Originals.
final class Speech {
    static let shared = Speech()
    private let synth = AVSpeechSynthesizer()

    func speak(_ text: String, language: String) {
        synth.stopSpeaking(at: .immediate)
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = AVSpeechSynthesisVoice(language: language == "en" ? "en-US" : "de-DE")
        utterance.rate = 0.42
        synth.speak(utterance)
    }

    func stop() {
        synth.stopSpeaking(at: .immediate)
    }
}
