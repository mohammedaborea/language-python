"""Print a downward number pattern
 where each row starts with a decreasing value."""
for i in range(10,0,-1):
    print("")
    for j in range(i,0,-1):
        print(j,end=" ",sep="")

