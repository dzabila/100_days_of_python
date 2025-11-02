import blackjack
import random

print(blackjack.logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_cards = []
player_cards = []
def deal_cards(cards_list, where_to_deal):
  for i in range(2):
    where_to_deal.append(random.choice(cards_list))
deal_cards(cards,player_cards)
deal_cards(cards,computer_cards)
print(f"Computer card is {computer_cards[0]}, Your cards are {player_cards}")
sum_player = sum(player_cards)
sum_computer = sum(computer_cards)
is_game_end = False
def check_for_blackjack():
  if sum_player == 21:
    winner = "player"
    return winner
  elif sum_computer == 21:
    winner = "computer"
    return winner
if check_for_blackjack() == "computer" or check_for_blackjack() == "player":
  if check_for_blackjack() == "computer" and check_for_blackjack() == "player":
    print('Draw You Both Have Blackjack')
    is_game_end = True
  else:
    print(f"{check_for_blackjack()} Wins With BlackJack!")
    is_game_end = True
def check_for_ace(cards_list):
  ace = 11
  if (sum(cards_list) + 11) > 21:
    ace = 1
  else:
    ace = 11
  return ace


while not is_game_end:
  ask_user = input('Do you want to deal another card? y/n : ').lower()
  while ask_user == "y":
    random_card = random.choice(cards)
    if random_card == 11:
      random_card = check_for_ace(player_cards)
      player_cards.append(random_card)
      print(f"{player_cards} Sum = {sum(player_cards)}")
      ask_user = input('Do you want to deal another card? y/n : ').lower()
    else:
      player_cards.append(random_card)
      if sum(player_cards) > 21:
        print(f'You burnt with {player_cards} sum = {sum(player_cards)}')
        is_game_end = True
        break
      else:
        print(f'Your cards: {player_cards} sum = {sum(player_cards)}')
        ask_user = input('Do you want to deal another card? y/n : ').lower()
  while sum(computer_cards) < 17:
    random_card = random.choice(cards)
    if random_card == 11:
      random_card = check_for_ace(computer_cards)
      computer_cards.append(random_card)
      print(f"{computer_cards} Sum = {sum(computer_cards)}")
    else:
      computer_cards.append(random_card)
      if sum(computer_cards) > 21:
        print(f'Computer burnt with {computer_cards} sum = {sum(computer_cards)}')
        is_game_end = True
        break
      else:
        print(f"Computer cards {computer_cards} sum = {sum(computer_cards)}")
  if not is_game_end:
    if sum(player_cards) > sum(computer_cards):
      print(f'Player won with cards {player_cards}, Sum = {sum(player_cards)}')
      is_game_end = True
    elif sum(player_cards) < sum(computer_cards):
      print(f'Computer Won with cards {computer_cards}, Sum = {sum(computer_cards)}')
      is_game_end = True
    elif sum(player_cards) == sum(computer_cards):
      print(f'It is Draw! Your Cards: {player_cards}, Computer cards: {computer_cards}')
      is_game_end = True