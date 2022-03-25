import random 

def playgame():
    print("'r' for rock\n'p' for paper\n's' for scissors\n")
    except_inputs = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    user_input = ""
    while not user_input in except_inputs.keys():
        user_input = (input("What's your choice?  ")).lower()

    computer_choice = random.choice(["r", "p", "s"])
    print(f"you Choose {except_inputs[user_input]} and computer Choose {except_inputs[computer_choice]}")
    if user_input == computer_choice:
        print("tie!")
        return 
    
    if (user_input == "r" and computer_choice == "s") or (user_input == "p" and computer_choice == "r") or (user_input == "s" and computer_choice == "p"):
        print("You won!")
        return 

    print("You lost!")

playgame()