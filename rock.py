import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle the button click
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    
    # Get the computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Update the labels with the results
    result_label.config(text=f"Computer chose: {computer_choice}")
    outcome_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create labels to display the result
result_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14))
result_label.pack(pady=10)

outcome_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
outcome_label.pack(pady=10)

# Create buttons for user choice
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), width=15, command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), width=15, command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), width=15, command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Run the GUI main loop
root.mainloop()
