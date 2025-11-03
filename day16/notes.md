1. OOP (Object-Oriented Programming) – ობიექტზე ორიენტირებული პროგრამირება

დეფინიცია:
OOP არის პროგრამირების პარადიგმა, რომელიც პროგრამას ობიექტების (objects) საშუალებით აწყობს. ეს გვეხმარება კოდის ორგანიზებაში, მარტივად მენეჯმენტში და მრავალჯერადი გამოყენებაში.

ძირითადი პრინციპები:

Encapsulation (ენკაპსულაცია)
– მონაცემებისა და ფუნქციების (attributes & methods) ჯგუფირება ობიექტში.
– ხელს უწყობს მონაცემების დაცვას.

Abstraction (აბსტრაქცია)
– აუცილებელი დეტალების გამოტოვება, მხოლოდ საჭირო ინტერფეისის ჩვენება.

Inheritance (მემკვიდრეობა)
– ერთი კლასი იღებს მახასიათებლებსა და ფუნქციებს სხვა კლასიდან.
– კოდი მეორდება ნაკლებად.

Polymorphism (პოლიმორფიზმი)
– ერთი ფუნქცია/მეთოდი სხვადასხვა ობიექტზე სხვადასხვა შედეგის წარმოება.

2. Class და Object

Class (კლასი)
– Blueprint ან შაბლონი, რომელიც განსაზღვრავს ობიექტის სტრუქტურას.
– აღწერს, რა attributes და methods ექნება ობიექტს.

Object (ობიექტი)
– კლასის რეალური ინსტანცია.
– მაგალითად:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")


აქ Car არის კლასსი, my_car არის ობიექტი.

3. Attributes და Methods

Attributes (მახასიათებლები)
– კლასის მონაცემები/შეკეთილობები.
– ორ ტიპად იყოფა:

Instance attributes – ობიექტზე სპეციფიკური.

self.color = "red"


Class attributes – კლასის საერთო, ყველა ობიექტისთვის საერთო.

wheels = 4


Methods (მეთოდები)
– კლასში ფუნქციები, რომლებიც ობიექტის ქმედებებს განსაზღვრავს.

def start(self):
    print(f"{self.brand} is starting!")


Special method: __init__
– კონსტრუქტორი, ობიექტის შექმნისას ავტომატურად იძახება.

def __init__(self, brand, model):
    self.brand = brand
    self.model = model

4. Python Packages (პაკეტები)

დეფინიცია:
Package არის ფოლდერი, რომელიც შეიცავს Python მოდულებს (.py ფაილებს) და ხშირად __init__.py ფაილს.
მიზანი: კოდის ორგანიზება და ფუნქციონალების მარტივი იმპორტი.

მოდულები vs პაკეტები

Module: single Python file (e.g., math.py)

Package: folder with multiple modules + __init__.py

პაკეტის გამოყენება:

# სტანდარტული პაკეტის იმპორტი
import math
print(math.sqrt(16))

# კონკრეტული ფუნქციის იმპორტი
from math import sqrt
print(sqrt(25))


მესაკუთრული პაკეტის შექმნა:

my_package/
    __init__.py
    module1.py
    module2.py


მხოლოდ საჭირო ფუნქციის იმპორტი:

from my_package.module1 import my_function


✅ შენიშვნები:

OOP-ში კლასები და ობიექტები “მსოფლიოს მოდელირების” ინსტრუმენტია.

Attributes + Methods – ობიექტის მდგომარეობისა და ქმედებების აღწერა.

Packages – კოდის სტრუქტურირება და განმეორებად გამოყენებადობა.