"""Write a program that counts how many times each word appears
in a given paragraph and stores these counts in a dictionary."""
from os import remove

text = "apple banana apple cherry banana apple"
words=[]
w=""
for i in text:
    if i !=" ":
        w=w+i
    else:
        if w !="":
            words.append(w)
            w=""

print(words)
for i in words:
    print(f"'{i}':{words.count(i)}")