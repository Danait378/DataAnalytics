# Ask user for saving account
savings = float(input("what is your savings amount"))

# Ask user for interest rate
interest_rate = float(input("what is the interest rate"))

# rule of 72
year = 72 / interest_rate

# Double savings
new_amount = savings * 2

# result
print("current saving is $" + str(savings))
print(" At a " + format(interest_rate, ".0%") + " interest rate, saving account")
print("worth $" + format(new_amount) + " in " + str(year) + "years")

# observations
# input() reads values as text (strings)
# float() is for math calculation
