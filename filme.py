# leeres Wörterbuch für Filmbewertungen
film_bewertungen = {}

# fünf Filmtitel und ihre Bewertungen 
film_bewertungen = {
    "Fight Club": 8.5,
    "There will be blood": 8.9,
    "No country for old man": 8.7,
    "Stalker": 9,
    "Interstelar": 8.8
}

# Berechnung der durchschnittlichen Bewertung
def durchschnittliche_bewertung(wörterbuch):
    if not wörterbuch:
        return 0
    summe = sum(wörterbuch.values())
    anzahl = len(wörterbuch)
    durchschnitt = summe / anzahl
    return durchschnitt

# Ermittlung des Films mit der höchsten Bewertung
def höchste_bewertung(wörterbuch):
    if not wörterbuch:
        return None
    bester_film = max(wörterbuch, key=wörterbuch.get)
    return bester_film

# Ermittlung der Filme mit einer Bewertung von 6 oder höher
def filme_ab_6(wörterbuch):
    return [film for film, bewertung in wörterbuch.items() if bewertung >= 6]

# ein weiterer Film
film_bewertungen["Titanic"] = 3

#  aktualisierte Wörterbuch ausgeben
print("Aktualisiertes Wörterbuch für Filmbewertungen:")
print(film_bewertungen)


durchschnitt = durchschnittliche_bewertung(film_bewertungen)
bester_film = höchste_bewertung(film_bewertungen)
filme_ab_6_liste = filme_ab_6(film_bewertungen)

print("Durchschnittliche Bewertung aller Filme:", durchschnitt)
print("Film mit der höchsten Bewertung:", bester_film)
print("Filme mit einer Bewertung von 6 oder höher:", filme_ab_6_liste)
