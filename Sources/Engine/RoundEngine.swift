import Foundation

/// Baut die Wortfolge einer Runde und verwaltet Bewertung, Fehler-Wiedervorlage
/// (Leitner-light) und den adaptiven Modus.
///
/// Garantierte Abdeckung: Pro Liste wird ein Cursor mit den noch nicht gespielten
/// Wort-Indizes im Profil gehalten. Runden ziehen daraus ohne Zurücklegen; erst wenn
/// alle Wörter dran waren, wird neu gemischt. (Kritikpunkt am Original: "nicht
/// garantiert alle Wörter einer Liste".)
struct RoundPlan {
    var words: [WordEntry]
    var listKey: String
    var listName: String
}

enum RoundEngine {

    static func filtered(_ entries: [WordEntry], settings: ProfileSettings) -> [WordEntry] {
        entries.filter { e in
            if !settings.typeFilter.isEmpty && !settings.typeFilter.contains(e.type) { return false }
            switch settings.syllableFilter {
            case "1": return e.syllableCount == 1
            case "2": return e.syllableCount == 2
            case "3plus": return e.syllableCount >= 3
            default: return true
            }
        }
    }

    /// Erzeugt den Rundenplan und aktualisiert den Listen-Cursor im Profil.
    static func buildRound(store: AppStore, profile: inout ChildProfile) -> RoundPlan {
        let key = profile.settings.selectedList
        let all = store.entries(forKey: key)
        let pool = filtered(all, settings: profile.settings)
        let ordered = store.isOrdered(forKey: key)
        let size = max(1, min(profile.settings.roundSize, max(pool.count, 1)))

        guard !pool.isEmpty else {
            return RoundPlan(words: [], listKey: key, listName: store.listName(forKey: key))
        }

        // Cursor-Schlüssel enthält die Filter, damit Filterwechsel sauber neu starten.
        let cursorKey = "\(key)|\(profile.settings.typeFilter.sorted().joined())|\(profile.settings.syllableFilter)"
        var remaining = profile.listCursors[cursorKey] ?? []
        remaining.removeAll { $0 >= pool.count }
        if remaining.isEmpty {
            remaining = Array(0..<pool.count)
            if !ordered { remaining.shuffle() }
        }

        var indices: [Int] = []
        while indices.count < size {
            if remaining.isEmpty {
                remaining = Array(0..<pool.count)
                if !ordered { remaining.shuffle() }
                // Doppelte direkt hintereinander vermeiden
                if let last = indices.last, remaining.first == last, remaining.count > 1 {
                    remaining.swapAt(0, 1)
                }
            }
            indices.append(remaining.removeFirst())
        }
        profile.listCursors[cursorKey] = remaining

        var words = indices.map { pool[$0] }

        // Fehler-Wiedervorlage: bis zu 20 % der Runde aus der Fehlerbox (gleiche Sprache).
        let dueWords = profile.errorBox.keys.filter { boxWord in
            all.contains { $0.word == boxWord }
        }
        if !dueWords.isEmpty {
            let slots = max(1, size / 5)
            for (i, w) in dueWords.shuffled().prefix(slots).enumerated() {
                if let entry = all.first(where: { $0.word == w }), !words.contains(entry) {
                    let pos = min(i * 2 + 1, words.count - 1)
                    words[pos] = entry
                }
            }
        }

        return RoundPlan(words: words, listKey: key, listName: store.listName(forKey: key))
    }

    /// Bewertung eines Worts: Sterne, Fehlerbox pflegen.
    static func mark(profile: inout ChildProfile, entry: WordEntry, correct: Bool) {
        if correct {
            profile.stars += 1
            if let w = profile.errorBox[entry.word] {
                if w <= 1 { profile.errorBox.removeValue(forKey: entry.word) }
                else { profile.errorBox[entry.word] = w - 1 }
            }
        } else {
            profile.errorBox[entry.word] = 3
        }
    }

    /// Adaptiver Modus: 3 richtige in Folge -> schneller, jeder Fehler -> langsamer.
    static func adaptedTime(current: Double, streak: Int, lastCorrect: Bool) -> Double {
        if !lastCorrect {
            return min(5.0, current * 1.3)
        }
        if streak > 0 && streak % 3 == 0 {
            return max(0.15, current * 0.85)
        }
        return current
    }

    static func finishRound(profile: inout ChildProfile, plan: RoundPlan, correct: Int, flashTime: Double) {
        profile.roundHistory.append(RoundRecord(
            date: Date(), listName: plan.listName,
            correct: correct, total: plan.words.count, flashTime: flashTime))
        if profile.roundHistory.count > 300 {
            profile.roundHistory.removeFirst(profile.roundHistory.count - 300)
        }
    }
}
