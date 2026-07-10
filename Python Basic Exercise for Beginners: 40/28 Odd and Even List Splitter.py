"""Start with a list of 10 numbers. Iterate through
them and sort them into two separate lists: one
for even numbers and one for odd numbers."""


list_1=[]
for i in range(10):
    a=int(input(f"list[{i+1}]="))
    list_1.append(a)

print(f"Your list :{list_1}")

even_list=[]
odd_list=[]

for i in list_1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Even list : {even_list}")
print(f"Odd list : {odd_list}")


