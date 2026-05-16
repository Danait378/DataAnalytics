# Open the file in read mode
f = open("about_me.txt", "r")

# Read the first 50 characters
first_50 = f.read(50)

# Save the next 4 lines into a list
next_four_lines = []

for i in range(4):
    next_four_lines.append(f.readline())

# Read the next 100 characters
next_100 = f.readlines(100)

# Print results
print("First 50 characters:")
print(first_50)

print("\nNext four lines:")
print(next_four_lines)

print("\nNext 100 characters:")
print(next_100)

# Close the file
f.close()