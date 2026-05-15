"""
restaurants.py
This program creates restaurant objects and prints information about them.
"""

# Create a Restaurant class
class Restaurant:
    """A simple class used to describe restaurants."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    # Describe the restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    # Show that the restaurant is open
    def rest_open(self):
        print(f"{self.rest_name} is open for customers.\n")


# Create restaurant objects
restaurant1 = Restaurant("Dominos", "pizza")
restaurant2 = Restaurant("smashed burger", "burgers")
restaurant3 = Restaurant("chick fila", "chicken sandwich")


# Display restaurant information
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()