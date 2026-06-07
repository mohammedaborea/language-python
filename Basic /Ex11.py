print("Programme pour verification de l'annee bissextile")
annee=int(input("Entrez un annee pour verification : "))
if annee%4==0 and annee%100!=0 or annee%400==0:
    print(annee,"est bissextile")
else:
    print(annee,"n'est pas  bissext
