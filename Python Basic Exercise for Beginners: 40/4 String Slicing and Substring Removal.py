"""Write a function to remove characters from a string starting
from index 0 up to n and return a new string."""
def remove_chars(char, n):
    return char[n:]

char = input("Enter the string: ")
n = int(input("Enter the number: "))

print(remove_chars(char, n))
