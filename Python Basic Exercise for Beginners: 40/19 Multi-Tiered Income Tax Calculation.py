"""Calculate income tax for a given income based on these rules:
First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax"""


def tax_total_tier(income):
    tier_1=(income+10000)-income
    tier_2=(income)-(income-10000)
    rest=income-(tier_1+tier_2)
    tax_tier_1=(0/100)*tier_1
    tax_tier_2=(10/100)*tier_2
    tax_rest=(20/100)*rest
    tax_total=tax_tier_1+tax_tier_2+tax_rest
    return tax_total

while True:
    income = int(input("Enter the income $: "))

    if income >= 0:
        break

if income<10000:
    print("Total income tax to pay is 0")
elif income<=20000:
    print("Total income tax to pay is $",(income - 10000) * 10 / 100)
else:
    print(f" Total income tax to pay is ${tax_total_tier(income)}")
