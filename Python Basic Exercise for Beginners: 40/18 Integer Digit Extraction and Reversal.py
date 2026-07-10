""" Write a program to extract each digit from an integer in the reverse order."""
def thousands_place(number):
    thousands=(number//1000)%10
    return thousands


def hundreds_place(number):
    hundreds=(number//100)%10
    return hundreds

def tens_place(number):
    tens=(number//10)%10
    return tens

def ones_place(number):
    onces=number%10
    return onces


number = int(input("Enter a number: "))
print(ones_place(number),tens_place(number),hundreds_place(number),thousands_place(number),sep=" ")

"""Only number 4 places and another general solution is :"""

n=int(input("Enter the number :"))
text=str(n)
for i in range(len(text)):
    place=(n//10**i)%10
    print(place, end=" ")
