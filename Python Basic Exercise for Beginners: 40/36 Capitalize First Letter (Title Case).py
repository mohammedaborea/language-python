"""Write a program to capitalize the first letter of each
word in a given string without using the built-in .title() method."""
text=input("Enter the text:")
words=text.split()
for i in range(len(words)):
    words[i]=words[i].capitalize()

new_text=" ".join(words)

print(new_text)