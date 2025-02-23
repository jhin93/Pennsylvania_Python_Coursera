
bill = float(input("How much is the meal?"))
tax = float(input("What is the sales tax(in %)?"))
tip = float(input("How much tip do you want to give(in %)?"))

tax_amount = (bill * tax) / 100
total = bill + tax_amount
tip_amount = (total * tip) / 100

total = total + tip_amount

#round the total to 2 decimal places
total = round(total, 2)

print("The total bill is $", total, sep = '')