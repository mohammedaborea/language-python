"""Create a list of 5 words. Write a loop that iterates through the list and
prints each word alongside its character count."""
from itertools import count

words=[]
while True:
    n = int(input("Enter the length of the list:"))
    if n>0:
        break

for i in range(n):
    word=input(f"word[{i+1}]=")
    words.append(word)

print(f"Your list :{words}")
for i in words:
    print(f"{i} - {len(i)}")

