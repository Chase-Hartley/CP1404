import random


NUMBERS_IN_LINE = 6
MIN = 1
MAX = 45

quick_picks = int(input("How many Quick Picks would you like? "))
while quick_picks < 0:
    print("You can't have negative picks sir. Try again")
    quick_picks = int(input("How many Quick Picks would you like? "))

print("You have chosen {} quick picks Good Luck! \n ----------------------------------".format(quick_picks))

for j in range(quick_picks):
    numbers = []
    for i in range(NUMBERS_IN_LINE):
        random_num = random.randint(MIN, MAX)
        while random_num in numbers:
            random_num = random.randint(MIN, MAX)
        numbers.append(random_num)
    numbers.sort()
    print(numbers)




