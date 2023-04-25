# Entwurfsmuster - Aufgabe 1

Multi-select: Bedarfsorientierte Mikroprojekte, Notiz
Zuletzt bearbeitet: 25. April 2023 15:00
https://git.ide3.de/gst/bcsm206_entwurfsmuster-und-algorithmen/lehrveranstaltung: Vorlesingsunterlagen
https://git.ide3.de/gst/bcsm206_entwurfsmuster-und-algorithmen/projektarbeit/aufgabe1: Aufgabe 1

# Aufgabenteil 1 - Entwurfsmuster

## Aufgabe 1.1 - Decorator-Pattern

Beispiel:

Eine Kaffeehaus-Kette, nennen wir sie Sternback-Kaffee, verkauft in vielen Filialen unterschiedliche Kaffeearten wie Hausmischung, dunkel geröstet, entkoffeiniert oder Espresso sowie verschiedene Zutaten wie heiße Milch, Soja, Schokolade oder Milchschaum. Je nach Kaffeeart und Zutaten ist für das Getränk ein Preis zu berechnen.
Zur Modellierung verwenden wir das Decorator-Pattern. Wir beginnen also mit einem Getränk und dekorieren es zur Laufzeit mit Zutaten. Wenn der Kunde eine dunkle Röstung mit Schoko und Milchschaum möchte, geht das beispielsweise so:

1. Wir nehmen ein DunkleRöstung-Objekt,
2. dekorieren es mit einem Schoko-Objekt,
3. dekorieren es mit einem Milchschaum-Objekt,
4. rufen die Methode preis() auf und stützen uns auf Delegierung, um den Preis für die Zutaten hinzuzufügen.

### Aufgabe 1.1.1

Erklären Sie das Dekorierer-Muster am o.g. Beispiel.

> Das Decorator-Pattern ermöglicht es, die Funktionalität eines Objekts zur Laufzeit zu erweitern, indem zusätzliche Verantwortlichkeiten durch Dekoration hinzugefügt werden. Im Beispiel der Kaffeehaus-Kette wird ein Getränk-Objekt mit zusätzlichen Zutaten dekoriert, um den Preis und Geschmack des Kaffees zu verändern. Jedes dekorierte Objekt wird durch den Aufruf der preis()-Methode erweitert, indem der Preis der Zutaten auf den Preis des ursprünglichen Getränks addiert wird.
> 

### Aufgabe 1.1.2

Setzen Sie das oben genannte Beispiel in einen lauffähigen Code (Python, C, C++ oder Ähnliches) um oder beschreiben Sie die Umsetzung in einer algorithmischen Form. Wie sieht das UML-Klassendiagramm aus?

```python
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
```

## Aufgabe 1.2 - Zustandsmuster

Gegeben sei ein Getränkeautomat, der die Auswahl zwischen 3 Getränken bietet: Kaffee, Suppe und Limonade. Die Getränke haben unterschiedliche Preise, evtl. ist eine Getränkeart nicht mehr verfügbar. Der Automat akzeptiert Münzen im Wert von 5c, 10c, 20c, 50c, 100 c und 200c sowie Geldscheine im Wert von 500c, 1000c und 2000c, Rückgeld wird erstattet. Beim Rückgeld können Sie davon ausgehen, dass immer genügend Münzen vorhanden sind.

Implementieren Sie ein interaktives Programm, mit dem der Kauf eines Getränks simuliert werden kann. Der Getränkeautomat soll mittels des Zustandsmusters implementiert werden. Die Benutzeroberfläche kann wie folgt aussehen:

```
Zustand: BEREIT

(1)  Kaffee:  60c
(2)  Suppe:  78c
(3)  Limonade: 45c
---------------- Ihre Auswahl?
```

Nach der Auswahl eines Getränks wird der zu zahlende Betrag angezeigt:

```
Zustand:  GELDEINWURF
noch zu zahlen: 37c
------------------Ihre Eingabe?
```

Auf jeder Ebene soll ein Abbruch möglich sein.

### Aufgabe 1.2.1

Erklären Sie das Zustandsmuster am o.g. Beispiel.

### Aufgabe 1.2.2

Setzen Sie das oben benannte Beispiel in einen lauffähigen Code (Python, C, C++ oder Ähnliches) um oder beschreiben Sie die Umsetzung in einer algorithmischen Form. Erstellen Sie zu Ihrer Implementierung ein UML-Klassendiagramm sowie eine geeignete Darstellung (z.B. Sequenzdiagramm), aus der der Ablauf beim Zustandswechsel hervorgeht.

## Aufgabe 1.3 - Singelton

### Aufgabe 1.3.1

Beschreiben Sie das Entwurfsmuster Singelton an einen von Ihnen zu entwickelnden Beispiel.

### Aufgabe 1.3.2

Setzen Sie Ihr Beispiel in einen lauffähigen Code (Python, C, C++ oder Ähnliches) um oder beschreiben Sie die Umsetzung in einer algorithmischen Form.