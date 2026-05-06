# Ask user for saving account
savings = float(input("what is your savings amount"))

# Ask user for interest rate
interest_rate = float(input("what is the interest rate"))

# rule of 72
year = 72 / interest_rate

# Double savings
new_amount = savings * 2

# result using f-string
print(f"current savings is ${savings}")
print(f" At a {interest_rate}% interest rate, saving account will be")
print(f"worth ${new_amount}  in {year:.1f} years")

# observations
# input() reads values as text (strings)
# float() is for math calculation
