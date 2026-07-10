"""Write a Python function that accepts two integer numbers.
If the product of the two numbers is less than or equal to
1000, return their product; otherwise, return their sum."""

def product(a, b):
    if (a * b) > 1000:
        return a + b
    else:
        return a * b

a = int(input("Enter the value of the first number: "))
b = int(input("Enter the value of the second number: "))

print(product(a, b))
