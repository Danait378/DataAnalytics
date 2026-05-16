# exception_basics.py
# Practicing different types of exceptions using try-except

# -----------------------------
# ValueError Example
# -----------------------------

try:
    age = int("twenty")
except ValueError:
    print("ValueError: You can only convert numbers, not words.")
else:
    print(age)
finally:
    print("Let's try another one...\n")


# -----------------------------
# NameError Example
# -----------------------------

try:
    print(favorite_food)
except NameError:
    print("NameError: This variable has not been created yet.")
else:
    print(favorite_food)
finally:
    print("Let's try another one...\n")


# -----------------------------
# TypeError Example
# -----------------------------

try:
    result = "5" + 10
except TypeError:
    print("TypeError: You cannot add a string and an integer together.")
else:
    print(result)
finally:
    print("Let's try another one...\n")


# -----------------------------
# SyntaxError Example
# -----------------------------
# SyntaxError is special because it stops the script before running.
# We use exec() so we can catch the error safely.

try:
    exec("print('Hello'")
except SyntaxError:
    print("SyntaxError: There is a missing parenthesis.")
else:
    print("Code worked correctly.")
finally:
    print("Let's try another one...\n")


