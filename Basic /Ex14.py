voyelles = 'aeiouy'

while True:
    mot = input("Entrez le mot pour compter: ")
    if mot.islower():
        break
    else:
        print("Erreur : Le mot doit etre en minuscule uniquement")

compteur = 0

for lettre in mot:
    if lettre in voyelles:
        compteur += 1

print("Nombre de voyelles est", compteur)


