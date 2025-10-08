import random

def spiel():
    optionen = ["schere","stein" ,"papier"]

    #Spielerwahl
    spieler = input("Wähle Schere, Stein oder Papier: ").lower()

    if spieler not in optionen:
        print("Ungültige Eingabe!")
        return #Abbruch

    #Computerwahl

    computer = random.choice(optionen)
    print(f"Computer wählt:{computer}")

    #Regeln

    if spieler == computer:

        print("Unentschieden!")
    
    elif (
        (spieler == "schere" and computer == "papier")
        or (spieler == "stein" and computer == "schere")
        or (spieler == "papier" and computer == "stein")
    ):
        print("Du gewinnst!")
    else:
        print("Computer gewinnt!")

def spiel_ausführen():
    while True:
        spiel() #Spiel starten
        abbruch = input("Drücke q zum beenden oder eine beliebige Taste zum weiterspielen!\n").lower()
        if(abbruch == "q"):
            break

spiel_ausführen()