import Foundation
import SwiftUI

/// Sprachpakete: Wortliste + Audio-Clips einer Sprache als eine .swpack-Datei
/// von sichtwort.com. Format: "SWPK" + UInt32 Version + UInt32 Index-Länge +
/// JSON-Index {list, voice, clips: {wort: [offset, länge]}} + mp3-Blob.
/// Bewusst KEIN Apple On-Demand-Resources: iOS darf ODR-Packs bei
/// Speicherdruck löschen — für eine Offline-Kinder-App inakzeptabel.
struct PackInfo: Codable, Identifiable, Hashable {
    let code: String       // "es", "mx", ...
    let nameDE: String
    let nameEN: String
    let voice: String      // Anzeigename der Stimme, z. B. "Elvira"
    let sizeMB: Double
    let version: Int
    var id: String { code }
    var localizedName: String { loc(nameDE, nameEN) }
}

private struct PackIndex: Codable {
    let list: BuiltinList
    let voice: String
    let clips: [String: [UInt64]]  // Wort -> [Offset, Länge] relativ zum Blob-Start
}

final class PackManager: ObservableObject {
    static let shared = PackManager()

    @Published var downloaded: Set<String> = []
    @Published var progress: [String: Double] = [:]   // code -> 0..1 während Download
    @Published var lastError: String?

    let available: [PackInfo]

    private var indexCache: [String: PackIndex] = [:]
    private var dataCache: [String: Data] = [:]
    private var blobOffset: [String: Int] = [:]
    private var observations: [String: NSKeyValueObservation] = [:]

    private static let baseURL = URL(string: "https://sichtwort.com/packs")!

    private static var packsDir: URL {
        let dir = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("Sichtwort/packs", isDirectory: true)
        try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
        return dir
    }

    private init() {
        if let url = Bundle.main.url(forResource: "packs_manifest", withExtension: "json"),
           let data = try? Data(contentsOf: url),
           let infos = try? JSONDecoder().decode([PackInfo].self, from: data) {
            available = infos
        } else {
            available = []
        }
        let files = (try? FileManager.default.contentsOfDirectory(atPath: Self.packsDir.path)) ?? []
        downloaded = Set(files.filter { $0.hasSuffix(".swpack") }.map { String($0.dropLast(7)) })
    }

    private static func fileURL(_ code: String) -> URL {
        packsDir.appendingPathComponent("\(code).swpack")
    }

    // MARK: - Download

    func download(_ code: String) {
        guard progress[code] == nil else { return }
        progress[code] = 0
        lastError = nil
        let remote = Self.baseURL.appendingPathComponent("\(code).swpack")
        let task = URLSession.shared.downloadTask(with: remote) { [weak self] tmp, response, error in
            let moved: URL?
            if let tmp, error == nil, (response as? HTTPURLResponse)?.statusCode == 200 {
                let dest = Self.fileURL(code)
                try? FileManager.default.removeItem(at: dest)
                moved = (try? FileManager.default.moveItem(at: tmp, to: dest)) != nil ? dest : nil
            } else {
                moved = nil
            }
            DispatchQueue.main.async {
                guard let self else { return }
                self.observations[code] = nil
                self.progress[code] = nil
                guard moved != nil else {
                    self.lastError = loc("Download fehlgeschlagen — bitte Internetverbindung prüfen.",
                                         "Download failed — please check your internet connection.")
                    return
                }
                if self.loadIndex(code) == nil {
                    try? FileManager.default.removeItem(at: Self.fileURL(code))
                    self.lastError = loc("Paket beschädigt — bitte erneut versuchen.",
                                         "Package corrupted — please try again.")
                } else {
                    self.downloaded.insert(code)
                }
            }
        }
        observations[code] = task.progress.observe(\.fractionCompleted) { [weak self] p, _ in
            DispatchQueue.main.async { self?.progress[code] = p.fractionCompleted }
        }
        task.resume()
    }

    func delete(_ code: String) {
        try? FileManager.default.removeItem(at: Self.fileURL(code))
        downloaded.remove(code)
        indexCache[code] = nil
        dataCache[code] = nil
        blobOffset[code] = nil
    }

    // MARK: - Inhalt

    func list(_ code: String) -> BuiltinList? { loadIndex(code)?.list }

    func clipData(language code: String, word: String) -> Data? {
        guard let idx = loadIndex(code), let pos = idx.clips[word], pos.count == 2,
              let data = packData(code), let base = blobOffset[code] else { return nil }
        let start = base + Int(pos[0])
        let end = start + Int(pos[1])
        guard start >= 0, end <= data.count else { return nil }
        return data.subdata(in: start..<end)
    }

    private func packData(_ code: String) -> Data? {
        if let d = dataCache[code] { return d }
        guard let d = try? Data(contentsOf: Self.fileURL(code)) else { return nil }
        dataCache[code] = d
        return d
    }

    @discardableResult
    private func loadIndex(_ code: String) -> PackIndex? {
        if let i = indexCache[code] { return i }
        guard let data = packData(code), data.count > 12,
              data.subdata(in: 0..<4) == Data("SWPK".utf8) else { return nil }
        // subdata kopiert -> aligned, load(as:) ist sicher
        let indexLen = data.subdata(in: 8..<12).withUnsafeBytes { $0.load(as: UInt32.self) }
        let end = 12 + Int(indexLen)
        guard end <= data.count,
              let idx = try? JSONDecoder().decode(PackIndex.self, from: data.subdata(in: 12..<end))
        else { return nil }
        indexCache[code] = idx
        blobOffset[code] = end
        return idx
    }
}
