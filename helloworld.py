print("Hallo Servus")
name=input("Wie lautet ihr Name?\n")
print("Schhön dich zu treffen", name, "Die länge von dem Namen ist", len(name),"Zeichen lang.")
alter=input("Wie alt bist du?\n")
alter=int(alter)
if (alter > 100):
    print ("Das ist wohl ein Scherz  oder? ;-)")
else:
    print("Du wirst in einem Jahr", alter+1, "Jahre alt sein.")
print ("Juice Tschuiss")