pay_rate = 17.30
hours_worked = 45
filing_status = "single"

# Gross pay
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else :
    gross_pay = (40 * pay_rate) + ((hours_worked - 40) * pay_rate * 1.5)

# Annual income
annual_income = gross_pay * 52

# Tax rate
if filing_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

# Tax and net pay
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# Results
print(f"You worked {hours_worked} hours.")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")