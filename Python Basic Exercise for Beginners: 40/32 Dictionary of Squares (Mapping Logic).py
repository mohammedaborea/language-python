"""Create a dictionary where the keys are numbers from 1 to 10 and
the values are the squares of those numbers (e.g., 2: 4, 3: 9)."""
dictionry={}
for i in range(1,11):
    key=i
    value=i**2
    dictionry[key]=value


print(dictionry)