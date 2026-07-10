"""Take two lists and find the elements that appear
 in both. Use Sets to perform the operation."""
n1=int(input("Enter the length of the list:"))
list1=[]
for i in range(n1):
    a1=int(input(f"list1[{i+1}]="))
    list1.append(a1)

list2=[]
for i in range(n1):
    a1=int(input(f"list2[{i+1}]="))
    list2.append(a1)

print(list1)
print(list2)
set1,set2=set(list1),set(list2)
set3=set1 & set2
print(f"Common Elements: {set3}")