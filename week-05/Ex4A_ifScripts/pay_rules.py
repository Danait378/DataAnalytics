# Pay information
pay_rate = 17.30
hours_worked = 45

# Regular hours
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked

# Overtime hour
else:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay

# Result
print(f"Gross pay is ${gross_pay:.2f}")