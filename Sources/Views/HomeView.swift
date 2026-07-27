import SwiftUI

/// Startbildschirm: Begleiter-Pose, Profilwahl, Schnelleinstellungen, Rundenstart.
struct HomeView: View {
    @EnvironmentObject var store: AppStore
    @State private var showGame = false
    @State private var showEasyReading = false

    private var settings: ProfileSettings { store.current.settings }
    private var darkBG: Bool { Theme.isDarkBackground(settings.background) }
    private var textColor: Color { darkBG ? .white : .primary }

    var body: some View {
        NavigationStack {
            ZStack {
                Theme.background(settings.background).ignoresSafeArea()
                ScrollView {
                    VStack(spacing: 20) {
                        profileSwitcher
                        MascotImage(pose: store.current.companionPose, height: 180)
                        Text("Sichtwort")
                            .font(.system(size: 44, weight: .heavy, design: .rounded))
                            .foregroundColor(darkBG ? .white : Theme.accent)
                        Text(loc("Wörter blitzschnell erkennen", "Recognize words in a flash"))
                            .font(.headline)
                            .foregroundColor(textColor.opacity(0.7))

                        quickInfo

                        Button {
                            showGame = true
                        } label: {
                            Label(loc("Runde starten", "Start round"), systemImage: "bolt.fill")
                                .font(.title2.bold())
                                .frame(maxWidth: 420)
                                .padding(.vertical, 14)
                        }
                        .buttonStyle(.borderedProminent)
                        .padding(.top, 4)

                        Button {
                            showEasyReading = true
                        } label: {
                            Label("Easy Reading", systemImage: "book.fill")
                                .font(.title3.bold())
                                .frame(maxWidth: 420)
                                .padding(.vertical, 12)
                        }
                        .buttonStyle(.bordered)
                        .tint(darkBG ? .white : Theme.accent)

                        modeToggle
                    }
                    .padding()
                }
            }
            .fullScreenCover(isPresented: $showGame) {
                GameView()
            }
            .fullScreenCover(isPresented: $showEasyReading) {
                EasyReadingView()
            }
        }
    }

    private var profileSwitcher: some View {
        HStack {
            Menu {
                ForEach(store.profiles) { p in
                    Button {
                        store.currentProfileID = p.id
                        store.save()
                    } label: {
                        if p.id == store.currentProfileID {
                            Label(p.name, systemImage: "checkmark")
                        } else {
                            Text(p.name)
                        }
                    }
                }
            } label: {
                Label(store.current.name, systemImage: "person.circle.fill")
                    .font(.headline)
                    .padding(.horizontal, 14)
                    .padding(.vertical, 8)
                    .background(Capsule().fill(Color(UIColor.systemBackground).opacity(0.85)))
            }
            Spacer()
            HStack(spacing: 4) {
                Image(systemName: "star.fill").foregroundColor(.orange)
                Text("\(store.current.stars)")
                    .font(.headline)
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 8)
            .background(Capsule().fill(Color(UIColor.systemBackground).opacity(0.85)))
            .accessibilityLabel(loc("\(store.current.stars) Sterne", "\(store.current.stars) stars"))
        }
    }

    private var quickInfo: some View {
        VStack(spacing: 6) {
            HStack {
                Image(systemName: "list.bullet")
                Text(store.listName(forKey: settings.selectedList))
                Spacer()
                Image(systemName: "timer")
                Text(flashTimeLabel(settings.flashTime))
            }
            .font(.subheadline.weight(.medium))
            .foregroundColor(textColor.opacity(0.85))
        }
        .padding(.horizontal, 18)
        .padding(.vertical, 12)
        .background(RoundedRectangle(cornerRadius: 14).fill(Color(UIColor.systemBackground).opacity(0.7)))
        .frame(maxWidth: 420)
    }

    private var modeToggle: some View {
        Picker("", selection: Binding(
            get: { settings.teacherMode },
            set: { v in
                var p = store.current
                p.settings.teacherMode = v
                store.current = p
            })) {
            Text(loc("Alleine", "On my own")).tag(false)
            Text(loc("Gemeinsam", "Together")).tag(true)
        }
        .pickerStyle(.segmented)
        .frame(maxWidth: 420)
    }
}

func flashTimeLabel(_ t: Double) -> String {
    if t < 0.1 {
        return String(format: "%.0f/100 s", t * 100)
    }
    return String(format: "%.2f s", t).replacingOccurrences(of: ".", with: ",")
}
