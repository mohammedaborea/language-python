"""Write a program to check if a user-entered string contains any
numeric digits. Use a for loop to examine each character."""
list_number=['1','2','3','4','5','6','7','8','9','0']
count=0
text=input("Enter the string:")
for i in text:
    if i in list_number:
        count=count+1


if count>0:
    print(f"{text} contains number")
else:
    print(f"{text} does not contain number")