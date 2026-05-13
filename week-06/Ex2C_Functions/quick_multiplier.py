# quick_multiplier.py

# This lambda doubles whatever value is given
doubler = lambda n: n * 2

print("Testing doubler:")
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))


# This lambda triples whatever value is given
tripler = lambda n: n * 3

print("(Testing tripler:")
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))


# Function that creates different multipliers
def multiplier(number):

    return lambda n: n * number


# Creating new multiplier functions
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Testing the new multipliers
print("\nTesting more multipliers:")

print("4 times 3 =", quadrupler(3))
print("5 times 3 =", quintupler(3))
print("6 times 3 =", sextupler(3))
print("7 times 3 =", septupler(3))
print("8 times 3 =", octupler(3))
print("9 times 3 =", nonupler(3))
print("10 times 3 =", decupler(3))