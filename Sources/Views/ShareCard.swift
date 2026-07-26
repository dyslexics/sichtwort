import SwiftUI

/// Ergebnis-Karte im Stil des Runden-Abschlusses.
/// Wird nicht direkt angezeigt, sondern per ImageRenderer zu einem Bild
/// gerendert und über das Share-Sheet geteilt (AirDrop, WhatsApp, Mail, …).
struct ShareCard: View {
    let profileName: String
    let listName: String
    let correct: Int
    let total: Int
    let flashTime: Double
    let background: String

    private var darkBG: Bool { Theme.isDarkBackground(background) }
    private var textColor: Color { darkBG ? .white : Theme.accent }

    var body: some View {
        VStack(spacing: 16) {
            MascotImage(pose: correct == total ? "tanzend" : "jubelnd", height: 140)

            Text(loc("Super Leistung!", "Great job!"))
                .font(.system(size: 34, weight: .bold, design: .rounded))
                .foregroundColor(textColor)

            Text(profileName)
                .font(.title2.weight(.semibold))
                .foregroundColor(textColor.opacity(0.8))

            HStack(spacing: 28) {
                VStack(spacing: 2) {
                    Text("\(correct)/\(total)")
                        .font(.system(size: 40, weight: .bold, design: .rounded))
                        .foregroundColor(Theme.correct)
                    Text(loc("richtig", "correct"))
                        .font(.subheadline.weight(.semibold))
                        .foregroundColor(.gray)
                }
                VStack(spacing: 2) {
                    Text(flashTimeLabel(flashTime))
                        .font(.system(size: 40, weight: .bold, design: .rounded))
                        .foregroundColor(Theme.accent)
                    Text(loc("Aufblitzzeit", "Flash time"))
                        .font(.subheadline.weight(.semibold))
                        .foregroundColor(.gray)
                }
            }
            .padding(.vertical, 18)
            .padding(.horizontal, 30)
            .background(RoundedRectangle(cornerRadius: 20).fill(.white))

            LazyVGrid(columns: [GridItem(.adaptive(minimum: 20), spacing: 6)], spacing: 6) {
                ForEach(0..<total, id: \.self) { i in
                    RoundedRectangle(cornerRadius: 4)
                        .fill(i < correct ? Theme.correct : Theme.wrong)
                        .frame(height: 20)
                }
            }
            .frame(maxWidth: 280)

            Text(listName)
                .font(.headline)
                .foregroundColor(textColor.opacity(0.75))

            Text("Sichtwort · sichtwort.com")
                .font(.footnote.weight(.bold))
                .foregroundColor(textColor.opacity(0.6))
                .padding(.top, 6)
        }
        .padding(28)
        .frame(width: 420)
        .background(Theme.background(background))
    }
}

@MainActor
func renderShareCard(profileName: String, listName: String, correct: Int,
                     total: Int, flashTime: Double, background: String) -> UIImage? {
    let card = ShareCard(profileName: profileName, listName: listName,
                         correct: correct, total: total,
                         flashTime: flashTime, background: background)
    let renderer = ImageRenderer(content: card)
    renderer.scale = 3
    return renderer.uiImage
}
