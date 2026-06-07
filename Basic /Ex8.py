# Ce programme demande les longueurs des côtés d'un triangle.
# Il vérifie que les valeurs saisies sont positives,
# puis détermine le type du triangle selon ses côtés.
# Enfin, il indique si le triangle est rectangle.
while True :
    a=float(input("Entrez une valeur positive de a : "))
    if a>0:
        break
while True :
    b=float(input("Entrez une valeur positive de b : "))
    if b>0:
        break
while True :
    c=float(input("Entrez une valeur positive de c : "))
    if c>0:
        break
if a==b and b==c:
    print("Le triangle est equilateral")
elif a==b or b==c or c==a:
    print("Le triangle est isocele ")
else:
    print("Le triangle est  quelconque")
if c**2==a**2+b**2:
    print("Le triangle est rectangle")
