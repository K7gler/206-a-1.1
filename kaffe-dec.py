class Getraenk:
    def __init__(self):
        self._preis = 0.0
        self._beschreibung = "Unbekanntes Getränk"

    def preis(self):
        return self._preis

    def beschreibung(self):
        return self._beschreibung


class Kaffee(Getraenk):
    def __init__(self):
        super().__init__()
        self._preis = 1.5
        self._beschreibung = "Kaffee"
        
    def __str__(self):
        return self._beschreibung



class KaffeeDecorator(Getraenk):
    def __init__(self, getraenk):
        super().__init__()
        self._getraenk = getraenk

    def preis(self):
        return self._getraenk.preis() + super().preis()

    def beschreibung(self):
        return self._getraenk.beschreibung() + f", {super().beschreibung()}"

class DunkleRöstung(Kaffee):
    def __init__(self):
        super().__init__()
        self._preis = 2.0
        self._beschreibung = "Dunkle Röstung"
        
    def __str__(self):
        return self._beschreibung



class Entkoffeiniert(Kaffee):
    def __init__(self):
        super().__init__()
        self._preis = 2.5
        self._beschreibung = "Entkoffeiniert"
        
    def __str__(self):
        return self._beschreibung


class Espresso(Kaffee):
    def __init__(self):
        super().__init__()
        self._preis = 3.0
        self._beschreibung = "Espresso"
        
    def __str__(self):
        return self._beschreibung


class ZutatDecorator(Getraenk):
    def __init__(self, getraenk):
        super().__init__()
        self._getraenk = getraenk


class Schoko(ZutatDecorator):
    def __init__(self, getraenk):
        super().__init__(getraenk)
        self._preis = 0.5
        self._beschreibung = "Schokolade"

    def preis(self):
        return self._getraenk.preis() + super().preis()

    def beschreibung(self):
        return self._getraenk.beschreibung() + ", " + super().beschreibung()


class Milchschaum(ZutatDecorator):
    def __init__(self, getraenk):
        super().__init__(getraenk)
        self._preis = 0.3
        self._beschreibung = "Milchschaum"

    def preis(self):
        return self._getraenk.preis() + super().preis()

    def beschreibung(self):
        return self._getraenk.beschreibung() + ", " + super().beschreibung()

# Eingabeaufforderungen
def frage_nach_auswahl(frage, auswahlmöglichkeiten):
    print(frage)
    for i, wahl in enumerate(auswahlmöglichkeiten):
        print(f"{i+1}. {str(wahl)}")
    while True:
        auswahl = input("Ihre Wahl: ")
        try:
            auswahl_index = int(auswahl) - 1
            if 0 <= auswahl_index < len(auswahlmöglichkeiten):
                return auswahl_index
        except ValueError:
            pass
        print("Ungültige Eingabe, bitte wählen Sie erneut.")
 




def frage_nach_zutat():
    zutaten = [Schoko, Milchschaum]
    print("Welche Zutat möchten Sie hinzufügen?")
    for i, zutat in enumerate(zutaten):
        if issubclass(zutat, ZutatDecorator): # Nur ZutatDecorators hinzufügen
            print(f"{i+1}. {zutat.__name__}")
    while True:
        auswahl = input("Ihre Wahl: ")
        try:
            auswahl_index = int(auswahl) - 1
            if 0 <= auswahl_index < len(zutaten) and issubclass(zutaten[auswahl_index], ZutatDecorator):
                return zutaten[auswahl_index]
        except ValueError:
            pass
        print("Ungültige Eingabe, bitte wählen Sie erneut.")


def main():
    print("Willkommen bei Sternback-Kaffee!")
    while True:
        kaffeearten = [Kaffee, DunkleRöstung, Entkoffeiniert, Espresso]
        kaffee_index = frage_nach_auswahl("Welchen Kaffee möchten Sie bestellen?", kaffeearten)
        getraenk = kaffeearten[kaffee_index]()

        while True:
            print(f"Sie haben ein {getraenk.beschreibung()} bestellt. Der Preis beträgt {getraenk.preis()} €.")
            zutat_auswahl = frage_nach_auswahl("Möchten Sie eine Zutat hinzufügen?", ["Ja", "Nein"])
            if zutat_auswahl == 0:
                zutat_typ = frage_nach_zutat()
                getraenk = zutat_typ(getraenk)
            else:
                break

        print(f"Vielen Dank für Ihre Bestellung! Sie haben ein {getraenk.beschreibung()} für {getraenk.preis()} € bestellt.")

        weitere_bestellung = input("Möchten Sie weitere Bestellungen aufgeben? (Ja/Nein) ")
        if weitere_bestellung.lower() not in ["ja", "j", "yes", "y"]:
            break

    print("Auf Wiedersehen bei Sternback-Kaffee!")

if __name__ == '__main__':
    main()