"""Create a new list from two given lists such that the new list
contains odd numbers from the first
 list and even numbers from the second list."""

def filtering(list1,list2):
    new_list=[]
    for i in list1:
        if i%2!=0:
            new_list.append(i)
    for i in list2:
        if i%2==0:
            new_list.append(i)

    return new_list
n1=int(input("Enterthe length of the first list: "))
n2=int(input("Enter the length of the second list: "))
list1=[]
list2=[]
print("List 1:")
for i in range(n1):
    a1=int(input(f"list1[{i+1}]="))
    list1.append(a1)
print("List 2:")
for i in range(n2):
    a2=int(input(f"list2[{i+1}]="))
    list2.append(a2)
new_list=filtering(list1,list2)
print(f"list1={list1}")
print(f"list2={list2}")
print(f"new_list={new_list}")











