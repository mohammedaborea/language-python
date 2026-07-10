"""Iterate through a given list of numbers and print only
those numbers which are divisible by 5."""
def filtering(list):
    for i in list :
        if i%5==0:
            print(i)




list=[]
n=int(input("Enter the length of the list: "))
for i in range(n):
    b=int(input(f"List[{i+1}]="))
    list.append(b)

print(list)
filtering(list)
