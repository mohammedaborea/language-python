import random

compteur = 0

while True:
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)

    compteur += 1

    print(de1, de2)

    if de1 == 6 and de2 == 6:
        break

print("Nombre de lancers nécessaires est :", compteur)
