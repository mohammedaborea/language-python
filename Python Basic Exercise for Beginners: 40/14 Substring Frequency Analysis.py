# Write a program to find how many times the substring “Emma” appears in a given string.
def analyse(text,value):
    count=text.count(value)
    return count

text=input("Enter a string:")
value=str(input("Enter a substring:"))
print(analyse(text,value))
