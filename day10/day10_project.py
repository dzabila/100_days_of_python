import calculator

print(calculator.calculator_art)

number_one = float(input("What's the first number?: "))
operation = input("+\n-\n*\n/\nchoose operation: ")
number_two = float(input("What's the second number?: "))


def add(n1,n2):
  return n1 + n2
def div(n1,n2):
  return n1 / n2
def mult(n1,n2):
  return n1 * n2
def sub(n1,n2):
  return n1 - n2
def calculation(num1,num2,operation):
  if operation == '+':
    return add(num1,num2)
  elif operation == "-":
    return sub(num1,num2)
  elif operation == "*":
    return mult(num1,num2)
  elif operation == '/':
    return div(num1,num2)

result = calculation(number_one,number_two,operation)
print(result)
ask = input(f'Do you want to continue with {result} or start again? y for continue / n for starting again  : ')
while True:
  if ask == 'y':
    number_one = result
    operation = input("+\n-\n*\n/\nchoose operation: ")
    number_two = float(input("What's the second number?: "))
    result = calculation(number_one,number_two,operation)
    print(result)
    ask = input(f'Do you want to continue with {result} or start again? y for continue / n for starting again  : ')
  elif ask == 'n':
    result = 0
    print(calculator.calculator_art)
    number_one = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nchoose operation: ")
    number_two = float(input("What's the second number?: "))
    result = calculation(number_one,number_two,operation)
    print(result)
    ask = input(f'Do you want to continue with {result} or start again? y for continue / n for starting again  : ')



  