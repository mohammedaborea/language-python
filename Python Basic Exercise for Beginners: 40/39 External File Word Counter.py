"""Write a script that opens an existing .txt file and
counts the total number of words it contains."""
try:
    with open("note.txt", "r") as file:
        data=file.read()
        words=data.split()
        words_count=len(words)
        print(f"The file contains {words_count} words.")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
