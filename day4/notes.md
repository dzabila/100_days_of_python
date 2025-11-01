🧩 1. Module (მოდული)

მოდული — ეს არის Python ფაილი (.py), რომელიც შეიცავს კოდს: ცვლადებს, ფუნქციებს ან კლასებს, რომლებსაც შეგიძლია სხვაგანაც გამოიყენო.
იგი საშუალებას გაძლევს კოდი დაყო ნაწილებად და თავიდან არ დაწერო ერთიდაიგივე ლოგიკა.

მაგალითი:

# greetings.py
def say_hello(name):
    print(f"Hello, {name}!")


სხვა ფაილში:

import greetings
greetings.say_hello("Nika")


👉 მოდულის მთავარი იდეაა კოდის ორგანიზება და ხელახალი გამოყენება.

🎲 2. Random Module

random მოდული გეხმარება შემთხვევითი რიცხვებისა და არჩევანის გენერაციაში.

იმპორტი:

import random


ძირითადი გამოყენება:

random.random()       # აბრუნებს float-ს 0.0 და 1.0 შორის
random.randint(1, 10) # აბრუნებს მთელ რიცხვს 1-დან 10-მდე
random.choice(list)   # აბრუნებს შემთხვევით ელემენტს სიიდან
random.shuffle(list)  # არევს სიას შემთხვევითად
random.uniform(1, 5)  # აბრუნებს float-ს 1 და 5 შორის

📦 3. Import Module in File

მოდულის გამოყენება სხვადასხვა გზით შეიძლება:

სინტაქსი	აღწერა	მაგალითი
import module	იმპორტავს მთელ მოდულს	import math
import module as m	აძლევს მეტსახელს	import random as r
from module import func	იმპორტავს კონკრეტულ ფუნქციას	from math import sqrt
from module import *	იმპორტავს ყველაფერს	from math import * (არ არის რეკომენდირებული)
🎯 4. Some Random Functions (random module-ის მაგალითზე)
ფუნქცია	დანიშნულება	მაგალითი	შედეგი
random.random()	შემთხვევითი float 0–1 შორის	random.random()	0.478
random.randint(a,b)	შემთხვევითი მთელი რიცხვი	random.randint(1,6)	3
random.uniform(a,b)	float	random.uniform(1,5)	3.25
random.choice(seq)	აბრუნებს შემთხვევით ელემენტს	random.choice(['a','b','c'])	'b'
random.shuffle(list)	არევს სიას შემთხვევითად	–	[3,1,2]
random.sample(population, k)	აბრუნებს შემთხვევით k ელემენტს	random.sample(range(10), 3)	[1, 7, 4]
🧾 5. List (სია)

List — არის მონაცემთა ტიპი, რომელიც შეიცავს ელემენტების კოლექციას.
შეიძლება შეიცავდეს სხვადასხვა ტიპის მნიშვნელობებს.

შექმნა:

numbers = [1, 2, 3, 4]
mixed = [1, "Hello", True, 3.14]


მთავარი მახასიათებლები:

ცვალებადია (mutable)

ელემენტები ინახება ინდექსებით

შესაძლებელია ლუპით გადავლა

🔧 6. Popular List Methods
მეთოდი	აღწერა	მაგალითი	შედეგი
append(x)	ამატებს ელემენტს ბოლოში	lst.append(5)	[1,2,3,5]
insert(i, x)	ამატებს ელემენტს კონკრეტულ პოზიციაზე	lst.insert(1, 10)	[1,10,2,3]
remove(x)	შლის პირველ შესაბამის ელემენტს	lst.remove(2)	[1,3]
pop(i)	შლის და აბრუნებს ელემენტს ინდექსით	lst.pop(0)	შლის პირველ ელემენტს
sort()	ალაგებს სიას ზრდადობით	lst.sort()	[1,2,3]
reverse()	აბრუნებს სიას უკუღმა	lst.reverse()	[3,2,1]
count(x)	ითვლის რამდენჯერ გვხვდება ელემენტი	lst.count(2)	3
index(x)	აბრუნებს ელემენტის ინდექსს	lst.index(4)	2
copy()	ქმნის ასლს	new = lst.copy()	
clear()	ცარიელებს სიას	lst.clear()	[]

