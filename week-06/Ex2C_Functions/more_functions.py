# Exercise 2.C - More Functions
# Beginner version


# Function for mailing label
def display_mailing_label(name, address, city, state, zip):

    print(name)
    print(address)
    print(city, state, zip)


# Function for adding numbers
def add_numbers(*numbers):

    total = 0

    for num in numbers:
        total = total + num

    print(numbers, "=", total)


# Function for receipt
def display_receipt(total_due, amount_paid):

    print("Total Due: $", total_due)
    print("Amount Paid: $", amount_paid)

    if amount_paid > total_due:

        change = amount_paid - total_due
        print("Change Due: $", change)

    elif amount_paid == total_due:

        print("Change Due: $0")

    else:

        balance = total_due - amount_paid
        print("Still Owed: $", balance)


# Mailing labels
display_mailing_label(
    "Danait Berhane",
    "1140 providence rd",
    "Charlotte",
    "NC",
    "28257")


print()

display_mailing_label(
    "john doe",
    "35 main Road",
    "charlotte",
    "NC",
    "28225"
)

print()


# Add numbers
add_numbers(6)

add_numbers(6, 15)

add_numbers(1, 2, 3, 4)

print()


# Receipts
display_receipt(30, 40)

print()

display_receipt(50, 50)

print()

display_receipt(80, 40)