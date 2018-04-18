a=int(input("geben sie eine Zahl ein\n"))
for i in range(1,a+1):
    if (i < a):
        print(i, end=" < ")
    else:
        print(i)
#You are a gerade Farmer
print("\n")
for i in range(1,a+1):
    if (i % 2 == 0):
        if (i < a):
            print(i, end=" < ")
        else:
            print(i)
#You are a ungerade Farmer
print("\n")
for i in range(1,a+1):
    if  (i % 2 != 0):
        if (i < a-1):
            print(i, end=" < ")
        else:
            print(i)
print("\n")
for i in range(1,a+1):
    if  (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i>1):
        print(i, end="; ")
        