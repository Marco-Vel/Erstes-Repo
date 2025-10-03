import random; import time

def Zahlenraten():
    computer = random.randint(1,100)

    while True:
        versuche = 0

        spieler = input("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.\n" \
        "Rate mal an welche Zahl ich denke:\n")
        try:
            spieler = int(spieler)
            if (spieler == computer):
                versuche = versuche + 1
                print("Du hast meine Zahl erraten!")
                if(versuche == 1):
                    print(f"Du hast einen Versuch gebraucht!")
                    time.sleep(0.75)
                    break
                else:
                    print(f"Du hast {versuche} Versuche gebraucht!")
                    time.sleep(0.75)
                    break
            elif (spieler >= computer):
                print("Deine Zahl ist größer als meine...")
                time.sleep(0.75)
                versuche = versuche + 1
            elif (computer >= spieler):
                print("Deine Zahl ist kleiner als meine...")
                time.sleep(0.75)
                versuche = versuche + 1
        except TypeError:
            print("Gebe eine Zahl an!")
            time.sleep(0.75)
            return

Zahlenraten()