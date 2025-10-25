#Hangman game
import random


word_list = ['aardvark', 'baboon', 'camel']
random_word = random.choice(word_list)
placeholder = ""
guess = []
for i in range(len(random_word)):
  placeholder += '_'
  guess.append('_')
print(placeholder)
print(guess)
lives = 6

while lives > 0 and "".join(guess) != random_word:
  usr_input = input('Enter Letter here: ').lower() 
  for i in range(len(random_word)):
    if random_word[i] == usr_input:
      guess[i] = usr_input
  if usr_input not in random_word:
    print(f"{usr_input} not in word")
    lives -= 1
    print(f"You have {lives} lives left")
  print(''.join(guess))
if lives == 0:
  print(f'Game Over lives left {lives}')
if "".join(guess) == random_word:
  print(f"You guessed word - {random_word}")