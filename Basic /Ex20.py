def unique(liste):
    liste1 = []
    for i in liste:
        while i not in liste1:
            liste1.append(i)

    for i in liste:
        if liste.count(i) > 1 and i not in liste1:
            liste1.append(i)

    return liste1

taille=int(input("Entrer la taille de la liste  : "))
liste=[]
for i in range (taille):
    a=int(input(f"[{i+1}]="))
    liste.append(a)
print("Votre liste sera : ",unique(liste))
