

from cmath import sqrt

a=int(input("Entrez la valeur de a : "))
b=int(input("Entrez la valeur de b : "))
somme=a+b
produit=a*b
division=a/b
quotient=a//b
reste_de_division=a%b
la_valeur_de_a_puissance_b=a**b
expression=abs(pow(a,2)+sqrt(b))
print("la somme de ",a," et",b," est : ",somme)
print("La produit de ",a," multiple par ",b," est : ",produit)
print ("La division de",a,"et",b,"est : ",division)
print ("La quotient ",a," divisee par ",b,"est : ",quotient)
print ("Le reste de la division ",a,"par",b,"est : ",reste_de_division)
print ("La puissance de ",a,"et",b,"est : ",la_valeur_de_a_puissance_b)
print ("l'expression demandee est",expression)
