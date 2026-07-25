import Foundation

/// Einstellungen pro Kind — alles lokal, keine Accounts.
struct ProfileSettings: Codable, Hashable {
    var flashTime: Double = 1.0        // 0,02–5,0 s
    var roundSize: Int = 10            // 5–40
    var teacherMode: Bool = true       // false = Alleine-Modus (Tippen)
    var adaptive: Bool = false         // Abenteuer-Modus
    var fontChoice: String = "system"  // system | dyslexic | lexend
    var fontSize: Double = 64          // 36–120
    var syllableMode: String = "none"  // none | colored | sequential
    var tts: Bool = true
    var swissSpelling: Bool = false
    var background: String = "wiese"
    var selectedList: String = "de500" // Builtin-ID oder "custom:<uuid>"
    var typeFilter: [String] = []      // leer = alle Wortarten
    var syllableFilter: String = "all" // all | 1 | 2 | 3plus
}

struct RoundRecord: Codable, Identifiable, Hashable {
    var id: UUID = UUID()
    var date: Date
    var listName: String
    var correct: Int
    var total: Int
    var flashTime: Double
}

struct ChildProfile: Codable, Identifiable, Hashable {
    var id: UUID = UUID()
    var name: String
    var stars: Int = 0
    var companionPose: String = "winkend"
    /// Leitner-light: falsch gelesene Wörter -> Restgewicht (3 = dreimal richtig nötig).
    var errorBox: [String: Int] = [:]
    var roundHistory: [RoundRecord] = []
    /// Garantierte Abdeckung: pro Liste die noch nicht gespielten Wort-Indizes.
    var listCursors: [String: [Int]] = [:]
    var settings: ProfileSettings = ProfileSettings()

    var totalCorrect: Int { roundHistory.reduce(0) { $0 + $1.correct } }
    var totalWords: Int { roundHistory.reduce(0) { $0 + $1.total } }

    /// Endloses Level-System: Level 1 ab 0, danach alle 100 Sterne.
    var level: Int { stars / 100 + 1 }
    var starsIntoLevel: Int { stars % 100 }
}
