x=int(input("Enter a number"))
if 10<=x<=20:
    print(x,"ans l'interval [10,20]")
elif -10<=x<=0:
    print(x,"dans l'interval [-10,0]")
else:
    print(x,"n'est pas dans l'interval [10,20]")

if 97<=x<=122:
    print( x,"dans  l'interval [a,z] et lettre correspond est :",chr(x))
else:
    print( x,"n'est pas dans  l'interval [a,z] il est : ",chr(x))
