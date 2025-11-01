🧩 1. Functions – რა არის ფუნქცია

ფუნქცია (Function) — ეს არის კოდის ბლოკი, რომელსაც ვწერთ ერთხელ და ვიძახებთ რამდენჯერმე, როცა გვჭირდება.

ფუნქცია:

ეხმარება კოდის გამეორების თავიდან აცილებას,

ზრდის კოდის წაკითხვადობას,

საშუალებას გაძლევს პრობლემები დაალაგო მცირე ნაწილებად.

📘 სინტაქსი:

def function_name():
    # შესასრულებელი კოდი


📗 მაგალითი:

def say_hello():
    print("Hello, world!")


📙 ფუნქციის გამოძახება:

say_hello()


👉 შედეგი:

Hello, world!

🧠 2. Functions with Inputs (პარამეტრებით)

ფუნქციას შეიძლება ჰქონდეს შეყვანის პარამეტრები (inputs / parameters), რომლებიც ფუნქციას მონაცემებს გადასცემენ.

📘 სინტაქსი:

def function_name(parameter1, parameter2):
    # გამოყენება


📗 მაგალითი:

def greet(name):
    print(f"Hello, {name}!")


გამოძახება:

greet("Nika")


👉 შედეგი:

Hello, Nika!

✅ რამდენიმე პარამეტრი:
def add(a, b):
    print(a + b)

add(3, 5)


👉 შედეგი:

8

✅ მნიშვნელობის დაბრუნება (return):

ფუნქცია შეიძლება აბრუნებდეს შედეგს return-ის მეშვეობით.

def multiply(x, y):
    return x * y

result = multiply(2, 4)
print(result)


👉 შედეგი:

8

⚙️ 3. Positional vs Keyword Arguments

ფუნქციას რომ ვიძახებთ, არგუმენტებს შეგვიძლია გადავცეთ ორ გზით:

🔹 Positional Arguments

(პოზიციის მიხედვით გადაცემული მნიშვნელობები)

მაგალითი:

def person_info(name, age):
    print(f"{name} is {age} years old.")

person_info("Nika", 25)   # positional


👉 შედეგი:

Nika is 25 years old.


➡️ აქ მნიშვნელობები მიეკუთვნება არგუმენტებს იმ თანმიმდევრობით, როგორც ფუნქციაშია განსაზღვრული.

🔸 Keyword Arguments

(გასაღების/სახელის მითითებით გადაცემული მნიშვნელობები)

person_info(age=25, name="Nika")  # keyword arguments


👉 შედეგი იგივე იქნება:

Nika is 25 years old.


➡️ Keyword არგუმენტებში თანმიმდევრობა არ არის მნიშვნელოვანი, რადგან სახელით გადაეცემა.

⚠️ შერეული გამოყენება (წესით):

შეიძლება ორივე ერთად გამოვიყენოთ, მაგრამ:

positional არგუმენტები ყოველთვის უნდა მივცეთ keyword-ებამდე.

✅ სწორად:

person_info("Nika", age=25)


❌ არასწორად:

person_info(age=25, "Nika")  # შეცდომა!

💡 შეჯამება ცხრილით
ცნება	აღწერა	მაგალითი
Function	კოდის ბლოკი ხელახალი გამოყენებისთვის	def greet():
Parameter	ფუნქციის შიგნით ცვლადი	def greet(name):
Argument	ფუნქციის გამოძახებისას გადაცემული მნიშვნელობა	greet("Nika")
Return	აბრუნებს შედეგს	return x + y
Positional arg	გადაეცემა თანმიმდევრობით	add(3, 5)
Keyword arg	გადაეცემა სახელით	add(b=5, a=3)