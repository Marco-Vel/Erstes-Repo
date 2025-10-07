import random; import time

wortliste = [
    "apfel", "banane", "birne", "kirsche", "pfirsich", "melone", "ananas", "erdbeere", "himbeere", "brombeere",
    "hund", "katze", "maus", "pferd", "schwein", "kuh", "huhn", "ente", "gans", "schaf",
    "tisch", "stuhl", "bett", "sofa", "schrank", "lampe", "teppich", "uhr", "fenster", "tür",
    "haus", "garten", "garage", "keller", "dach", "wand", "boden", "zimmer", "bad", "küche",
    "auto", "bus", "bahn", "flugzeug", "fahrrad", "motorrad", "boot", "schiff", "zug", "taxi",
    "schule", "lehrer", "schüler", "tafel", "heft", "buch", "bleistift", "radiergummi", "lineal", "rucksack",
    "computer", "tastatur", "mauspad", "bildschirm", "drucker", "internet", "email", "website", "programm", "datei",
    "baum", "blume", "gras", "strauch", "wald", "see", "fluss", "berg", "tal", "insel",
    "wolke", "regen", "schnee", "hagel", "wind", "sturm", "sonne", "mond", "stern", "himmel",
    "freund", "freundin", "vater", "mutter", "bruder", "schwester", "oma", "opa", "onkel", "tante",
    "arzt", "polizist", "bäcker", "metzger", "maler", "tischler", "elektriker", "mechaniker", "koch", "friseur",
    "kellner", "lehrer", "fahrer", "briefträger", "richter", "anwalt", "soldat", "pilot", "kapitän", "musiker",
    "sänger", "maler", "tänzer", "schauspieler", "dichter", "autor", "journalist", "zeichner", "fotograf", "designer",
    "blau", "rot", "gelb", "grün", "schwarz", "weiß", "grau", "braun", "orange", "violett",
    "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
    "heiß", "kalt", "warm", "kühl", "trocken", "nass", "laut", "leise", "hell", "dunkel",
    "schnell", "langsam", "stark", "schwach", "groß", "klein", "jung", "alt", "neu", "altmodisch",
    "freundlich", "böse", "lustig", "traurig", "müde", "wach", "faul", "fleißig", "klug", "dumm",
    "laufen", "springen", "rennen", "gehen", "fahren", "fliegen", "sitzen", "stehen", "liegen", "schlafen",
    "essen", "trinken", "kochen", "backen", "malen", "schreiben", "lesen", "spielen", "tanzen", "singen",
    "arbeiten", "lernen", "denken", "reden", "hören", "sehen", "fühlen", "riechen", "schmecken", "lachen",
    "weinen", "träumen", "hoffen", "lieben", "hassen", "kämpfen", "gewinnen", "verlieren", "suchen", "finden",
    "stadt", "dorf", "markt", "platz", "straße", "weg", "brücke", "turm", "kirche", "schloss",
    "museum", "theater", "kino", "park", "spielplatz", "bibliothek", "krankenhaus", "apotheke", "supermarkt", "restaurant",
    "brot", "butter", "käse", "wurst", "fleisch", "fisch", "reis", "nudeln", "salat", "gemüse",
    "tomate", "gurke", "zwiebel", "karotte", "kartoffel", "pilz", "mais", "spinat", "bohne", "erbse",
    "wasser", "saft", "kaffee", "tee", "milch", "bier", "wein", "cola", "limonade", "eis",
    "tag", "nacht", "morgen", "abend", "mittag", "jahr", "monat", "woche", "minute", "stunde",
    "januar", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober",
    "november", "dezember", "montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag", "ferien", "urlaub",
    "papier", "glas", "metall", "holz", "stein", "stoff", "plastik", "leder", "gold", "silber",
    "messer", "gabel", "löffel", "teller", "glas", "tasse", "pfanne", "topf", "schüssel", "flasche",
    "hose", "hemd", "pullover", "jacke", "mantel", "schuh", "socke", "mütze", "hut", "schal",
    "ring", "kette", "uhr", "armband", "brille", "tasche", "rucksack", "geldbeutel", "schirm", "gürtel",
    "baby", "kind", "jugendlicher", "erwachsener", "mann", "frau", "oma", "opa", "nachbar", "freund",
    "zoo", "museum", "theater", "kino", "zirkus", "markt", "strand", "wald", "see", "fluss",
    "meer", "insel", "gebirge", "höhle", "wüste", "feld", "wiese", "tal", "berg", "gipfel",
    "spiegel", "bild", "foto", "rahmen", "uhr", "kerze", "pflanze", "vase", "blume", "kissen",
    "decken", "vorhang", "stuhl", "sofa", "bett", "kommode", "tisch", "regal", "lampe", "teppich",
    "buch", "roman", "zeitung", "magazin", "brief", "karte", "post", "tagebuch", "gedicht", "geschichte",
    "computer", "tablet", "handy", "kamera", "mikrofon", "lautsprecher", "fernseher", "radio", "konsole", "controller"
]

def galgenmännchen():
    wort = random.choice(wortliste)

    buchstabenanzahl = len(wort)

    erratene_buchstaben = []

    anzeige = ["_"] * buchstabenanzahl

    übrige_versuche = 8

    versuche = (übrige_versuche - 8) * (-1)

    while True:
        if übrige_versuche == 0:
            print(f"Du hast verloren!\nDas Wort war: {wort}")
            time.sleep(0.5)
            break
        if "_" not in anzeige:
            print(f"Du hast gewonnen!\nBenötigte Versuche:{versuche}")
            time.sleep(0.5)
        if erratene_buchstaben:
            buchstabe = input(f"Rate nochmal einen Buchstaben({übrige_versuche} Versuche)>{anzeige}\n>>>").lower()
        elif not erratene_buchstaben:
            print("Ich habe mir ein Wort ausgedacht...")
            time.sleep(0.25)
            buchstabe = input(f"Errate einen Buchstaben von meinem Wort>{anzeige}\n>>>").lower()
        if buchstabe in wort and not erratene_buchstaben:
            print("Richtig!")
            erratene_buchstaben.append(buchstabe)
            for i in range(len(wort)):
                if buchstabe == wort[i]:
                    anzeige[i] = wort[i]
                else:
                    if anzeige[i] in erratene_buchstaben:
                        anzeige[i] = wort[i]
        elif buchstabe in erratene_buchstaben:
            print("Dieser Buchstabe ist schon aufgedeckt!")
        else:
            print("Falsch!")
            übrige_versuche = übrige_versuche - 1
            time.sleep(0.25)
            print(f"Übrige Versuche:{übrige_versuche}")
            time.sleep(0.25)
        
while True: 
    galgenmännchen()