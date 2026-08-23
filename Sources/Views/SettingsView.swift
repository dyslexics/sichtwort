import SwiftUI

/// Alle Einstellungen gelten pro Kind-Profil.
struct SettingsView: View {
    @EnvironmentObject var store: AppStore
    @State private var newProfileName = ""
    @State private var showNewProfile = false

    var body: some View {
        NavigationStack {
            List {
                profileSection
                timingSection
                displaySection
                filterSection
                extrasSection
                aboutSection
            }
            .navigationTitle(loc("Einstellungen", "Settings"))
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    MascotImage(pose: "tafel", height: 36)
                }
            }
            .alert(loc("Neues Profil", "New profile"), isPresented: $showNewProfile) {
                TextField(loc("Name des Kindes", "Child's name"), text: $newProfileName)
                Button(loc("Anlegen", "Create")) {
                    let name = newProfileName.trimmingCharacters(in: .whitespaces)
                    if !name.isEmpty {
                        let p = ChildProfile(name: name)
                        store.profiles.append(p)
                        store.currentProfileID = p.id
                        store.save()
                    }
                    newProfileName = ""
                }
                Button(loc("Abbrechen", "Cancel"), role: .cancel) { newProfileName = "" }
            }
        }
    }

    private var settingsBinding: Binding<ProfileSettings> {
        Binding(get: { store.current.settings },
                set: { var p = store.current; p.settings = $0; store.current = p })
    }

    // MARK: - Profile (Mehrkind — fehlt im Original)

    private var profileSection: some View {
        Section {
            Picker(loc("Aktives Kind", "Active child"), selection: Binding(
                get: { store.currentProfileID ?? UUID() },
                set: { store.currentProfileID = $0; store.save() })) {
                ForEach(store.profiles) { p in
                    Text(p.name).tag(p.id)
                }
            }
            TextField(loc("Name", "Name"), text: Binding(
                get: { store.current.name },
                set: { var p = store.current; p.name = $0; store.current = p }))
            Button {
                showNewProfile = true
            } label: {
                Label(loc("Kind hinzufügen", "Add child"), systemImage: "person.badge.plus")
            }
            if store.profiles.count > 1 {
                Button(role: .destructive) {
                    let id = store.current.id
                    store.profiles.removeAll { $0.id == id }
                    store.currentProfileID = store.profiles.first?.id
                    store.save()
                } label: {
                    Label(loc("Dieses Profil löschen", "Delete this profile"), systemImage: "trash")
                }
            }
        } header: {
            Text(loc("Profile", "Profiles"))
        } footer: {
            Text(loc("Jedes Kind hat eigene Sterne, Einstellungen und Fehlerwörter. Alles bleibt auf diesem Gerät.",
                     "Each child has their own stars, settings and practice words. Everything stays on this device."))
        }
    }

    // MARK: - Zeit & Runde

    private var timingSection: some View {
        Section(loc("Aufblitzen", "Flash")) {
            VStack(alignment: .leading) {
                HStack {
                    Text(loc("Aufblitzzeit", "Flash time"))
                    Spacer()
                    Text(flashTimeLabel(settingsBinding.wrappedValue.flashTime))
                        .foregroundColor(.secondary)
                        .monospacedDigit()
                }
                // Log-Skala: unten fein (Hundertstel), oben bis 5 s (Original: max 2 s)
                Slider(value: Binding(
                    get: { log10(settingsBinding.wrappedValue.flashTime) },
                    set: { settingsBinding.wrappedValue.flashTime = (pow(10, $0) * 100).rounded() / 100 }),
                    in: log10(0.02)...log10(5.0))
                    .accessibilityLabel(loc("Aufblitzzeit", "Flash time"))
            }
            Stepper(loc("Wörter pro Runde: \(settingsBinding.wrappedValue.roundSize)",
                        "Words per round: \(settingsBinding.wrappedValue.roundSize)"),
                    value: settingsBinding.roundSize, in: 5...40, step: 5)
            Toggle(isOn: settingsBinding.adaptive) {
                VStack(alignment: .leading, spacing: 2) {
                    Text(loc("Abenteuer-Modus", "Adventure mode"))
                    Text(loc("Wird bei Erfolg automatisch schneller, bei Fehlern langsamer.",
                             "Speeds up automatically on success, slows down after mistakes."))
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
        }
    }

    // MARK: - Darstellung

    private var displaySection: some View {
        Section(loc("Darstellung", "Display")) {
            Picker(loc("Schriftart", "Font"), selection: settingsBinding.fontChoice) {
                Text(loc("Standard", "Standard")).tag("system")
                Text("OpenDyslexic").tag("dyslexic")
                Text("Lexend").tag("lexend")
            }
            VStack(alignment: .leading) {
                HStack {
                    Text(loc("Schriftgröße", "Font size"))
                    Spacer()
                    Text("\(Int(settingsBinding.wrappedValue.fontSize)) pt")
                        .foregroundColor(.secondary)
                }
                Slider(value: settingsBinding.fontSize, in: 36...120, step: 2)
                    .accessibilityLabel(loc("Schriftgröße", "Font size"))
            }
            Text(loc("Beispiel", "Sample") + ": Fenster")
                .font(Theme.wordFont(choice: settingsBinding.wrappedValue.fontChoice,
                                     size: min(settingsBinding.wrappedValue.fontSize, 44)))
                .frame(maxWidth: .infinity, alignment: .center)
            Picker(loc("Silben zeigen", "Show syllables"), selection: settingsBinding.syllableMode) {
                Text(loc("Aus", "Off")).tag("none")
                Text(loc("Farbig", "Colored")).tag("colored")
                Text(loc("Nacheinander", "One by one")).tag("sequential")
            }
            Picker(loc("Hintergrund", "Background"), selection: settingsBinding.background) {
                ForEach(Theme.backgrounds, id: \.id) { bg in
                    Text(loc(bg.de, bg.en)).tag(bg.id)
                }
            }
        }
    }

    // MARK: - Filter

    private var filterSection: some View {
        Section {
            Picker(loc("Silbenzahl", "Syllable count"), selection: settingsBinding.syllableFilter) {
                Text(loc("Alle", "All")).tag("all")
                Text(loc("1 Silbe", "1 syllable")).tag("1")
                Text(loc("2 Silben", "2 syllables")).tag("2")
                Text(loc("3+ Silben", "3+ syllables")).tag("3plus")
            }
            ForEach([("n", loc("Nomen", "Nouns")), ("v", loc("Verben", "Verbs")),
                     ("a", loc("Adjektive", "Adjectives")), ("o", loc("Sonstige", "Other"))], id: \.0) { item in
                let (type, label) = item
                Toggle(label, isOn: Binding(
                    get: {
                        let f = settingsBinding.wrappedValue.typeFilter
                        return f.isEmpty || f.contains(type)
                    },
                    set: { on in
                        var f = settingsBinding.wrappedValue.typeFilter
                        if f.isEmpty { f = ["n", "v", "a", "o"] }
                        if on { if !f.contains(type) { f.append(type) } }
                        else { f.removeAll { $0 == type } }
                        if f.count == 4 { f = [] }
                        settingsBinding.wrappedValue.typeFilter = f
                    }))
            }
        } header: {
            Text(loc("Wortauswahl", "Word selection"))
        } footer: {
            Text(loc("Filter gelten für den Grundwortschatz und Listen mit passenden Angaben.",
                     "Filters apply to the basic vocabulary and lists with matching data."))
        }
    }

    // MARK: - Extras

    private var extrasSection: some View {
        Section(loc("Sprache & Ton", "Language & sound")) {
            Toggle(loc("Vorsprechen (Sprachausgabe)", "Speak words aloud"), isOn: settingsBinding.tts)
            if store.current.settings.tts {
                Picker(loc("Deutsche Stimme", "German voice"), selection: settingsBinding.germanVoice) {
                    Text(loc("Seraphina (weiblich)", "Seraphina (female)")).tag("seraphina")
                    Text(loc("Conrad (männlich)", "Conrad (male)")).tag("conrad")
                }
                Picker(loc("Englische Stimme", "English voice"), selection: settingsBinding.englishAccent) {
                    Text(loc("Amerikanisch (Ava)", "American (Ava)")).tag("us")
                    Text(loc("Britisch (Sonia)", "British (Sonia)")).tag("gb")
                }
            }
            Toggle(loc("Schweizer Schreibweise (ss statt ß)", "Swiss spelling (ss instead of ß)"),
                   isOn: settingsBinding.swissSpelling)
        }
    }

    // MARK: - Über

    private var aboutSection: some View {
        Section {
            NavigationLink {
                HelpView()
            } label: {
                Label(loc("Anleitung & Tipps", "Guide & tips"), systemImage: "lightbulb.fill")
            }
            Link(destination: URL(string: "https://sichtwort.com")!) {
                Label("sichtwort.com", systemImage: "globe")
            }
            Link(destination: URL(string: "https://www.legasthenie.at")!) {
                Label(loc("EÖDL — legasthenie.at", "EÖDL — legasthenie.at"), systemImage: "link")
            }
            Link(destination: URL(string: "https://github.com/dyslexics/sichtwort")!) {
                Label(loc("Quellcode (Open Source, GPL-3.0)", "Source code (open source, GPL-3.0)"),
                      systemImage: "chevron.left.forwardslash.chevron.right")
            }
        } header: {
            Text(loc("Über Sichtwort", "About Sichtwort"))
        } footer: {
            Text(loc("Ein Projekt des EÖDL — Erster Österreichischer Dachverband Legasthenie. Gratis, werbefrei, ohne Datensammlung. Version 1.0. Schriften: OpenDyslexic, Lexend (SIL OFL).",
                     "A project by EÖDL — Austrian Dyslexia Association. Free, ad-free, no data collection. Version 1.0. Fonts: OpenDyslexic, Lexend (SIL OFL)."))
        }
    }
}

/// Anleitung mit fachlichem Hinweis (fehlt im Original).
struct HelpView: View {
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                HStack {
                    Spacer()
                    MascotImage(pose: "gluehbirne", height: 130)
                    Spacer()
                }
                helpBlock(
                    loc("So funktioniert Blitzlesen", "How flash reading works"),
                    loc("Ein Wort blitzt kurz auf. Das Kind erfasst es als Ganzes und spricht es aus. So werden häufige Wörter automatisiert — das entlastet beim Lesen von Texten.",
                        "A word flashes briefly. The child recognizes it as a whole and says it aloud. Frequent words become automatic — freeing up attention for reading comprehension."))
                helpBlock(
                    loc("Der richtige Einstieg", "Getting started right"),
                    loc("Mit 2 Sekunden oder mehr beginnen und erst verkürzen, wenn die Wörter sicher erkannt werden. Für Kinder, die noch Buchstabe für Buchstabe lesen, ist Blitzlesen noch nicht geeignet — erst wenn die Buchstabensynthese sicher ist.",
                        "Start at 2 seconds or more and only reduce the time once words are recognized reliably. For children still decoding letter by letter, flash reading is premature — wait until blending is secure."))
                helpBlock(
                    loc("Gemeinsam oder alleine", "Together or on their own"),
                    loc("Im Modus „Gemeinsam“ hört eine erwachsene Person zu und bewertet — ideal fürs Training. Im Modus „Alleine“ tippt das Kind das Wort und übt zusätzlich die Rechtschreibung.",
                        "In \"Together\" mode an adult listens and judges — ideal for training sessions. In \"On my own\" mode the child types the word, which also practices spelling."))
                helpBlock(
                    loc("Eigene Wortlisten", "Custom word lists"),
                    loc("Unter „Listen“ eigene Wörter anlegen oder als CSV importieren — zum Beispiel die Lernwörter der Woche oder Wörter mit einem bestimmten Rechtschreibphänomen. Mit Bindestrich lassen sich Silben markieren: Fens-ter.",
                        "Under \"Lists\" you can create your own words or import a CSV — for example this week's spelling words. Use hyphens to mark syllables: lit-tle."))
                helpBlock(
                    loc("Falsch gelesene Wörter", "Missed words"),
                    loc("Wörter, die nicht erkannt wurden, bringt Sichtwort in den nächsten Runden automatisch wieder — bis sie dreimal sicher gelesen wurden.",
                        "Words that weren't recognized come back automatically in the next rounds — until they have been read correctly three times."))
            }
            .padding()
        }
        .navigationTitle(loc("Anleitung", "Guide"))
    }

    private func helpBlock(_ title: String, _ text: String) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title).font(.headline).foregroundColor(Theme.accent)
            Text(text).font(.body)
        }
    }
}
