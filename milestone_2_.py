import random

# Assigning the fruits to a variable
word_list = ["apple", "banana", "grapes", "orange", "mango"]

#Random word assignment
word = random.choice(word_list)

# Creating input button and assigned variable to guess
guess = input(f"Enter a single letter: ")
# if and else statements to ensure one letter is passed through

if guess.isalpha() and len(guess) == 1:
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")