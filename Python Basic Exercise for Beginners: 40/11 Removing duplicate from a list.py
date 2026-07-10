"""Write a script that takes a list containing duplicate items
and returns a new list with only unique elements."""
def remove_duplicates(list):
    new_list = []
    for i in list :
        if i not in new_list:
            new_list.append(i)
    return new_list
n=int(input("Enter the length of the list:"))
list=[]
for i in range(n):
    element=int(input(f"List[{i+1}]="))
    list.append(element)

new_list=remove_duplicates(list)
print(f"The list before removing is {list}")
print(f"The list after removing duplicates is {new_list}")

