import random

print("Welcome to Rock, Paper, Scissors! First to 3 wins is the champion!")

options = ['rock', 'paper', 'scissors']

user_wins = 0
computer_wins = 0
ties = 0

while True:
    
    user_input = input("Type rock, paper or scissors to play (or 'quit' to stop): ").lower()
    if user_input == 'quit':
        break
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    computer_choice = options[random.randint(0,2)]
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

    if user_wins == 3:
      print("Overall, you are the champion!")
      break
    elif computer_wins == 3:
      print("Overall, the computer is the champion!")
      break

print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Ties: {ties}")


