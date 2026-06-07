n1 = int(input("Entrez la taille de la premiere liste 1 : "))
list1 = []

for i in range(n1):
    element = int(input(f"[{i + 1}]="))
    list1.append(element)

while True:
    n2 = int(input("Entrez la taille de la deuxieme liste 2 : "))

    if n1 == n2:
        break
    else:
        print("Il faut entrer la meme taille")

list2 = []

for i in range(n2):
    element1 = int(input(f"[{i + 1}]="))
    list2.append(element1)

print(list1)
print(list2)

list3 = []

for i in range(n1):
    s = list1[i] + list2[i]
    list3.append(s)

print(list3)
