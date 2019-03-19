
numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers [0] will select the first index which is '3'
# numbers[-1] will select the last index of a list which is '2'
# numbers[3] will select the third index, since we start at 0 it will show '1'
# numbers[:-1] will show a list of values up to the 5th value.
# numbers [3:4] will show '1'
# 5 in numbers will check if the number 5 is in the list, which is it therefore will return True.
# 7 in numbers isn't in the list so will return False
# "3" in numbers will also return False as its an int in the list not a string.
# numbers + [6,5,3] will add it to the list but will not change our original list as its not appending these numbers.

# Making the first element of the list 10.
numbers[0] = 'ten'
# making the last element 1
numbers[-1] = 1
# Get all elements except the first 2
numbers[2:]
# checking if 9 is in the list//returns False
9 in numbers


