#Rock paper scossors game
import game_ascii
import random
player_choice = int(input(('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors : ')))


computer_choice = random.randint(0,2)


if player_choice == 0:
  if computer_choice == 0:
    print(f"Computer choose : {game_ascii.rock}")
    print(f"Player choose :{game_ascii.rock}")
    print('TIE!')
  elif computer_choice == 1:
    print(f"Computer chooce : {game_ascii.paper}")
    print(f"Player choose : {game_ascii.rock}")
    print('computer wins')
  elif computer_choice == 2:
    print(f"Computer chooce : {game_ascii.scissors}")
    print(f"Player choose : {game_ascii.rock}")
    print('player wins')
  else:
    print('Invalid input!')
elif player_choice == 1:
  if computer_choice == 0:
    print(f"Computer choose : {game_ascii.rock}")
    print(f"Player choose :{game_ascii.paper}")
    print('Player wins')
  elif computer_choice == 1:
    print(f"Computer chooce : {game_ascii.paper}")
    print(f"Player choose : {game_ascii.paper}")
    print('TIE!')
  elif computer_choice == 2:
    print(f"Computer chooce : {game_ascii.scissors}")
    print(f"Player choose : {game_ascii.paper}")
    print('Computer wins')
  else:
    print('Invalid input!')
elif player_choice == 2:
  if computer_choice == 0:
    print(f"Computer choose : {game_ascii.rock}")
    print(f"Player choose :{game_ascii.scissors}")
    print('Computer wins')
  elif computer_choice == 1:
    print(f"Computer chooce : {game_ascii.paper}")
    print(f"Player choose : {game_ascii.scissors}")
    print('Player wins')
  elif computer_choice == 2:
    print(f"Computer chooce : {game_ascii.scissors}")
    print(f"Player choose : {game_ascii.scissors}")
    print('Tie')
  else:
    print('Invalid input!')