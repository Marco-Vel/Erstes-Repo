import random

def Zahlenraten():
    computer = random.randint(1,100)

    while True:
        versuche = None

        spieler = input("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.\n" \
        "Rate mal an welche Zahl ich denke:\n")
        try:
            spieler = int(spieler)
            if (spieler == computer):
                versuche = versuche + 1
                print("Du hast meine Zahl erraten!")
                if(versuche == 1):
                    print(f"Du hast einen Versuch gebraucht!")
                    break
                else:
                    print(f"Du hast {versuche} Versuche gebraucht!")
                    break
            elif (spieler >= computer):
                print("Deine Zahl ist größer als meine...")
                versuche = versuche + 1
                return
            elif (computer >= spieler):
                print("Deine Zahl ist kleiner als meine...")
                versuche = versuche + 1
                return
        except:
            print("Gebe eine Zahl an!")

Zahlenraten()