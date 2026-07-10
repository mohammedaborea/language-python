"""Write a program to count the total number of vowels
(a, e, i, o, u) present in a given sentence."""
def count_vowels(text):
    list_vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in text:
        if i in list_vowels:
            count+=1
    return count

text=input("Enter a string:")
print(count_vowels(text))