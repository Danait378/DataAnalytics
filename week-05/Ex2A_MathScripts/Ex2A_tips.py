# define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# calculate the unknown
total_due = food_cost + tax + tip

# The str() function changes into text so it can print together in words.

# Display the results
# print(The total due is " + str(total_due)

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))

# print("Tip is " + str(tip))

print("Tip is " + format(tip, ".2f"))

print("Total due is " + str(total_due))