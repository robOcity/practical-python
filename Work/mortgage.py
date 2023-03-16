# mortgage.py
#
# Exercise 1.9 extra month payment calculator
# Exercise 1.10 now extra payments can be made for any period and amount

principle = 500000.0
rate = 0.05
nominal_payment = 2684.11
extra_payment = 1000
extra_payment_month_start = 61
extra_payment_month_end = 108
total_paid = 0.0
months = 0

while principle > 0:
    payment = nominal_payment
    if months >= extra_payment_month_start and months <= extra_payment_month_end:
        payment = nominal_payment + extra_payment
    total_paid += payment
    principle = principle * (1 + rate / 12) - payment
    months = months + 1
    if principle < 0:
        total_paid += principle
        principle = 0
    print(f"{months:6d}  {total_paid:12,.2f}  {principle:10,.2f}")

print(f"\nTotal paid of ${total_paid:,.2f} over months {months}")
