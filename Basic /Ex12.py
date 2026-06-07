import random

# Générer un nombre aléatoire entre 0 et 255
nombre = random.randint(0, 255)
print("Le nombre aléatoire:", nombre)

# Convertir le nombre en caractère ASCII
char = chr(nombre)
print("Le caractère correspondant dans ASCII:", char)

# Déterminer la nature du caractère basé sur son code ASCII
if nombre >= 48 and nombre <= 57:
    print("C'est un chiffre.")
elif nombre >= 65 and nombre <= 90:
    if char in 'AEIOU':
        print("Lettre majuscule voyelle.")
    else:
        print("Lettre majuscule consonne.")
elif nombre >= 97 and nombre <= 122:
    if char in 'aeiou':
        print("Lettre minuscule voyelle.")
    else:
        print("Lettre minuscule consonne.")
else:
    print("Ce n'est ni une lettre, ni un chiffre.")
