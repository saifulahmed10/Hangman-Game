import random

# Assigning the fruits to a variable
word_list = ["apple", "banana", "grapes", "orange", "mango"]

#Random word assignment
word = random.choice(word_list)

# Creating input button and assigned variable to guess
guess = input(f"Enter a single letter: ")
# if and else statements to ensure one letter is passed through

while guess:
  if guess.isalpha() and len(guess) == 1 and guess.alpha() == word:
    print("Good guess!")
    guess = input(f"Enter a single letter: ")
  else:
    print("Oops! That is not a valid input.")
    guess = input(f"Enter a single letter: ")

# function that checks guess

def check_guess(guess):
  guess.lower()
  if guess.isalpha() and len(guess) == 1 and guess in word:
    print(f"Good guess! {guess} is in the word")
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

#ask for input function

def ask_for_input():
  while True:
    guess = input(f"Enter a single letter: ")
    if guess.isalpha() and len(guess) == 1:
      print("Good guess!")
    else:
      print("Oops! That is not a valid input.")
  check_guess(guess)
ask_for_input()