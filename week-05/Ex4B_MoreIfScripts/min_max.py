a = 34
b = 12
c = 27

# Smallest number
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

# Largest number
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

print("The smallest number is", smallest)
print("The largest number is", largest)