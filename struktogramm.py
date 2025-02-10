import turtle


def draw_tax_logic_structogram():
    screen = turtle.Screen()
    screen.title("Steuerberechnungslogik")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Start position
    t.goto(-200, 150)
    width = 400

    # Main header
    t.pendown()
    t.forward(width)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(30)
    t.penup()
    t.goto(-190, 135)
    t.write("Steuerberechnung für Einkommen", font=("Arial", 10, "bold"))

    # Draw decision structure
    y_pos = 120
    decisions = [
        ("Einkommen > 48000€", "Steuer = 36% auf Betrag über 48000€"),
        ("Einkommen > 24000€", "Steuer = 24% auf Betrag zwischen 24000€ und 48000€"),
        ("Einkommen > 8000€", "Steuer = 12% auf Betrag zwischen 8000€ und 24000€"),
        ("Einkommen ≤ 8000€", "Steuer = 0%")
    ]

    for decision, action in decisions:
        # Decision box
        t.goto(-200, y_pos)
        t.pendown()
        t.setheading(0)
        t.forward(width)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(40)

        # Write text
        t.penup()
        t.goto(-190, y_pos - 15)
        t.write(decision, font=("Arial", 9, "normal"))
        t.goto(-190, y_pos - 35)
        t.write(action, font=("Arial", 9, "normal"))

        y_pos -= 40

    screen.exitonclick()


if __name__ == "__main__":
    draw_tax_logic_structogram()