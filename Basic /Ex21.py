# cal(ch)
# def cal(ch):
#     nblettre = 0
#     nbchiffre = 0
#
#     for i in ch:
#         if i.isalpha():
#             nblettre += 1
#         elif i.isdigit():
#             nbchiffre += 1
#
#     print("Le nombre de lettres est :", nblettre)
#     print("Le nombre de chiffres est :", nbchiffre)
def cal(ch):
    nblettre=0
    nbchiffre=0
    for i in ch:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122:
            nblettre=nblettre+1

    for i in ch:
        if 48<=ord(i)<=57:
            nbchiffre=nbchiffre+1

    print("la nombre de lettre est : ",nblettre)
    print("la nombre de lettre du chiffre est ",nbchiffre)
ch=input("Entrez un phrase  : ")
