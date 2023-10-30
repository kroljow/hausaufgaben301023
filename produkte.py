# Erstelle eine Liste, die nur die Namen der Produkte enthält, die derzeit verfügbar sind.
# Erstelle eine Liste, die die Namen der Produkte enthält, die einen Preis von weniger als 50 Euro haben und eine Bewertung von mindestens 4 von 5 Sternen haben.
# Berechne den Durchschnittspreis aller Produkte in der Liste.
# Finde das teuerste Produkt in der Liste.



#Produkte 
produkte = [
    ("Laptop", 899.99, 4.6, True),
    ("Smartphone", 549.99, 4.2, True),
    ("Tablet", 299.99, 3.9, False),
    ("Kopfhörer", 149.99, 4.8, True),
    ("Maus", 19.99, 4.1, True),
]

# Aufgabe 1 - Liste verfügbare Produkte
verfuegbare_produkte = [produkt[0] for produkt in produkte if produkt[3]]
print("Verfügbare Produkte:", verfuegbare_produkte)

# Aufgabe 2 - weniger als 50 €uro und 4 von 5 Sternen
gesuchte_produkte = [produkt[0] for produkt in produkte if produkt[1] < 50 and produkt[2] >= 4]
print("Gesuchte Produkte:", gesuchte_produkte)

# Aufgabe 3 - Durchschnittspreis aller Produkte
durchschnittspreis = sum(produkt[1] for produkt in produkte) / len(produkte)
print("Durchschnittspreis aller Produkte:", durchschnittspreis)

# Aufgabe 4 - teuerstes Produkt
teuerstes_produkt = max(produkte, key=lambda x: x[1])
print("Teuerstes Produkt:", teuerstes_produkt[0])
