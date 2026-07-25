import Foundation

/// Ein Wort mit Silbenmarkierung ("Fens-ter") und Wortart (n/v/a/o).
struct WordEntry: Codable, Hashable, Identifiable {
    let syl: String
    let type: String

    var id: String { syl }
    var word: String { syl.replacingOccurrences(of: "-", with: "") }
    var syllables: [String] { syl.components(separatedBy: "-") }
    var syllableCount: Int { syllables.count }

    /// Schweizer Schreibweise: ß -> ss (nur Darstellung/Prüfung).
    func display(swiss: Bool) -> String {
        swiss ? word.replacingOccurrences(of: "ß", with: "ss") : word
    }

    func displaySyllables(swiss: Bool) -> [String] {
        swiss ? syllables.map { $0.replacingOccurrences(of: "ß", with: "ss") } : syllables
    }
}

/// Mitgelieferte Liste aus dem Bundle (WordLists/*.json).
struct BuiltinList: Codable, Identifiable {
    let id: String
    let language: String
    let nameDE: String
    let nameEN: String
    let words: [[String]]

    var entries: [WordEntry] {
        words.compactMap { pair in
            guard pair.count >= 2 else { return nil }
            return WordEntry(syl: pair[0], type: pair[1])
        }
    }

    var localizedName: String { loc(nameDE, nameEN) }
}

/// Vom Nutzer angelegte Liste (auch CSV-Import).
struct CustomList: Codable, Identifiable, Hashable {
    var id: UUID = UUID()
    var name: String
    var language: String = "de"
    var ordered: Bool = false // true = feste Reihenfolge statt Zufall
    var entries: [WordEntry] = []
}

enum WordLists {
    /// Reihenfolge der Anzeige: Grundwortschatz, Themen, Englisch.
    static let builtinOrder = [
        "de500", "de1000",
        "theme_silben", "theme_dehnungs_h", "theme_ei_ie", "theme_doppelkonsonanten",
        "theme_sch", "theme_sp_st", "theme_d_t", "theme_weltraum",
        "en_dolch", "en_fry",
    ]

    static func loadBuiltin() -> [BuiltinList] {
        var lists: [BuiltinList] = []
        for name in builtinOrder {
            guard let url = Bundle.main.url(forResource: name, withExtension: "json"),
                  let data = try? Data(contentsOf: url),
                  let list = try? JSONDecoder().decode(BuiltinList.self, from: data)
            else { continue }
            lists.append(list)
        }
        return lists
    }
}

enum CSV {
    /// Import: eine Zeile pro Wort, optional zweite Spalte mit Silbenform ("Fens-ter").
    /// Trennzeichen ; oder , — Kopfzeilen und Leerzeilen werden übersprungen.
    static func parse(_ text: String) -> [WordEntry] {
        var result: [WordEntry] = []
        var seen = Set<String>()
        for rawLine in text.components(separatedBy: .newlines) {
            let line = rawLine.trimmingCharacters(in: .whitespaces)
            if line.isEmpty { continue }
            let sep: Character = line.contains(";") ? ";" : ","
            let cols = line.split(separator: sep, omittingEmptySubsequences: false)
                .map { $0.trimmingCharacters(in: .whitespaces) }
            guard let word = cols.first, !word.isEmpty else { continue }
            if word.lowercased() == "wort" || word.lowercased() == "word" { continue }
            let syl: String
            if cols.count > 1, !cols[1].isEmpty,
               cols[1].replacingOccurrences(of: "-", with: "") == word {
                syl = cols[1]
            } else {
                syl = word
            }
            let key = word.lowercased()
            if seen.contains(key) { continue }
            seen.insert(key)
            let first = word.first.map(String.init) ?? ""
            let type = first == first.uppercased() && first != first.lowercased() ? "n" : "o"
            result.append(WordEntry(syl: syl, type: type))
        }
        return result
    }

    static func export(_ list: CustomList) -> String {
        var lines = ["Wort;Silben"]
        for e in list.entries {
            lines.append("\(e.word);\(e.syl)")
        }
        return lines.joined(separator: "\n")
    }
}
