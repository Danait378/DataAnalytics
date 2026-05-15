class Restaurant:
    '''This class creates a restaurant with a name, food type, customers served, and ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a scale of 1-5? ")

            if rating.isdigit():
                rating = int(rating)

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)
                    print(f"Your rating was {rating}. The average rating for this restaurant is {average:.1f}.")
                    break
                else:
                    print("Please enter a number from 1 to 5.")
            else:
                print("Please enter a whole number only.")


restaurant1 = Restaurant("Tasty Bites", "burgers")
restaurant2 = Restaurant("Pasta House", "Italian food")
restaurant3 = Restaurant("Sushi Spot", "sushi")


restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()
restaurant1.customer_rating()
restaurant1.customer_rating()


restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()
restaurant2.customer_rating()


restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.customer_rating()