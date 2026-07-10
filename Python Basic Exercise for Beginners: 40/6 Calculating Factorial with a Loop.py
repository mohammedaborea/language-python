"""Write a program that calculates the factorial
of a given number (e.g., 5!) using a for loop."""
a=int(input("Enter the first number: "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i


print(f"The factorial of {a} is {factorial}")