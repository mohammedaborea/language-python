"""Display only those characters which
are present at an even index number in given string."""

def character(character):
    for i in range(len(character)):
        if i%2==0:
            print(character[i])


char=list(input("Enter the character:"))
character(char)
