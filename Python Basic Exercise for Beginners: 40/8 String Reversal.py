"""Write a program that takes a string and reverses
it (e.g., “Python” becomes “nohtyP”)."""
def reverse(text):
    return text[::-1]



text=input("Enter a string:")
print(reverse(text))