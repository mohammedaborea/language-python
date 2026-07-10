"""Print a downward half-pyramid
pattern using stars (*)."""

for i in range(6,0,-1):
    print("")
    for j in range(i):
        print("* ",end="",)
