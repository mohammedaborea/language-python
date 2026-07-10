"""Create a list of 5 fruits. Add a new fruit to the end of the
 list, then remove the second fruit (at index 1)."""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
fruits.append('fig')
print(fruits)
del fruits[1]
print(fruits)