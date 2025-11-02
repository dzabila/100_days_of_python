🧩 1. Functions with Outputs (ფუნქციები, რომლებიც აბრუნებენ მნიშვნელობას)
🔹 განმარტება:

ფუნქცია შეიძლება მხოლოდ რაღაც ბეჭდავდეს (print()), ან დააბრუნოს შედეგი – ანუ “output”.
ამისთვის ვიყენებთ return საკვანძო სიტყვას.

🔸 მაგალითი:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # გამოიტანს 8


🧠 ახსნა:

return აბრუნებს მნიშვნელობას ფუნქციიდან.

ფუნქციის შესრულება return-ის შემდეგ წყდება.

დაბრუნებულ მნიშვნელობას შეგიძლია მიანიჭო ცვლადს.

🔹 კიდევ ერთი მაგალითი:
def greet(name):
    return f"Hello, {name}!"

message = greet("Nika")
print(message)


💡 განსხვავება print და return შორის:

მოქმედება	ახსნა
print()	უბრალოდ აჩვენებს ეკრანზე
return	აბრუნებს მნიშვნელობას პროგრამის შიგნით გამოსაყენებლად
🔁 2. Multiple Return Values (რამდენიმე მნიშვნელობის დაბრუნება)

Python-ში შეგიძლია ფუნქციამ ერთზე მეტი მნიშვნელობა დააბრუნოს — მძიმით გამოყოფილი ელემენტების სახით.
ფაქტობრივად, ფუნქცია აბრუნებს tuple-ს.

🔸 მაგალითი:
def get_name_and_age():
    name = "Nika"
    age = 25
    return name, age

n, a = get_name_and_age()
print(n)  # Nika
print(a)  # 25


📘 ახსნა:

ფუნქცია აბრუნებს ორ მნიშვნელობას → "Nika" და 25

როცა ვიძახებთ, შეგვიძლია ორივე ცვლადს მივანიჭოთ ეს მნიშვნელობები (n, a).

🔹 პრაქტიკული მაგალითი:
def min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

nums = [3, 8, 1, 5]
low, high = min_max(nums)
print(f"Min: {low}, Max: {high}")


შედეგი:

Min: 1, Max: 8

💡 დამატებითი შენიშვნა:

შეგიძლია მხოლოდ ერთი მნიშვნელობაც გამოიყენო, მაგალითად:

result = min_max(nums)
print(result)   # გამოიტანს (1, 8)


ეს არის tuple.

🧠 3. Docstrings (დოკუმენტაცია ფუნქციაში)
🔹 განმარტება:

Docstring — ეს არის ტექსტი, რომელიც აღწერს, რა აკეთებს ფუნქცია.
იგი იწერება სამმაგ ბრჭყალებში """ ... """ ფუნქციის შიგნით, პირველ ხაზად.

🔸 მაგალითი:
def greet(name):
    """
    Takes a person's name and returns a greeting message.
    """
    return f"Hello, {name}!"


📘 ახსნა:

Docstring უნდა იყოს პირველი სტრიქონი ფუნქციაში.

ხშირად გამოიყენება აღწერისთვის, რომ სხვამაც მარტივად გაიგოს, რას აკეთებს ფუნქცია.

მისი ნახვა შეიძლება help() ან .__doc__ მეშვეობით.

🔹 მაგალითი გამოყენებით:
def add(a, b):
    """
    Returns the sum of two numbers a and b.
    Parameters:
        a (int or float): first number
        b (int or float): second number
    Returns:
        int or float: sum of a and b
    """
    return a + b

print(help(add))         # ბეჭდავს docstring-ს
print(add.__doc__)       # იგივე შედეგი

🔹 მაგალითი უფრო კომპლექსური ფუნქციისთვის:
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The computed area (length * width).
    """
    return length * width


💡 ასეთი სტილი ძალიან ხშირად გამოიყენება პროფესიულ პროექტებში, რადგან:

კოდი უფრო გასაგებია სხვებისთვის

ხელს უწყობს ავტომატურ დოკუმენტაციის გენერაციას (მაგ. Sphinx)

📘 შეჯამება
თემა	აღწერა	საკვანძო სიტყვა / მაგალითი
Functions with Outputs	ფუნქცია აბრუნებს მნიშვნელობას	return result
Multiple Return Values	ფუნქცია აბრუნებს ერთზე მეტ მნიშვნელობას (tuple)	return x, y
Docstrings	ტექსტური აღწერა ფუნქციის შიგნით	""" აღწერა """