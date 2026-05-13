import random
import math
import statistics

# Starting values
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)

# Sample calculations
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# 200 value calculations
choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)

# Circle area
area = math.pi * radius * 2

print("Experimenting with a subset of integers 1-100:")
print("Sum:", sample_sum)
print("Average:", sample_avg)
print("Median:", sample_median)

print()

print("Experimenting with a superset of 200 values, integers 1-100:")
print("Average:", choices_avg)
print("Median:", choices_median)
print("Mode:", choices_mode)

print()

print("Modeling = random circle:")
print("Radius =", radius)
print("Area rounded up =", math.ceil(area))
print("Area rounded down =", math.floor(area))