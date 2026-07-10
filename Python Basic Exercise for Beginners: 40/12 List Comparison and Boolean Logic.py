"""Write a function to return True if the first
and last number of a given list is the same.
 If the numbers are different, return False."""
def comerarison(mylist):
    a=len(mylist)
    if mylist[0]==mylist[a-1]:
         return True
    else:
        return False




list=[]
n=int(input("Enter the length of the list: "))
for i in range(n):
    b=int(input(f"List[{i+1}]="))
    list.append(b)

print(list)
print(comerarison(list))