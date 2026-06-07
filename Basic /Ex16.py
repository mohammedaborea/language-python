while True:
    try:
        n = int(input("Entrez un nombre : "))
        break
    except:
        pass

liste = []

for i in range(1, n + 1):
    if n % i == 0:
        liste.append(i)

print("Les diviseurs de", n, "sont", liste)
