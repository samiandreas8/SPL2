a=int(input("geben sie eine Zahl ein"))
for i in range(1,a+1):
    if (i < a):
        print(i, end=" ,")
    else:
        print(i)
for i in range(1,a+1):
    if (a%2 == 0):
        if (i < a):
            print(i, end=" ,")
        else:
            print(i)
for i in range(1,a+1):
    if  (a%2 != 0):
        if (i < a):
            print(i, end=" ,")
        else:
            print(i)
    
        
    