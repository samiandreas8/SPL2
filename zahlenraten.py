import random
n = in(input("Wählen sie den Zahlenruam aus"))
zufallszahl = randint(1,n)
m = int(input("Geben sie die Anzahl der Versuche ein"))
while(i<=m):
    x=int(input("Geben sie ihren Tipp ein"))
    if (x == zufallszahl):
        print("Sie haben richtig geraten!!")
        break
    else:
        print ("Leider Falsch sie haben noch", i, "Versuche")
        if (x > zufallszahl):
            print("zu groß")
        else:
            print("zu groß")
continue