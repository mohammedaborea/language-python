taille=int(input("Entrez La taille de la liste : "))
list1=[]
for i in range(taille):
    element=int(input(f"[{i+1}]="))
    list1.append(element)
print("Votre liste est ",list1)

list2=[]
for i in list1:
    if list1.count(i)>1:
        list2.append(i)
        list1.remove(i)
print("les elementes ddupliquees dans votre liste sont : ",list2)

