🧠 1. Local vs Global Scope

Scope — არის ის ტერიტორია, სადაც ცვლადი ხელმისაწვდომია (გამოიყენება).

🔹 Local scope (ლოკალური არე)

ცვლადი გამოცხადებულია ფუნქციის შიგნით.

გამოიყენება მხოლოდ იმ ფუნქციაში, სადაც შეიქმნა.

ფუნქციის დასრულების შემდეგ იღუპება.

მაგალითი:

def my_function():
    x = 10   # local variable
    print(x)

my_function()
print(x)  # Error: x is not defined


🔹 Global scope (გლობალური არე)

ცვლადი გამოცხადებულია ფუნქციის გარეთ.

ხელმისაწვდომია მთელ პროგრამაში, მათ შორის ფუნქციების შიგნით (მხოლოდ წასაკითხად).

მაგალითი:

x = 5  # global variable

def my_function():
    print(x)  # შეგვიძლია წაკითხვა

my_function()
print(x)

🚫 2. Does Python Have Block Scope?

❌ არა. Python-ში ბლოკური scope არ არსებობს.

ეს ნიშნავს, რომ if, for, while, ან try ბლოკებში შექმნილი ცვლადები მთელ ფუნქციაში ან მოდულში ხელმისაწვდომია.

მაგალითი:

if True:
    x = 10  # declared inside block

print(x)  # Still works! (Python doesn't have block scope)


📘 განსხვავებით JavaScript ან C++-ისგან, სადაც ბლოკში შექმნილი ცვლადი მხოლოდ იმ ბლოკში მოქმედებს.

✏️ 3. How to Modify a Global Variable (Inside a Function)

თუ ფუნქციის შიგნით გინდა გლობალური ცვლადის შეცვლა, უნდა გამოიყენო global keyword.

მაგალითი:

x = 10

def change_global():
    global x    # declare we mean the global x
    x = 20      # modify it

change_global()
print(x)  # 20


🟡 თუ არ გამოიყენებ global-ს, Python შექმნის ახალ ლოკალურ ცვლადს, და გლობალურს არ შეცვლის.

მაგალითი:

x = 10

def wrong_way():
    x = 20  # local variable, does NOT affect global x

wrong_way()
print(x)  # 10

💎 4. Python Constants and Global Scope

Python-ში ნამდვილ "constant" ტიპი არ არსებობს, მაგრამ ტრადიციულად დიდი ასოებით (UPPERCASE) ვწერთ ცვლადებს, რომ აღვნიშნოთ — არ უნდა შეიცვალოს.

მაგალითი:

PI = 3.14159  # constant (by convention)

def area_of_circle(r):
    return PI * r ** 2

print(area_of_circle(5))


📍Constant-ები ჩვეულებრივ გლობალური ცვლადებია, მაგრამ პროგრამისტის კეთილი ნებაა, რომ არ შეცვალოს ისინი.

PI = 3.14159
PI = 3  # technically allowed, but bad practice ❌

🧩 მოკლე შეჯამება
ცნება	აღწერა	მაგალითი
Local variable	ფუნქციის შიგნით შექმნილი ცვლადი	def f(): x = 5
Global variable	ფუნქციის გარეთ შექმნილი ცვლადი	x = 10
No block scope	if, for ბლოკში შექმნილი ცვლადი მაინც ხელმისაწვდომია	if True: x=1; print(x)
Modify global	გამოიყენე global სიტყვა	global x
Constant	ჩვეულებრივი ცვლადი, მაგრამ დიდი ასოებით	MAX_SIZE = 100