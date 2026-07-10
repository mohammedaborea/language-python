""" Ask the user for a sentence. Replace every empty space in that
sentence with an underscore (_) and print the final result."""
from idlelib.replace import replace

sentence=input("Enter the sentence:")
print(f"Your sentence is: {sentence.replace(' ', '_')}")
