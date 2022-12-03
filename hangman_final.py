import random
from hangman_art import *
from hangman_words import word_list

# Hangman logo
print(logo)
# Choosing a random word from word_list
chosen_word = random.choice(word_list)

# # Testing code
# print(f"testing!, the solution is {chosen_word}. ")
# Creating blanks('_')
display = []
for letter in range(len(chosen_word)):
    display += "_"
# Printing initial display
print(f"{' '.join(display)}\n")
# print("\n")
# Game over variable
end_of_game = False
# User number of lives
lives = 6

while not end_of_game:
    # User guess
    guess = input("Guess a letter: ").lower()
    print("\n")
    # Check if guess is entered already
    if guess in display:
        print(f"You've guessed '{guess}' already!")
        print("\n")

    # Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    # Guess not in chosen_word message and penalization
    if not guess in chosen_word:
        print(f"You guessed '{guess}' and it's not in the word")
        print("\n")
        lives -= 1
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}") 

    # Game over over conditions
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print("\n")
        print("You lose.")

    # Penalization image    
    if lives < 6:
        print(stages[lives])
