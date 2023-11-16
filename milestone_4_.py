import random

# Assigning the fruits to a variable
word_list = ["apple", "banana", "grapes", "orange", "mango"]

#Random word assignment
word = random.choice(word_list)


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        
        for index, letter in enumerate(self.word[0]):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {num_lives} lives left.")
        
    def ask_for_input(self):
        while True:
            guess = input(f"Enter a single letter: ")
            if guess != guess.isalpha() and len(guess) != 1:
                 print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in (self.list_of_guesses):
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hang_1 = Hangman(word_list)
hang_1.ask_for_input()