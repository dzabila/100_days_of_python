import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)
lives = 0
difficulity = input("Choose difficulity: easy/hard :").lower()
if difficulity == "easy":
  lives = 10
elif difficulity == "hard":
  lives = 5
else:
  print("invalid input")

is_game_end = False
while not is_game_end:
  print(f"You have {lives} lives")
  ask_user = int(input('Guess The Number:'))
  if ask_user == random_number:
    print('You guessed correctly')
    is_game_end = True
  else:
    lives -= 1
    if lives == 0:
      print('You have no lives left! You lost!')
      is_game_end = True
    else:
      if ask_user < random_number:
        print('Number is Too low')
      else:
        print('Number is too High')