print("     Programme pour calculer la surpoid     ")
taille=float(input("Entrez votre taille en metre : " ))
masse=float(input("Entrez votre masse en kg : "))
mcl=masse/taille**2
print(mcl)
if mcl<25:
    print("Vous n'etes pas en surpoids")
else:
    print("Vous etes en surpoids")
