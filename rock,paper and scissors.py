import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

while True:
    # Get user's choice
    user_choice = input("Enter your choice (rock/paper/scissors or 'exit' to quit): ").lower()
    
    if user_choice == "exit":
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    print("-" * 30)
