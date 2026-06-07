# Ce programme réalise un tour de magie mathématique.
# L'utilisateur suit une série d'opérations sur un nombre secret,
# puis saisit le résultat final. Le programme tente ensuite
# de retrouver le nombre choisi au départ et vérifie la validité du calcul.
print("Je suis le magicien 😈 ")
print ("Penser a un nombre en ta tete ")
input ("Appuie sur Entree quand c'est fait ...😁 ")
print ("Mutiplie ce nombre par 5 ")
input ("Appuie sur Entree quand c'est fait ... 😁")
print ("Ajoute ce nombre un valeur 7")
input ("Appuie sur Entree quand c'est fait ... 😁")
print ("Mutiplie ce nombre par 4 ")
input ("Appuie sur Entree quand c'est fait ... 😁")
print ("Ajoute ce nombre un valeur 6")
input ("Appuie sur Entree quand c'est fait ... 😁")
print ("Mutiplie ce nombre par 5 ")
input ("Appuie sur Entree quand c'est fait ... 😁")
resultat=input("Entrez la valeur obtinee de calcule : ")

if int(resultat) % 10 == 0:
    nombre=(int(resultat)-170)//100
    print(" Votre nombre est ",nombre)
else:
    print("Votre calcule est faux 😏")


