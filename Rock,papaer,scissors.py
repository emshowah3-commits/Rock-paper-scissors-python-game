import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("The computer wins!")
    elif player == "scissors" and computer  == "paper":
        print("You win!")
    else:
        print("The computer wins!")

    play_again = input("play again? (y/n): ").lower
    if not play_again == "y":
        running = False