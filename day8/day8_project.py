import string
import random
alphabet = list(string.ascii_lowercase)

def encrypt(original_text, shift_amount):
  cipher_text = ""
  for letter in original_text:
    shifted_position = alphabet.index(letter) + shift_amount
    if shifted_position > 26:
      shifted_position = shifted_position % 26
      cipher_text += alphabet[shifted_position]
    else:
      cipher_text += alphabet[shifted_position]
  return cipher_text
def decode(encoded_text, shift_amount):
  if shift_amount > 26:
    shift_amount = shift_amount % 26
  decoded_text = "" 
  for letter in encoded_text:
    shifted_position = alphabet.index(letter) - shift_amount
    if shifted_position < 0:
      shifted_position = 26 - abs(shifted_position)
      decoded_text += alphabet[shifted_position]
    else:
      decoded_text += alphabet[shifted_position]
  return decoded_text

game_is_on = True

while game_is_on:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'encode':
    
    print(encrypt(text,shift))
    ask = input('Do you want to start again? : yes/no   ')
    if ask == 'no':
      game_is_on = False
  elif direction == "decode":
    print(decode(text, shift))
    ask = input('Do you want to start again? : yes/no   ')
    if ask == 'no':
      game_is_on = False

