"""Write a function called exponent(base, exp)
 that returns an integer value of the
 base raised to the power of the exponent."""
def exponent(base, exp):
    result=base**exp
    return result



base=int(input("Enter The base:"))
exp=int(input("Enter the exponent"))
print(f"{base} raises to the power {exp}:{exponent(base,exp)}")