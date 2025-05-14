program:
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user == "exit":
            break
        if user not in choices:
            print("Invalid input")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()
