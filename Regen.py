regen=True
if (regen==True):
    Regenschirm=input("Hast du einen Regenschirm?y/n\n")
    if (Regenschirm=="n"):
        while(regen):
            print("warten bis der Regen aufhört")
            regen1=input("Regnet es noch immer?y/n\n")
            if(regen1=="n"):
                regen=False
        print("jetzt regnet es nicht mehr")
print ("Geh nach draußen")