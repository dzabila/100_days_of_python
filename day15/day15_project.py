import data
resources = data.resources
menu = data.MENU
ask_customer = input("What would you like? (espresso/latte/cappuccino)  ")
def check_sufficent(drink):
  for key,value in drink.items():
    if value > resources[key]:
      print(f'Sorry there is not enough {key}')
      return False
  return True
    
def get_coins():
  print('Please insert coins.')
  total = 0
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

def process_order(drink_name):
  if check_sufficent(menu[drink_name]['ingredients']) == True:
      coins = get_coins()
      if coins < menu[drink_name]['cost']:
        print(f'Sorry that is not enough money. Money refunded: {coins}')
      elif coins == menu[drink_name]['cost']:
        make_drink(drink_name)
      elif coins > menu[drink_name]['cost']:
        print(f"Take your change {round(coins - menu[drink_name]['cost'],2)}") 
        make_drink(drink_name)
while ask_customer != "off":
  if ask_customer == "report":
    for key,value in resources.items():
      print(f"{key} : {value}")
  elif ask_customer == 'espresso':
    process_order('espresso')
  elif ask_customer == 'latte':
    process_order('latte')
  elif ask_customer == 'cappuccino':
    process_order('cappuccino')
  else:
    print('Invalid input')
  ask_customer = input("What would you like? (espresso/latte/cappuccino)  ")