import random

def check(player, computer):
    if player == "rock" and computer == "scissors":
        return True
    elif player == "rock" and computer == "paper":
        return False
    elif player == "rock" and computer == "rock":
        return False
    elif player == "paper" and computer == "scissors":
        return False
    elif player == "paper" and computer == "paper":
        return False
    elif player == "paper" and computer == "rock":
        return True
    elif player == "scissors" and computer == "scissors":
        return False
    elif player == "scissors" and computer == "paper":
        return True
    elif player == "scissors" and computer == "rock":
        return False

def game():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    userInput = input("What would you like to play? (1,2,3) ")
    userChoice = ""
    try:
        userInput = int(userInput)
    except TypeError:
        print("You did not give a valid input")
        game()

    computer_choice = random.randint(0,2)
    computer_choices = ["rock", "paper", "scissors"]

    computer_sign = computer_choices[computer_choice]

    if userInput == 1:
        userChoice = "rock"
    elif userInput == 2:
        userChoice = "paper"
    elif userChoice == 3:
        userChoice == "scissors"
    
    victory = check(userChoice, computer_sign)

    if victory:
        print("You win! The computer chose " + computer_sign)
    else:
        print("You lost, the computer chose " + computer_sign)
    
    again = input("Play again? (Yes, No) ")

    if again == "Yes":
        game()
    else:
        print("Goodbye")
    
game()
