
# I understood the task as creating a dictionary and then getting a user to enter a sentence to count the amount of
# times that it occured in your dictionary. Taking a look at the solution I noticed it was different.
dictionary = {"a": 0, "be": 0, "car": 0, "drive": 0, "cat": 0, "fun": 0, "dog": 0, "alpha": 0,
              "kitty": 0, "love": 0, "meme": 0, "review": 0, "subscribe": 0, "youtube": 0}

# user_string = input("Please enter a sentence: ")
user_string = " a be car drive a be car drive a be car drive a be car drive a be car drive a be car drive subscribe"
# split the string so each word is it only value in the list.
words = user_string.split()

for words in words:
    if words in dictionary:
        dictionary[words] += 1
    else:
        pass
# I noticed in the solution that if I created the dictionary by storing the user values then the below code would work.
# Since I made the dictionary and compared it to the sentence I can set a max value for it to line up.
# max_length = max(len(words) for user_string in words)
for word, value in dictionary.items():
    print("{:{}} = {}".format(word, 9, value))
