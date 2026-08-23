import SwiftUI

@main
struct SichtwortApp: App {
    @StateObject private var store = AppStore()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environmentObject(store)
                .tint(Theme.accent)
        }
    }
}

struct RootView: View {
    @EnvironmentObject var store: AppStore
    @State private var tab: Int

    init() {
        var initial = 0
        let args = ProcessInfo.processInfo.arguments
        if let i = args.firstIndex(of: "-tab"), i + 1 < args.count, let n = Int(args[i + 1]) {
            initial = n
        }
        _tab = State(initialValue: initial)
    }

    var body: some View {
        TabView(selection: $tab) {
            HomeView()
                .tabItem { Label(loc("Üben", "Practice"), systemImage: "bolt.fill") }
                .tag(0)
            ListsView()
                .tabItem { Label(loc("Listen", "Lists"), systemImage: "list.bullet.rectangle") }
                .tag(1)
            RewardsView()
                .tabItem { Label(loc("Belohnungen", "Rewards"), systemImage: "star.fill") }
                .tag(2)
            StatsView()
                .tabItem { Label(loc("Statistik", "Statistics"), systemImage: "chart.bar.fill") }
                .tag(3)
            SettingsView()
                .tabItem { Label(loc("Einstellungen", "Settings"), systemImage: "gearshape.fill") }
                .tag(4)
        }
    }
}

/// Sprache von Menü und App-Führung. „system" folgt der Gerätesprache,
/// „de"/„en" erzwingen sie — nötig, weil auf einem englisch eingestellten
/// Gerät trotzdem deutsch geübt wird (und umgekehrt).
/// Liegt in UserDefaults, nicht im Kind-Profil: die Bediensprache gehört
/// zum Gerät, nicht zum Kind.
enum UILanguage {
    private static let key = "uiLanguage"

    static var setting: String {
        get { UserDefaults.standard.string(forKey: key) ?? "system" }
        set { UserDefaults.standard.set(newValue, forKey: key) }
    }

    static var isEnglish: Bool {
        switch setting {
        case "de": return false
        case "en": return true
        default: return (Locale.preferredLanguages.first ?? "de").hasPrefix("en")
        }
    }
}

/// Zweisprachigkeit ohne xcstrings: UI folgt der Einstellung „Sprache der App",
/// standardmäßig der Gerätesprache. Standard Deutsch.
func loc(_ de: String, _ en: String) -> String {
    let args = ProcessInfo.processInfo.arguments
    if let i = args.firstIndex(of: "-lang"), i + 1 < args.count {
        return args[i + 1] == "en" ? en : de
    }
    return UILanguage.isEnglish ? en : de
}

enum Theme {
    static let accent = Color(red: 0x26 / 255.0, green: 0x43 / 255.0, blue: 0x98 / 255.0) // EÖDL #264398
    static let correct = Color(red: 0.20, green: 0.65, blue: 0.30)
    static let wrong = Color(red: 0.85, green: 0.25, blue: 0.20)

    /// Schrift für die Wortdarstellung (Schriftwahl ist ein Kernfeature).
    static func wordFont(choice: String, size: CGFloat, bold: Bool = false) -> Font {
        switch choice {
        case "dyslexic": return .custom(bold ? "OpenDyslexic-Bold" : "OpenDyslexic-Regular", size: size)
        case "lexend": return .custom("Lexend-Regular", size: size)
        default: return .system(size: size, weight: bold ? .bold : .medium, design: .rounded)
        }
    }

    static let syllableColors: [Color] = [
        Color(red: 0x26 / 255.0, green: 0x43 / 255.0, blue: 0x98 / 255.0),
        Color(red: 0.80, green: 0.30, blue: 0.10),
    ]

    static let backgrounds: [(id: String, de: String, en: String, colors: [Color])] = [
        ("meer", "Meer", "Ocean", [Color(red: 0.80, green: 0.93, blue: 0.98), Color(red: 0.45, green: 0.72, blue: 0.92)]),
        ("wiese", "Wiese", "Meadow", [Color(red: 0.85, green: 0.95, blue: 0.80), Color(red: 0.62, green: 0.85, blue: 0.55)]),
        ("weltall", "Weltall", "Space", [Color(red: 0.16, green: 0.16, blue: 0.35), Color(red: 0.05, green: 0.05, blue: 0.15)]),
        ("wueste", "Wüste", "Desert", [Color(red: 0.99, green: 0.93, blue: 0.78), Color(red: 0.93, green: 0.76, blue: 0.48)]),
        ("wald", "Wald", "Forest", [Color(red: 0.80, green: 0.90, blue: 0.78), Color(red: 0.35, green: 0.58, blue: 0.38)]),
    ]

    static func background(_ id: String) -> LinearGradient {
        let def = backgrounds.first { $0.id == id } ?? backgrounds[0]
        return LinearGradient(colors: def.colors, startPoint: .top, endPoint: .bottom)
    }

    /// Dunkle Hintergründe brauchen helle Schrift.
    static func isDarkBackground(_ id: String) -> Bool { id == "weltall" }
}

/// Maskottchen-Posen und ihre Freischalt-Schwellen (Sterne).
enum Mascot {
    static let poses: [(name: String, stars: Int, de: String, en: String)] = [
        ("winkend", 0, "Winken", "Waving"),
        ("laufend", 10, "Loslaufen", "Running"),
        ("jubelnd", 25, "Jubeln", "Cheering"),
        ("lesend", 50, "Lesen", "Reading"),
        ("tanzend", 80, "Tanzen", "Dancing"),
        ("gluehbirne", 120, "Gute Idee", "Bright idea"),
        ("tafel", 170, "An der Tafel", "At the board"),
        ("hanteln", 230, "Training", "Training"),
        ("malerin", 300, "Malen", "Painting"),
    ]

    static func unlocked(stars: Int) -> [String] {
        poses.filter { $0.stars <= stars }.map { $0.name }
    }
}

struct MascotImage: View {
    let pose: String
    var height: CGFloat = 120

    var body: some View {
        if let ui = UIImage(named: pose) {
            Image(uiImage: ui)
                .resizable()
                .scaledToFit()
                .frame(height: height)
                .accessibilityHidden(true)
        }
    }
}
