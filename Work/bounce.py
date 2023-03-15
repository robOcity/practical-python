# bounce.py
#
# Exercise 1.5
BOUNCE_PER_DROP = 3 / 5

height = 100
for i in range(1, 11):
    height *= BOUNCE_PER_DROP
    print(i, round(height, 4))
