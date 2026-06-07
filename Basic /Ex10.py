voyelles = ('a', 'i', 'o', 'u', 'y')
while True:
    mot_de_passe = input("Entrer un mot de passe: ")
    if 6 < len(mot_de_passe) < 10 and mot_de_passe[0] in voyelles:
        break
# while True :
#     mot=input("Entrez le mot de passe:")
#     if 6<=len(mot)<=10 and 65<=ord(mot[0])<=90:
#         break
#     print("Le mot de passe n'est pas valide")
