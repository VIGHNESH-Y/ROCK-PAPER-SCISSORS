import random


user_profiles = {}

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name} ({self.score} points)"

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Advanced Rock, Paper, Scissors!")
    player_name = input("Enter your name: ")
    
    if player_name not in user_profiles:
        user_profiles[player_name] = Player(player_name)
    
    player = user_profiles[player_name]
    computer = Player("Computer")
    
    rounds = int(input("How many rounds would you like to play? "))
    tied_rounds = 0
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"{player.name} chose {user_choice}. {computer.name} chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            player.score += 1
        elif result == "Computer wins!":
            computer.score += 1
        else:
            tied_rounds += 1
    
    print(f"Round score - {player.name}: {player.score}, {computer.name}: {computer.score}, Tied Rounds: {tied_rounds}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
