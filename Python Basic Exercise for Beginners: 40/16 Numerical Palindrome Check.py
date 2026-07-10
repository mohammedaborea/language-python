"""Write a program to check if a given number is a palindrome
(reads the same forwards and backwards)."""
def palindrome(text):
    if text[::-1]==text:
        return True
    else:
        return False

number=int(input("Enter a number:"))
text=str(number)
print(f"Your number is {number}")
result=palindrome(text)
if result == True:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")