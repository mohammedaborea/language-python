# Ce programme explore différentes opérations sur une chaîne de caractères.
# Il affiche sa longueur, extrait des sous-chaînes, inverse le texte,
# recherche et compte certains mots, modifie la casse des caractères,
# supprime les espaces inutiles et remplace les espaces par un autre symbole.
ch='Le travail est un VRAI tresor. Un travail ASSIDU surmonte tous les obstacles  '
print("La taille de chain est : ",len(ch))
print(ch[3:10])
print(ch[3:])
print(ch[:2])
print(ch[-6:])
print(ch[::2])
print(ch[::-1])
print(ch[9:2])
print(ch[9:2:-1])
print(ch.find('a'))
print(ch.find('travail'))
print(ch.rfind('travail'))
print(ch.count('travail'))
print(ch.lower())
print(ch.upper())
print(ch.capitalize())
print(ch.swapcase())
print (ch.strip())
print(ch.replace(' ','*'))
