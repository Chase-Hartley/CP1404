
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []
amount_of_numbers = 0
user_name = input("Please enter your username: ")

for amount_of_numbers in range(1, 6):
    user_number = int(input("Please enter number {}: ".format(amount_of_numbers)))
    numbers.append(user_number)
    amount_of_numbers += 1

if user_name in usernames:
    print("\n Access Granted")
else:
    print("\n Access Denied")

print("\n Interesting Things \n -----------------")
print("The first number is {} ".format(numbers[0]))
print("The last number is {} ".format(numbers[-1]))
print("The smallest number is {} ".format(min(numbers)))
print("The largest number is {} ".format(max(numbers)))
print("The average of your 5 numbers is {} ".format(sum(numbers) / 5))