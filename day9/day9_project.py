import art
players = {}


name = input('Enter Your Name Here:  ')
price = int(input('Enter Your price Here:  '))


def add_to_players(name,price):
  players[name] = price

add_to_players(name,price)

game_is_on = True
while game_is_on:
  ask = input('Are there any onter byders? type y/n  : ').lower()
  if ask == 'y':
    name = input('Enter Your Name Here:  ')
    price = int(input('Enter Your price Here:  '))
    add_to_players(name,price)
  else:
    game_is_on = False


values = []
names = []
for key,value in players.items():
  values.append(value)
  names.append(key)

highest = max(values)
highest_name = names[values.index(highest)]

print(f'Auction winner is {highest_name} with {highest}$ bid!')