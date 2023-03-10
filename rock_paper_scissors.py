import random

# Prompt the user for their choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate the user's choice
while user_choice not in ['rock', 'paper', 'scissors']:
    user_choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()

# Generate a random choice for the computer
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Determine the winner of the game
if user_choice == computer_choice:
    result = 'tie'
elif user_choice == 'rock':
    if computer_choice == 'paper':
        result = 'computer'
    else:
        result = 'user'
elif user_choice == 'paper':
    if computer_choice == 'scissors':
        result = 'computer'
    else:
        result = 'user'
else:
    if computer_choice == 'rock':
        result = 'computer'
    else:
        result = 'user'

# Output the result of the game to the user
if result == 'tie':
    print(f"It's a tie! Both chose {user_choice}.")
elif result == 'user':
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {user_choice}.")
