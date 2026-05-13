import random
products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# Product of the Day
product_day = random.choice(products)
print("Product of the Day:", product_day)

# 3 products for survey
survey_products =  random.sample(products, 3)
print("Survey Products:", survey_products)

# Shuffle product list
random.shuffle(products)
print("Shuffled Products:", products)

# Random transaction count
transactions = random.randint(50, 300)
print("Daily Transactions:", transactions)