🔁 1. For Loop – განმარტება და სინტაქსი

for loop გამოიყენება, როცა გვინდა მოვახდინოთ გამეორება (iteration) ელემენტებზე — მაგალითად სიაში, სტრიქონში ან სხვა კოლექციაში.

📘 სინტაქსი:

for element in sequence:
    # იმოქმედე ყოველი ელემენტისთვის


🔹 element — ცვლადი, რომელიც იღებს თითოეულ მნიშვნელობას
🔹 sequence — მონაცემთა კოლექცია (მაგ. list, string, tuple, range და სხვ.)

📘 მაგალითი:

for letter in "Python":
    print(letter)


👉 გამოიტანს:

P
y
t
h
o
n

📋 2. Using for loop on Lists

სიის გადავლა ციკლით საშუალებას გვაძლევს ვიმუშაოთ თითოეულ ელემენტზე.

✅ ელემენტების ბეჭდვა:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


👉 შედეგი:

apple
banana
cherry

✅ ელემენტების დამუშავება:
numbers = [1, 2, 3, 4]
for n in numbers:
    print(n * 2)


👉 შედეგი:

2
4
6
8

✅ ინდექსით წვდომა (enumerate):
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)


👉 შედეგი:

0 red
1 green
2 blue

✅ სიაში ახალი ელემენტების შექმნა ციკლით:
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)


👉 შედეგი: [1, 4, 9, 16]

🔢 3. For Loop with range() Function

range() ქმნის რიცხვების მიმდევრობას, რომლის მეშვეობითაც შეგვიძლია ციკლის რაოდენობის კონტროლი.

📘 სინტაქსი:

range(start, stop, step)

პარამეტრი	აღწერა	მაგალითი
start	საიდან იწყოს	range(2, 10) → იწყებს 2-იდან
stop	სადამდე (არ ჩათვლით)	range(2, 10) → ჩერდება 9-ზე
step	ნაბიჯი	range(1, 10, 2) → 1, 3, 5, 7, 9
✅ მაგალითი 1 – უბრალო ციკლი:
for i in range(5):
    print(i)


👉 შედეგი:

0
1
2
3
4

✅ მაგალითი 2 – დაწყების და დასრულების მითითებით:
for i in range(2, 7):
    print(i)


👉 შედეგი:

2
3
4
5
6

✅ მაგალითი 3 – ნაბიჯით ციკლი:
for i in range(0, 10, 2):
    print(i)


👉 შედეგი:

0
2
4
6
8

✅ range და სიასთან ერთად:
nums = [10, 20, 30, 40]

for i in range(len(nums)):
    print(i, nums[i])


👉 შედეგი:

0 10
1 20
2 30
3 40

🧠 შეჯამება:
თემა	მთავარი აზრი
for loop	იმეორებს კოდს თითოეული ელემენტისთვის
for loop on list	გადადის სიაში ელემენტიდან ელემენტზე
for loop + range()	იმეორებს კოდს განსაზღვრული რაოდენობისჯერ