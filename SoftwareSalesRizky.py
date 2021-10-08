#Inputs and variables

Quantity = float(input("Enter the number of packages you would like to purchase: "))
Discount = 0

#DiscountChecking

if Quantity < 10:
    Discount = 0
if 10 <= Quantity <= 19:
    Discount = 10
if 20 <= Quantity <= 49:
    Discount = 20
if 50 <= Quantity <= 99:
    Discount = 30
if Quantity >= 100:
    Discount = 40

#Calculations and Formatting

DiscountAmount = (99 * Quantity) * Discount/100
Total = (99 * Quantity) - DiscountAmount

FormatDiscount = format( DiscountAmount, ",.2f")
FormatTotal = format( Total, ",.2f")

#Output

print(f"""Discount Amount @ {Discount}%: ${FormatDiscount}
Total Amount: ${FormatTotal}""")