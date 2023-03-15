# mortgage.py
#
# Exercise 1.7

principle = 500000.0
rate = 0.05
nominal_payment = 2684.11
extra_payment = 1000
extra_payment_months = 12
total_paid = 0.0
months = 0

while principle > 0:
    payment = nominal_payment
    if months < 12:
        payment = nominal_payment + extra_payment
    total_paid += payment
    principle = principle * (1 + rate / 12) - payment
    months = months + 1

print(f"Total paid of ${total_paid:,.2f} over {months} months")
