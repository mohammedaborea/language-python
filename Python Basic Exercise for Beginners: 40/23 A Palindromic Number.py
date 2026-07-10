"""Write a program to check if a given number is a palindrome. A palindrome number
 remains the same when its digits are reversed (e.g., 121, 545)."""
while True:
    nm=int(input("Enter the positive number :"))
    if nm>=0:
        break

t_nm=str(nm)
list1=[]
list2=[]
for i in range(len(t_nm)):
    place=(nm//10**i)%10
    list1.append(place)


for i in range(len(t_nm)-1,-1,-1):
    place = (nm // 10 ** i) % 10
    list2.append(place)

if (list1==list2):
    print(f"{nm} is a palindrome")
else:
    print(f"{nm} is not a palindrome")