# Ce programme simule un petit jeu de hasard.
# Un nombre aléatoire est généré puis analysé
# afin de déterminer le gain ou la perte du joueur
# selon certaines règles prédéfinies.
import random as r
input("Clique 'Entre' pour commencer")
nombre=r.randint(1,100)
print("Le nombre tire au hasard est : ",nombre)
if int(nombre)%2==0:
    print("Vous allez gagner 1 Dinar")
elif chr(nombre)[-1]=='7':
    print("Vous avez gagner 10 Dinars")
else:
    print("Vous avez perdre 3 Dinar")
