# my savings amount
saving = 8000

# interest rate
interest_rate = 0.05

# rule of 72
year = 72 /(interest_rate * 100)

# Double savings
Double_saving = saving * 2

# result
print("current saving is $" + str(saving))
print(" At a " + format(interest_rate, ".0%") + " interest rate, saving account")
print("worth $" + format(Double_saving, ".2f") + " in " + format(year, ".1f") + " years")
