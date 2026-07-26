import SwiftUI
import UniformTypeIdentifiers

/// Wortlisten: mitgeliefert (alles gratis) + eigene Listen mit CSV-Import UND -Export.
struct ListsView: View {
    @EnvironmentObject var store: AppStore
    @ObservedObject private var packs = PackManager.shared
    @State private var showImporter = false
    @State private var newListName = ""
    @State private var showNewList = false
    @State private var exportList: CustomList?
    @State private var importError: String?

    private var selectedKey: String { store.current.settings.selectedList }

    var body: some View {
        NavigationStack {
            List {
                Section(loc("Grundwortschatz", "Basic vocabulary")) {
                    ForEach(store.builtinLists.filter { $0.id.hasPrefix("de") }) { list in
                        builtinRow(list)
                    }
                }
                Section(loc("Themenlisten (alle gratis)", "Theme lists (all free)")) {
                    ForEach(store.builtinLists.filter { $0.id.hasPrefix("theme") }) { list in
                        builtinRow(list)
                    }
                }
                Section(loc("Englisch", "English")) {
                    ForEach(store.builtinLists.filter { $0.id.hasPrefix("en") }) { list in
                        builtinRow(list)
                    }
                }
                if !packs.available.isEmpty {
                    Section {
                        ForEach(packs.available) { pack in
                            packRow(pack)
                        }
                    } header: {
                        Text(loc("Weitere Sprachen", "More languages"))
                    } footer: {
                        Text(loc("Sprachpakete werden einmalig geladen (je ca. 3–4 MB) und funktionieren danach komplett offline.",
                                 "Language packs download once (about 3–4 MB each) and then work fully offline."))
                    }
                }
                Section {
                    ForEach(store.customLists) { list in
                        customRow(list)
                    }
                    .onDelete { idx in
                        store.customLists.remove(atOffsets: idx)
                        store.save()
                    }
                    .onMove { from, to in
                        store.customLists.move(fromOffsets: from, toOffset: to)
                        store.save()
                    }
                    Button {
                        showNewList = true
                    } label: {
                        Label(loc("Neue Liste", "New list"), systemImage: "plus.circle.fill")
                    }
                    Button {
                        showImporter = true
                    } label: {
                        Label(loc("CSV importieren", "Import CSV"), systemImage: "square.and.arrow.down")
                    }
                } header: {
                    Text(loc("Eigene Listen", "My lists"))
                } footer: {
                    Text(loc("CSV: ein Wort pro Zeile, optional zweite Spalte mit Silben (Fens-ter).",
                             "CSV: one word per line, optional second column with syllables (lit-tle)."))
                }
            }
            .navigationTitle(loc("Wortlisten", "Word lists"))
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    MascotImage(pose: "lesend", height: 36)
                }
            }
            .alert(loc("Neue Liste", "New list"), isPresented: $showNewList) {
                TextField(loc("Name", "Name"), text: $newListName)
                Button(loc("Anlegen", "Create")) {
                    let name = newListName.trimmingCharacters(in: .whitespaces)
                    if !name.isEmpty {
                        store.customLists.append(CustomList(name: name))
                        store.save()
                    }
                    newListName = ""
                }
                Button(loc("Abbrechen", "Cancel"), role: .cancel) { newListName = "" }
            }
            .alert(loc("Sprachpaket", "Language pack"),
                   isPresented: Binding(get: { packs.lastError != nil }, set: { _ in packs.lastError = nil })) {
                Button("OK", role: .cancel) {}
            } message: {
                Text(packs.lastError ?? "")
            }
            .alert(loc("Import fehlgeschlagen", "Import failed"),
                   isPresented: Binding(get: { importError != nil }, set: { _ in importError = nil })) {
                Button("OK", role: .cancel) {}
            } message: {
                Text(importError ?? "")
            }
            .fileImporter(isPresented: $showImporter,
                          allowedContentTypes: [.commaSeparatedText, .plainText, .text]) { result in
                handleImport(result)
            }
            .fileExporter(isPresented: Binding(get: { exportList != nil }, set: { if !$0 { exportList = nil } }),
                          document: CSVDocument(text: exportList.map(CSV.export) ?? ""),
                          contentType: .commaSeparatedText,
                          defaultFilename: (exportList?.name ?? "liste") + ".csv") { _ in
                exportList = nil
            }
        }
    }

    private func builtinRow(_ list: BuiltinList) -> some View {
        Button {
            selectList(list.id)
        } label: {
            HStack {
                VStack(alignment: .leading, spacing: 2) {
                    Text(list.localizedName).foregroundColor(.primary)
                    Text(loc("\(list.entries.count) Wörter", "\(list.entries.count) words"))
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                Spacer()
                if selectedKey == list.id {
                    Image(systemName: "checkmark.circle.fill").foregroundColor(Theme.accent)
                }
            }
        }
    }

    @ViewBuilder
    private func packRow(_ pack: PackInfo) -> some View {
        let key = "pack:\(pack.code)"
        if packs.downloaded.contains(pack.code) {
            Button {
                selectList(key)
            } label: {
                HStack {
                    VStack(alignment: .leading, spacing: 2) {
                        Text(pack.localizedName).foregroundColor(.primary)
                        Text(loc("Stimme: \(pack.voice)", "Voice: \(pack.voice)"))
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                    Spacer()
                    if selectedKey == key {
                        Image(systemName: "checkmark.circle.fill").foregroundColor(Theme.accent)
                    }
                }
            }
            .swipeActions {
                Button(role: .destructive) {
                    packs.delete(pack.code)
                    if selectedKey == key { selectList("de500") }
                } label: {
                    Label(loc("Löschen", "Delete"), systemImage: "trash")
                }
            }
        } else if let p = packs.progress[pack.code] {
            HStack {
                Text(pack.localizedName)
                Spacer()
                ProgressView(value: p).frame(width: 90)
            }
        } else {
            Button {
                packs.download(pack.code)
            } label: {
                HStack {
                    VStack(alignment: .leading, spacing: 2) {
                        Text(pack.localizedName).foregroundColor(.primary)
                        Text(String(format: loc("%.1f MB — Stimme: %@", "%.1f MB — voice: %@"),
                                    pack.sizeMB, pack.voice))
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                    Spacer()
                    Image(systemName: "arrow.down.circle.fill")
                        .font(.title3)
                        .foregroundColor(Theme.accent)
                }
            }
        }
    }

    private func customRow(_ list: CustomList) -> some View {
        NavigationLink {
            CustomListEditor(listID: list.id)
        } label: {
            HStack {
                VStack(alignment: .leading, spacing: 2) {
                    Text(list.name)
                    Text(loc("\(list.entries.count) Wörter · \(list.language == "en" ? "Englisch" : "Deutsch")\(list.ordered ? " · feste Reihenfolge" : "")",
                             "\(list.entries.count) words · \(list.language == "en" ? "English" : "German")\(list.ordered ? " · fixed order" : "")"))
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                Spacer()
                if selectedKey == "custom:\(list.id.uuidString)" {
                    Image(systemName: "checkmark.circle.fill").foregroundColor(Theme.accent)
                }
                Button {
                    exportList = list
                } label: {
                    Image(systemName: "square.and.arrow.up")
                }
                .buttonStyle(.borderless)
                .accessibilityLabel(loc("Liste exportieren", "Export list"))
            }
        }
        .swipeActions(edge: .leading) {
            Button {
                selectList("custom:\(list.id.uuidString)")
            } label: {
                Label(loc("Auswählen", "Select"), systemImage: "checkmark")
            }
            .tint(Theme.accent)
        }
    }

    private func selectList(_ key: String) {
        var p = store.current
        p.settings.selectedList = key
        store.current = p
    }

    private func handleImport(_ result: Result<URL, Error>) {
        switch result {
        case .failure(let err):
            importError = err.localizedDescription
        case .success(let url):
            let secured = url.startAccessingSecurityScopedResource()
            defer { if secured { url.stopAccessingSecurityScopedResource() } }
            guard let data = try? Data(contentsOf: url),
                  let text = String(data: data, encoding: .utf8)
                    ?? String(data: data, encoding: .isoLatin1) else {
                importError = loc("Datei konnte nicht gelesen werden.", "Could not read the file.")
                return
            }
            let entries = CSV.parse(text)
            guard !entries.isEmpty else {
                importError = loc("Keine Wörter in der Datei gefunden.", "No words found in the file.")
                return
            }
            var list = CustomList(name: url.deletingPathExtension().lastPathComponent)
            list.entries = entries
            store.customLists.append(list)
            store.save()
        }
    }
}

/// Editor für eigene Listen: Wörter, Sprache, Reihenfolge, Umbenennen.
struct CustomListEditor: View {
    @EnvironmentObject var store: AppStore
    let listID: UUID
    @State private var newWord = ""

    private var index: Int? { store.customLists.firstIndex { $0.id == listID } }

    var body: some View {
        if let i = index {
            List {
                Section(loc("Einstellungen", "Settings")) {
                    TextField(loc("Name", "Name"), text: Binding(
                        get: { store.customLists[i].name },
                        set: { store.customLists[i].name = $0; store.save() }))
                    Picker(loc("Sprache", "Language"), selection: Binding(
                        get: { store.customLists[i].language },
                        set: { store.customLists[i].language = $0; store.save() })) {
                        Text("Deutsch").tag("de")
                        Text("English").tag("en")
                    }
                    Toggle(loc("Feste Reihenfolge", "Fixed order"), isOn: Binding(
                        get: { store.customLists[i].ordered },
                        set: { store.customLists[i].ordered = $0; store.save() }))
                }
                Section(loc("Wörter", "Words")) {
                    ForEach(store.customLists[i].entries) { e in
                        Text(e.syl)
                    }
                    .onDelete { idx in
                        store.customLists[i].entries.remove(atOffsets: idx)
                        store.save()
                    }
                    .onMove { from, to in
                        store.customLists[i].entries.move(fromOffsets: from, toOffset: to)
                        store.save()
                    }
                    HStack {
                        TextField(loc("Neues Wort (mit Silben: Fens-ter)", "New word (syllables: lit-tle)"),
                                  text: $newWord)
                            .autocorrectionDisabled(true)
                            .onSubmit(addWord)
                        Button(action: addWord) {
                            Image(systemName: "plus.circle.fill")
                        }
                        .disabled(newWord.trimmingCharacters(in: .whitespaces).isEmpty)
                    }
                }
            }
            .navigationTitle(store.customLists[i].name)
            .toolbar { EditButton() }
        }
    }

    private func addWord() {
        guard let i = index else { return }
        let raw = newWord.trimmingCharacters(in: .whitespaces)
        guard !raw.isEmpty else { return }
        let word = raw.replacingOccurrences(of: "-", with: "")
        if !store.customLists[i].entries.contains(where: { $0.word.lowercased() == word.lowercased() }) {
            let first = word.first.map(String.init) ?? ""
            let type = first == first.uppercased() && first != first.lowercased() ? "n" : "o"
            store.customLists[i].entries.append(WordEntry(syl: raw, type: type))
            store.save()
        }
        newWord = ""
    }
}

struct CSVDocument: FileDocument {
    static var readableContentTypes: [UTType] { [.commaSeparatedText, .plainText] }
    var text: String

    init(text: String) { self.text = text }

    init(configuration: ReadConfiguration) throws {
        text = String(data: configuration.file.regularFileContents ?? Data(), encoding: .utf8) ?? ""
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        FileWrapper(regularFileWithContents: text.data(using: .utf8) ?? Data())
    }
}
