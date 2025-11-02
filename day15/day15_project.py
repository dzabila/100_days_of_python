import data
resources = data.resources
menu = data.MENU
ask_customer = input("What would you like? (espresso/latte/cappuccino)  ")
def check_sufficent(drink):
  for key,value in drink.items():
    if value > data.resources[key]:
      print(f'Sorry there is not enough {key}')
      return False
  return True
    
def get_coins():
  print('Please insert coins.')
  sum = 0
  quarters = int(input('How many quarters? :  ')) * 0.25
  dimes = int(input('How many dimes? :   ')) * 0.1
  nickles = int(input('How many nickles?  :')) * 0.05
  pennies = int(input('How many pennies? :'))* 0.01
  sum = sum + quarters + dimes + nickles + pennies
  return sum

def make_drink(drink):
  for key,value in menu[drink]['ingredients'].items():
    resources[key] -= value
  resources['money'] += menu[drink]['cost']
  print(f'Take your {drink}')
while ask_customer != "off":
  if ask_customer == "report":
    for key,value in resources.items():
      print(f"{key} : {value}")
    # ask_customer = input("What would you like? (espresso/latte/cappuccino)  ")
  elif ask_customer == 'espresso':
    if check_sufficent(menu['espresso']['ingredients']) == True:
      coins = get_coins()
      if coins < menu['espresso']['cost']:
        print(f'Sorry that is not enough money. Money refunded: {coins}')
      elif coins == menu['espresso']['cost']:
        make_drink('espresso')
      elif coins > menu['espresso']['cost']:
        print(f'Take your change {round(coins - menu['espresso']['cost'],2)}') 
        make_drink('espresso')
  elif ask_customer == 'latte':
    if check_sufficent(menu['latte']['ingredients']) == True:
      coins = get_coins()
      if coins < menu['latte']['cost']:
        print(f'Sorry that is not enough money, Money refunded: {coins}')
      elif coins == menu['latte']['cost']:
        make_drink('latte')
      elif coins > menu['latte']['cost']:
        print(f'Take your change {round(coins - menu['latte']['cost'],2)}')
        make_drink('latte')
  elif ask_customer == 'cappuccino':
    if check_sufficent(menu['cappuccino']['ingredients']) == True:
      coins = get_coins()
      if coins < menu['cappuccino']['cost']:
        print(f'Sorry that is not enough money. Money refunded: {coins}')
      elif coins == menu['cappuccino']['cost']:
        make_drink('cappuccino')
      elif coins > menu['cappuccino']['cost']:
        print(f'Take your change {round(coins - menu['cappuccino']['cost'],2)}')
        make_drink('cappuccino')
  ask_customer = input("What would you like? (espresso/latte/cappuccino)  ")