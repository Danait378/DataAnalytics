import math

tourists = 38

van_capacity = 15
van_cost = 250

vans_needed = (tourists // van_capacity)

total_cost = vans_needed * van_cost

cost_per_person = total_cost / tourists

print("i need" , vans_needed, "vans")
print("total cost is $", total_cost)
print("the cost per person is $", round(cost_per_person, 2))