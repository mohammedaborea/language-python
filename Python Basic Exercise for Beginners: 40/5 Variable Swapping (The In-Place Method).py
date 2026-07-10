"""Write a program to swap the values of two variables, a and b,
 without using a third temporary variable."""
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(f"Before swaping a={a},b={b}")
a,b=b,a
print(f"After swaping a={a},b={b}")