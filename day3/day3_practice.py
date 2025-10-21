# control flow and logical operators

# height = int(input('What is your height in cm? '))

# if height > 120:
#   print('Can ride')
# else:
#   print('Can not ride')


# num = int(input('Enter number here: '))

# if num % 2 == 0:
#   print(f'{num} is even')
# else:
#   print(f"{num} is odd")



height = int(input('What is your height in cm?  '))
age = int(input('Enter your age here: '))
if height > 120:
  print('can ride')
  if age < 12:
    print('Price is $5')
    photo = input('Do you want to take photo? yes/no  :')
    if photo == 'yes':
      print('Total will be $8')
    else:
      print('Then price will be same')
  elif age > 45 and age < 55:
    print('Price will be $0')
  elif age > 18:
    print('Price is $12')
    photo = input('Do you want to take photo? yes/no  :')

    if photo == 'yes':
      print('Total will be $15')
    else:
      print('Then price will be same')
  else:
    print('Price is $7')
    photo = input('Do you want to take photo? yes/no  :')
    if photo == 'yes':
      print('Total will be $10')
    else:
      print('Then price will be same')
else:
  print('Can not ride')


# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M or L')
# pepperoni = input('Do you want pepperoni on your pizza?  Y or N : ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
# price = 0

# # price according to size
# if size == 's':
#   price += 15
#   if pepperoni == 'y':
#     price += 2
# elif size == 'm':
#   price += 20
#   if pepperoni == 'y':
#     price += 3
# elif size == 'l':
#   price += 25
#   if pepperoni == 'y':
#     price += 3

# if extra_cheese == 'y':
#   price += 1

# print(f'Your total will be ${price}')
# # price according to pepperoni

