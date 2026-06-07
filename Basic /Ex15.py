import random as r

sc = r.randint(1,100)
compt = 0

while True:
    n = int(input("Entrez un nombre : "))
    if n != sc:
        compt += 1
    if n > sc:
        print("Trop grand")
    elif n < sc:
        print("Trop petit")
    else:
        print("Bravo !")
        print("Nombre de tentatives =", compt)
        break
