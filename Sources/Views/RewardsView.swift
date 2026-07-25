import SwiftUI

/// Belohnungen: Posen freischalten, Begleiter wählen, endloses Level-System
/// (Original-Kritik: „Belohnungspool läuft leer").
struct RewardsView: View {
    @EnvironmentObject var store: AppStore

    private var profile: ChildProfile { store.current }
    private var unlocked: [String] { Mascot.unlocked(stars: profile.stars) }

    private let columns = [GridItem(.adaptive(minimum: 140), spacing: 16)]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 20) {
                    levelHeader
                    LazyVGrid(columns: columns, spacing: 16) {
                        ForEach(Mascot.poses, id: \.name) { pose in
                            poseCard(pose)
                        }
                    }
                    .padding(.horizontal)
                }
                .padding(.vertical)
            }
            .navigationTitle(loc("Belohnungen", "Rewards"))
        }
    }

    private var levelHeader: some View {
        VStack(spacing: 8) {
            HStack(spacing: 6) {
                Image(systemName: "star.fill").foregroundColor(.orange)
                Text("\(profile.stars)")
                    .font(.system(size: 40, weight: .heavy, design: .rounded))
                Text(loc("Sterne", "stars"))
                    .font(.title3)
                    .foregroundColor(.secondary)
            }
            Text(loc("Level \(profile.level)", "Level \(profile.level)"))
                .font(.headline)
                .padding(.horizontal, 14)
                .padding(.vertical, 6)
                .background(Capsule().fill(Theme.accent.opacity(0.15)))
                .foregroundColor(Theme.accent)
            ProgressView(value: Double(profile.starsIntoLevel), total: 100)
                .frame(maxWidth: 300)
            Text(loc("Noch \(100 - profile.starsIntoLevel) Sterne bis Level \(profile.level + 1)",
                     "\(100 - profile.starsIntoLevel) stars to level \(profile.level + 1)"))
                .font(.caption)
                .foregroundColor(.secondary)
        }
    }

    private func poseCard(_ pose: (name: String, stars: Int, de: String, en: String)) -> some View {
        let isUnlocked = unlocked.contains(pose.name)
        let isCompanion = profile.companionPose == pose.name
        return VStack(spacing: 8) {
            ZStack {
                RoundedRectangle(cornerRadius: 18)
                    .fill(isUnlocked ? Theme.accent.opacity(0.08) : Color.gray.opacity(0.12))
                VStack(spacing: 6) {
                    MascotImage(pose: pose.name, height: 90)
                        .saturation(isUnlocked ? 1 : 0)
                        .opacity(isUnlocked ? 1 : 0.35)
                    Text(loc(pose.de, pose.en))
                        .font(.subheadline.weight(.medium))
                    if isUnlocked {
                        if isCompanion {
                            Label(loc("Begleiter", "Companion"), systemImage: "checkmark.circle.fill")
                                .font(.caption)
                                .foregroundColor(Theme.accent)
                        }
                    } else {
                        Label("\(pose.stars)", systemImage: "star.fill")
                            .font(.caption)
                            .foregroundColor(.orange)
                    }
                }
                .padding(10)
            }
        }
        .onTapGesture {
            if isUnlocked {
                var p = store.current
                p.companionPose = pose.name
                store.current = p
            }
        }
        .accessibilityLabel(isUnlocked
            ? loc("\(pose.de), freigeschaltet", "\(pose.en), unlocked")
            : loc("\(pose.de), ab \(pose.stars) Sternen", "\(pose.en), unlocks at \(pose.stars) stars"))
    }
}
