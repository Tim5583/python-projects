max_number = int(input("What is the range > 1 to : "))


def computer_guess(min, max):
    middle_number = int((max-min) / 2)
    return middle_number


def display_answer(answer):
        print(f"Is that number {answer}")
        user_answer = (input("Is that currect? ")).lower()
        return user_answer


def guess_my_number(x):
    won = False
    max = x
    low = 1
    inputs = {
        "l" : "Low",
        "h" : "high",
        "c" : "Currect"
    }

    while not won: 
        computers_guess = computer_guess(low, max)
        user_answer = display_answer(computers_guess)
        if user_answer == "c":
            won = True
            print("Yeeee!!! I won")
            return
        elif user_answer == "h":
            min = computers_guess

        



guess_my_number(max_number)
