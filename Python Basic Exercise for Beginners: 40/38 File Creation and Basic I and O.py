"""Write a program that creates a new text file named notes.txt,
writes three separate lines of text to it, and then
reads that file back to display the contents in the console."""
with open('note.txt','a') as file:
    file.write("Hello, this is my first note.\n")
    file.write("Python file handling is simple.\n")
    file.write("End of file.\n")

with open("note.txt", "r") as file:
    content = file.read()
    print(content)