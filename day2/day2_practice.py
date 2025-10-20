
print('Hello'[4])

len('12345')

print(type('abc'))


print(type(123))
print(type('string'))
print(type(3.14))
print(type(True))

int('123')

print('Number of letters in your name: ' + len(str(input('Enter your name : '))))

# number manipulation and f strings

bmi = 84 / 1.65 ** 2
print(bmi)

print(round(bmi))
print(round(bmi, 2))

score = 0
height = 1.8
is_winning = True
print(f'Your score is {score} your height is {height} and you are winning = {is_winning}')