import string
import random
a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase)
alphabet = a + b
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!',"#","$",'%',"&","(",")","*","+"]

print('Welcome to PyPassword generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many symbols would you like?\n'))
nr_symbols = int(input('How many numbers would you like?\n'))

password = ""
for letter in range(nr_letters):
  password += random.choice(alphabet)

for number in range(nr_numbers):
  password += random.choice(numbers)

for symbol in range(nr_symbols):
  password += random.choice(symbols)

print(f'Password is {password}')




# hard version

hard_password = []
for i in range(nr_letters):
  hard_password.append(random.choice(alphabet))
for i in range(nr_numbers):
  hard_password.append(random.choice(numbers))
for i in range(nr_symbols):
  hard_password.append(random.choice(symbols))

hard_password_as_text = "" 

for i in range(len(hard_password)):
  rand_choice = random.choice(hard_password)
  hard_password_as_text += rand_choice
  hard_password.remove(rand_choice)

print(hard_password_as_text)