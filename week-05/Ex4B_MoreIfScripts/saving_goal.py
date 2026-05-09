balance = 50
goal = 300
weekly_savings = 40

while balance < goal:
    balance = balance + weekly_savings

    if balance > goal / 2:
        print("Almost there! My balance is now $" + str(balance))
    else:
        print("My balance is now $" + str(balance))

print("Goal met! I saved $" + str(balance))