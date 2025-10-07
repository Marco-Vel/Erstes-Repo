import os; from pathlib import Path; import time
 
ordner = Path(__file__).parent / "notizen"
ordner.mkdir(exist_ok = True)

def update_dateien_anzahl():
    global dateien_anzahl
    dateien = [f.name for f in ordner.iterdir() if f.is_file()]
    dateien_anzahl = len(dateien)   

hauptmenu_optionen = ["Notiz hinzufügen", "Notizen ansehen", "Notizen löschen"]

def notiz_hinzufuegen():
    while True:
        print(">>>Notiz hinzufügen")
        titel = input("Gebe den Titel der Datei an:\n").lower()
        inhalt = input("Gebe den Inhalt der Datei an:\n")

        datei_pfad = ordner / f"{titel}.txt"
        with open(datei_pfad, "w", encoding="utf-8") as datei:
            datei.write(inhalt)
        print(f"Notiz {inhalt} gespeichert...")
        break

def notizen_ansehen():

    while True:
        dateien = [f for f in ordner.iterdir() if f.is_file()]
        print(f">>>Notizen ansehen\n")
        for i, datei in enumerate(dateien, start=1):
            print(f"{i}>{datei.name}")

        input("\n>(Enter zum fortfahren)\n")
        break

def notizen_loeschen():
    while True:
        update_dateien_anzahl()
        if dateien_anzahl >= 0:
            dateien = [f.name for f in ordner.iterdir() if f.is_file()]
            print("\nAktuelle dateien im Ordner:\n")
            for i, datei in enumerate(dateien, start=1):
                print(f"{i}>{datei}")
            angabe_loeschen = input("\nGebe den Namen der zu löschenden Datei an:\n")
            try:
                if angabe_loeschen in dateien:
                    sicher_abfrage = input("Diese Datei wird gelöscht, bist du dir sicher?\n>Ja\n>Nein\n>>>").lower()

                    if sicher_abfrage == "ja":
                        print("gelöscht")

                    elif sicher_abfrage not in ["nein", "ja"]:
                        value_input = input("Gebe eine Option an oder verlasse mit(q)")
                        if value_input == "q":
                            break

                    elif sicher_abfrage == "nein":
                        print(f"{angabe_loeschen} wurde behalten.")

                    break
                else:
                    raise NameError
            except:
                input("Diese Datei existiert nicht...\n\n(Weiter mit Enter)\n")
                break
        else:
            input("Keine Dateien gespeichert...\n(Enter zum fortfahren)")
            
hauptmenu_funktionen = [notiz_hinzufuegen, notizen_ansehen, notizen_loeschen]

def menu_optionslistung():
    for i, variable_optionen in enumerate(hauptmenu_optionen, start=1):
        print(f"{i}>{variable_optionen}")

def hauptmenu():
    while True:
        menu_optionslistung()
        auswahl = input("\n\n>>>")
        try:
            auswahl_num = int(auswahl)
            if 1 <= auswahl_num <= len(hauptmenu_optionen):
                gewählte_option = hauptmenu_optionen[auswahl_num - 1]
                print(f"Hauptmenu > {gewählte_option}")
                hauptmenu_funktionen[auswahl_num - 1]()
                
            else:
                print("Wähle eine Option...")
        except:
            print("Gebe eine Zahl an...")

hauptmenu()