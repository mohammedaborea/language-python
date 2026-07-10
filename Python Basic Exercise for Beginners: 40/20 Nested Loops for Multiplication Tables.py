""" Print a multiplication table
 from 1 to 10 in a formatted grid."""


for i in range(1,11):
    print("")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")