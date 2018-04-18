import random
n = int(input("Wählen sie den Zahlenruam aus\n"))
zufallszahl = random.randint(1,n)
m = int(input("Geben sie die Anzahl der Versuche ein\n"))
i=1
while(i<=m):
    x=int(input("Geben sie ihren Tipp ein\n"))
    if (x == zufallszahl):
        print("Sie haben richtig geraten!!")
        i=m
    else:
        print ("Leider Falsch sie haben noch", m-i, "Versuche\n")
        if (x > zufallszahl):
            print("zu groß\n")
        else:
            print("zu klein\n")
    i+=1
