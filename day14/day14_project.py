import random
import art
import game_data

print(art.logo)

score = 0
is_game_end = False
random_a = random.choice(game_data.data)
random_b = random.choice(game_data.data)
while not is_game_end:
  print(f"Compare A: {random_a['name']}, {random_a['description']}, from {random_a["country"]}")
  print(art.vs)
  print(f"Against B: {random_b['name']}, {random_b['description']}, from {random_b["country"]}")
  choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
  if choice == 'a':
    if random_a["follower_count"] > random_b['follower_count']:
      score += 1
      print(f'You are right! Current score {score}')
      random_b = random.choice(game_data.data)
    elif random_a['follower_count'] < random_b['follower_count']:
      print("You Lost!")
      is_game_end = True
      break
    elif random_a["follower_count"] == random_b['follower_count']:
      print('Its draw!')
      random_b = random.choice(game_data.data)
    
  elif choice == 'b':
    if random_b['follower_count'] > random_a['follower_count']:
      score += 1
      print(f'You are right! Current score {score}')
      random_a = random_b
      random_b = random.choice(game_data.data)
    elif random_b['follower_count'] < random_a['follower_count']:
      print('You lost!')
      is_game_end = True
      break
    elif random_a["follower_count"] == random_b['follower_count']:
      print('Its draw!')
      random_a = random_b
      random_b = random.choice(game_data.data)