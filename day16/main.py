from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
# menuitem = MenuItem()
coffemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True
while is_on:
  ask_customer = input(f'What coffe do you want? {menu.get_items()}  :  ')
  if ask_customer == 'off':
    is_on = False
  elif ask_customer == 'report':
    coffemaker.report()
    moneymachine.report()
  else:
    drink = menu.find_drink(ask_customer)
    if coffemaker.is_resource_sufficient(drink) == True:
      if moneymachine.make_payment(drink.cost) == True:
        coffemaker.make_coffee(drink)
  
