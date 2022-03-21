import random;

def gussing(max_number):
    guess = 0
    computer_guess = random.randint(1, max_number)

    while guess != computer_guess:
        try: 
            guess = int(input(f"Enter your guess between {1} and {max_number}: "))
            if guess > computer_guess:
                print("Too High Try Again")
            elif guess < computer_guess:
                print("Too low Try Again")
            else:
                print(f"congratulation you have guessed the number {computer_guess} correctly!")
        except:
            print("Enter a Number")

gussing(10)