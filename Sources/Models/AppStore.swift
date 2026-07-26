import Foundation
import SwiftUI

/// Zentraler Zustand + Persistenz. Alles liegt als JSON in Application Support —
/// kein Backend, kein Tracking, keine Accounts.
final class AppStore: ObservableObject {
    @Published var profiles: [ChildProfile] = []
    @Published var customLists: [CustomList] = []
    @Published var currentProfileID: UUID?

    let builtinLists: [BuiltinList]

    private struct PersistedState: Codable {
        var version: Int = 1
        var profiles: [ChildProfile]
        var customLists: [CustomList]
        var currentProfileID: UUID?
    }

    private static var fileURL: URL {
        let dir = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("Sichtwort", isDirectory: true)
        try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir.appendingPathComponent("state.json")
    }

    init() {
        builtinLists = WordLists.loadBuiltin()
        load()
        if ProcessInfo.processInfo.arguments.contains("-demoData") {
            installDemoData()
        }
        if profiles.isEmpty {
            let p = ChildProfile(name: loc("Mein Kind", "My child"))
            profiles = [p]
            currentProfileID = p.id
        }
        if currentProfileID == nil || !profiles.contains(where: { $0.id == currentProfileID }) {
            currentProfileID = profiles.first?.id
        }
    }

    var current: ChildProfile {
        get { profiles.first { $0.id == currentProfileID } ?? profiles[0] }
        set {
            if let i = profiles.firstIndex(where: { $0.id == newValue.id }) {
                profiles[i] = newValue
                save()
            }
        }
    }

    func binding() -> Binding<ChildProfile> {
        Binding(get: { self.current }, set: { self.current = $0 })
    }

    // MARK: - Listen

    func entries(forKey key: String) -> [WordEntry] {
        if key.hasPrefix("custom:"), let uuid = UUID(uuidString: String(key.dropFirst(7))) {
            return customLists.first { $0.id == uuid }?.entries ?? []
        }
        if key.hasPrefix("pack:") {
            return PackManager.shared.list(String(key.dropFirst(5)))?.entries ?? []
        }
        return builtinLists.first { $0.id == key }?.entries ?? []
    }

    func listName(forKey key: String) -> String {
        if key.hasPrefix("custom:"), let uuid = UUID(uuidString: String(key.dropFirst(7))) {
            return customLists.first { $0.id == uuid }?.name ?? "?"
        }
        if key.hasPrefix("pack:") {
            return PackManager.shared.list(String(key.dropFirst(5)))?.localizedName ?? "?"
        }
        return builtinLists.first { $0.id == key }?.localizedName ?? "?"
    }

    func listLanguage(forKey key: String) -> String {
        if key.hasPrefix("custom:"), let uuid = UUID(uuidString: String(key.dropFirst(7))) {
            return customLists.first { $0.id == uuid }?.language ?? "de"
        }
        if key.hasPrefix("pack:") {
            return String(key.dropFirst(5))
        }
        return builtinLists.first { $0.id == key }?.language ?? "de"
    }

    func isOrdered(forKey key: String) -> Bool {
        if key.hasPrefix("custom:"), let uuid = UUID(uuidString: String(key.dropFirst(7))) {
            return customLists.first { $0.id == uuid }?.ordered ?? false
        }
        return false
    }

    // MARK: - Persistenz

    func load() {
        guard let data = try? Data(contentsOf: Self.fileURL),
              let state = try? JSONDecoder().decode(PersistedState.self, from: data)
        else { return }
        profiles = state.profiles
        customLists = state.customLists
        currentProfileID = state.currentProfileID
        // Migration v1->v2: Standard-Hintergrund wurde von Wiese auf Meer geändert;
        // Profile mit dem alten Default einmalig umstellen.
        if state.version < 2 {
            for i in profiles.indices where profiles[i].settings.background == "wiese" {
                profiles[i].settings.background = "meer"
            }
            save()
        }
    }

    func save() {
        let state = PersistedState(version: 2, profiles: profiles, customLists: customLists, currentProfileID: currentProfileID)
        if let data = try? JSONEncoder().encode(state) {
            try? data.write(to: Self.fileURL, options: .atomic)
        }
    }

    // MARK: - Demo-Daten (Screenshots/Video)

    private func installDemoData() {
        var p = ChildProfile(name: "Noah")
        p.stars = 137
        p.companionPose = "jubelnd"
        let cal = Calendar.current
        for day in (0..<12).reversed() {
            let d = cal.date(byAdding: .day, value: -day, to: Date()) ?? Date()
            let total = 10
            let correct = min(total, 5 + (12 - day) / 2)
            p.roundHistory.append(RoundRecord(
                date: d, listName: "Grundwortschatz 500",
                correct: correct, total: total,
                flashTime: max(0.4, 1.5 - Double(12 - day) * 0.08)))
        }
        p.errorBox = ["Fahrrad": 2, "Straße": 1, "springt": 3]
        var list = CustomList(name: loc("Liste für Noah", "List for Noah"))
        list.entries = CSV.parse("Fahrrad;Fahr-rad\nSchule;Schu-le\nFreund;Freund\nlesen;le-sen\nStraße;Stra-ße")
        profiles = [p]
        customLists = [list]
        currentProfileID = p.id
    }
}
