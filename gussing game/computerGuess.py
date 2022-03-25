print("Welcome to the Guessing Game; First, how does this work? First, you give the range and you think of one number in that range. (0 - your number)\n")
print("How to play")
print("if number is low you enter > 'l'")
print("if number is high you enter > 'h'")
print("if i guess the correct you enter > 'c'")


def computer_guess(min, max):
    middle_number = int(round((min + max) / 2, 0))
    return middle_number


def display_answer(answer):
        print(f"Is that number {answer}")
        user_answer = (input("Is that currect? ")).lower()
        return user_answer


def guess_my_number(x):
    won = False
    max = x
    min = 0

    computers_guess = computer_guess(min, max)
    user_answer = display_answer(computers_guess)

    while not won: 
        if user_answer == "c":
            won = True
            print("Yeeee!!! I won")
            return
        elif user_answer == "h":
            print('"OOPs!"\n')
            min = computers_guess - 1
            computers_guess = computer_guess(min, max)
            user_answer = display_answer(computers_guess)
        elif user_answer == "l":
            print('"OPPs!"\n')
            max = computers_guess + 1
            computers_guess = computer_guess(min, max)
            user_answer = display_answer(computers_guess)
        else:
            print("I don't undestand! did you read the instructions??")

        
try:
    max_number = int(input("What is the range > 0 to : "))
    guess_my_number(max_number)
except:
    print("Enter a Valid Input")
