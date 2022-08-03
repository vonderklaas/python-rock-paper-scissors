import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
  user_input = input('Rock / Paper / Scissors or Q to quit: ').lower()
  if user_input == 'q':
    break

  if user_input not in options:
    print('Please enter a correct value!')
    continue

  # Computer's choices:
  # 0 - rock
  # 1 - paper
  # 2 - scissors
  random_number = random.randint(0, 2)
  computer_choice = options[random_number]
  print(f'Computer picked: {computer_choice}')

  # Determine winner
  if user_input == 'rock' and computer_choice == 'scissors':
    print('You won!')
    user_wins += 1
  elif user_input == 'paper' and computer_choice == 'rock':
    print('You won!')
    user_wins += 1
  elif user_input == 'scissors' and computer_choice == 'rock':
    print('You won!')
    user_wins += 1
  elif user_input == computer_choice:
    print('Tie!')
  else:
    print('Computer won!')
    computer_wins += 1

print(f'You won {user_wins} times')
print(f'Computer won {computer_wins} times')
print('Thanks, have a nice day!')