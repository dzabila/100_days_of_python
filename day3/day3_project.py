# treasure island

print('Welcome to Treasure Island. Your mission is to find the treasure.')
usr_input = input('Enter which side you want to go?  Left/Right  :')

if usr_input == 'left':
  usr_input = input('Swim or Wait? type swim/wait  :')
  if usr_input == 'swim':
    print('game over')
  else:
    usr_input = input('Choose door,  blue/yellow/red   ')
    if usr_input == 'blue':
      print('game over')
    elif usr_input == 'red':
      print('game over')
    elif usr_input == 'yellow':
      print('You win')
    else:
      print('Wrong input')
else:
  print('Game over')