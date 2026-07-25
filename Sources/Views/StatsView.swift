import SwiftUI
import Charts

/// Lernstatistik pro Profil — fehlt im Original komplett.
struct StatsView: View {
    @EnvironmentObject var store: AppStore

    private var profile: ChildProfile { store.current }
    private var recent: [RoundRecord] { Array(profile.roundHistory.suffix(30)) }

    var body: some View {
        NavigationStack {
            List {
                Section {
                    HStack(spacing: 16) {
                        MascotImage(pose: "hanteln", height: 90)
                        VStack(alignment: .leading, spacing: 6) {
                            statLine(loc("Runden", "Rounds"), "\(profile.roundHistory.count)")
                            statLine(loc("Geübte Wörter", "Words practiced"), "\(profile.totalWords)")
                            statLine(loc("Richtig", "Correct"),
                                     profile.totalWords > 0
                                     ? "\(profile.totalCorrect) (\(profile.totalCorrect * 100 / max(profile.totalWords, 1)) %)"
                                     : "—")
                            statLine(loc("Sterne", "Stars"), "\(profile.stars)")
                        }
                        Spacer()
                    }
                    .padding(.vertical, 4)
                } header: {
                    Text(profile.name)
                }

                if recent.count >= 2 {
                    Section(loc("Verlauf (letzte Runden)", "Progress (recent rounds)")) {
                        Chart(recent) { r in
                            LineMark(
                                x: .value(loc("Datum", "Date"), r.date),
                                y: .value(loc("Richtig %", "Correct %"),
                                          Double(r.correct) / Double(max(r.total, 1)) * 100))
                                .foregroundStyle(Theme.accent)
                            PointMark(
                                x: .value(loc("Datum", "Date"), r.date),
                                y: .value(loc("Richtig %", "Correct %"),
                                          Double(r.correct) / Double(max(r.total, 1)) * 100))
                                .foregroundStyle(Theme.accent)
                        }
                        .chartYScale(domain: 0...100)
                        .frame(height: 180)
                        .padding(.vertical, 6)

                        Chart(recent) { r in
                            LineMark(
                                x: .value(loc("Datum", "Date"), r.date),
                                y: .value(loc("Aufblitzzeit s", "Flash time s"), r.flashTime))
                                .foregroundStyle(.orange)
                        }
                        .frame(height: 120)
                        .padding(.vertical, 6)
                    }
                }

                Section {
                    if profile.errorBox.isEmpty {
                        Text(loc("Gerade keine — super!", "None right now — great!"))
                            .foregroundColor(.secondary)
                    } else {
                        ForEach(profile.errorBox.sorted(by: { $0.key < $1.key }), id: \.key) { word, weight in
                            HStack {
                                Text(word)
                                Spacer()
                                Text(loc("noch \(weight)× richtig lesen", "read correctly \(weight) more times"))
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }
                } header: {
                    Text(loc("Übungswörter (werden automatisch wiederholt)", "Practice words (repeated automatically)"))
                }

                if !profile.roundHistory.isEmpty {
                    Section(loc("Letzte Runden", "Recent rounds")) {
                        ForEach(recent.reversed()) { r in
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(r.listName).font(.subheadline)
                                    Text(r.date, style: .date)
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                }
                                Spacer()
                                Text("\(r.correct)/\(r.total)")
                                    .font(.headline)
                                    .foregroundColor(r.correct == r.total ? Theme.correct : .primary)
                            }
                        }
                    }
                }
            }
            .navigationTitle(loc("Statistik", "Statistics"))
        }
    }

    private func statLine(_ label: String, _ value: String) -> some View {
        HStack {
            Text(label).foregroundColor(.secondary)
            Spacer()
            Text(value).bold().monospacedDigit()
        }
        .font(.subheadline)
    }
}
