import random


NUMBERS_IN_LINE = 6
MIN = 1
MAX = 45

quick_picks = int(input("How many Quick Picks would you like? "))
while quick_picks < 0:
    print("You can't have negative picks sir. Try again")
    quick_picks = int(input("How many Quick Picks would you like? "))

numbers = []
for j in range(quick_picks):
    for i in range(NUMBERS_IN_LINE):
        numbers.append(random.randrange(MIN, MAX))
        i += 1

numbers.sort()
print(numbers)


