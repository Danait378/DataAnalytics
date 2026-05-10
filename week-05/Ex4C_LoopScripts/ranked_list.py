foods = ["pasta", "tacos", "ramen", "pizza", "injera"]

number = 1

for food in foods:
    if number == 1:
        print(str(number) + ". " + food + " - favorite")
    else:
        print(str(number) + ". " + food)

    number = number + 1