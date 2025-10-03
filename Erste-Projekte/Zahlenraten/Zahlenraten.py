import random; import time

def Zahlenraten():
    computer = random.randint(1,100)                                                    #Random

    versuche = 0                                                                        #Aufzählung
    
    while True:
        spieler = input("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.\n" \
        "Rate mal an welche Zahl ich denke:\n")
        try:
            spieler = int(spieler)
            if (spieler == computer):
                versuche = versuche + 1
                print("Du hast meine Zahl erraten!")
                if(versuche == 1):                                                      #Wenn ein Versuch benötigt wird print Ausgabe
                    print(f"Du hast einen Versuch gebraucht!")
                    time.sleep(0.75)
                    break
                else:
                    print(f"Du hast {versuche} Versuche gebraucht!")                    #Wenn mehrere Versuche benötigt werden print Ausgabe
                    time.sleep(0.75)
                    break
            elif (spieler >= computer):                                                 #Wenn Zahl des Spielers größer ist
                print("Deine Zahl ist größer als meine...")
                time.sleep(0.75)
                versuche = versuche + 1
            elif (computer >= spieler):                                                 #Wenn Zahl des Computers größer ist
                print("Deine Zahl ist kleiner als meine...")
                time.sleep(0.75)
                versuche = versuche + 1
        except TypeError:
            print("Gebe eine Zahl an!")
            time.sleep(0.75)
            return

while True:                                                                             #Schleife für die Wiederholbarkeit
    Zahlenraten()        

    q = input("Spiel erneut spielen?\n>Ja\n>Nein\n>").lower()                           #Abfrage ob Spieler weiterspielen möchte
    if(q == "nein"):
        print("Bis zum nächsten Mal!")
        time.sleep(0.75)
        break