from words import words
import random

def random_word():
    word = random.choice(words)
    while "-" in word:
        word = random.choice(words)
    return word.upper()


def handman():
    # get random word
    print("Welcome to Hangman")
    print("""

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    
    """)
    chosen_word = random_word()
    chosen_word_letters = set(chosen_word)
    lives = 6
    users_letters = []

    while len(chosen_word_letters) != 0 and lives > 0:
        print(f"You have used these letters: {users_letters}")
        print(f"You have {lives} lives left\n")
        print("Word >> "+"".join([f" {letter} " if letter in users_letters else " # " for letter in chosen_word]))
        user_guess_letter = (input("Guess a letter: ")).upper()
        users_letters.append(user_guess_letter)

        if user_guess_letter in chosen_word_letters:
            chosen_word_letters.discard(user_guess_letter)
        elif user_guess_letter in users_letters:
            print(f"You already guesed letter: ''{user_guess_letter}''")
            lives -= 1
        else: 
            print("got got wrong")
            lives -= 1

    if len(chosen_word_letters) == 0 and lives > 0:
        print(f"Congratulation! You guess the word ''{chosen_word}'' correctly")
    if lives == 0:
        print(f"Sorry! You Died, The word was {chosen_word}")

handman()
