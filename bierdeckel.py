def steuer_berechnen(einkommen):
    # Initialisierung der Variablen
    gesamtsteuer = 0
    verbleibendes_einkommen = einkommen
    steuer_pro_stufe = []

    # Definition der Steuerstufen und Steuersätze
    steuerstufen = [
        (48000, 0.36, "über 48.000€"),
        (24000, 0.24, "24.000€ bis 48.000€"),
        (8000, 0.12, "8.000€ bis 24.000€"),
        (0, 0, "0€ bis 8.000€")
    ]

    # Steuerberechnung für jede Stufe
    for schwelle, satz, bezeichnung in steuerstufen:
        if verbleibendes_einkommen > schwelle:
            steuerpflichtiger_betrag = verbleibendes_einkommen - schwelle
            steuer = steuerpflichtiger_betrag * satz
            gesamtsteuer += steuer
            steuer_pro_stufe.append((bezeichnung, satz, steuer, steuerpflichtiger_betrag))
            verbleibendes_einkommen = schwelle

    # Berechnung des effektiven Steuersatzes
    effektiver_steuersatz = (gesamtsteuer / einkommen * 100)

    return gesamtsteuer, effektiver_steuersatz, steuer_pro_stufe


def main():
    try:
        einkommen = float(input("Geben Sie das Jahreseinkommen in Euro ein: "))
        if einkommen < 0:
            print("Einkommen kann nicht negativ sein!")
            return

        steuer, effektiver_satz, steuer_pro_stufe = steuer_berechnen(einkommen)

        print(f"\nSteuerbericht:")
        print(f"Jahreseinkommen: {einkommen:,.2f}€")
        print(f"\nAufschlüsselung nach Steuerstufen:")
        print("-" * 60)

        for bezeichnung, satz, stufen_steuer, steuerpflichtiger_betrag in steuer_pro_stufe:
            print(f"Mit {int(satz*100)}% zu versteuern:    {steuerpflichtiger_betrag:,.2f}€")
        print("-" * 60)

        print(f"\nZusammenfassung:")
        print(f"Gesamtsteuer: {steuer:,.2f}€")
        print(f"Effektiver Steuersatz: {effektiver_satz:.2f}%")
        print(f"Nettoeinkommen: {einkommen - steuer:,.2f}€")

    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")


if __name__ == "__main__":
    main()