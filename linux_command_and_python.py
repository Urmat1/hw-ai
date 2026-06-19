# linux 1 easy
# mkdir practice_linux
# cd practice_linux
# mkdir docs images trash
# cd docs
# echo "Hello Linux" > notes.txt
# cat notes.txt

# linux 2 medium
# cd ~/practice_linux
# touch lesson1.txt lesson2.txt lesson3.txt
# mv lesson1.txt linux_intro.txt
# mv lesson2.txt commands.txt
# mv lesson3.txt trash/
# ls

# linux 3 hard
# mkdir project
# cd project
# mkdir src tests docs data
# echo "Urmat files" > README.md
# touch src/main.py
# cp README.md docs/
# rm -r data
# ls -R


# lists 1 easy
# numbers = [3, 7, 1, 9, 4]
# print(numbers[0])
# print(numbers[-1])
# print(sum(numbers))

# lists 2 medium
# Вариант 1
# numbers = [10, 15, 20, 25, 30, 35]
# numbers2 = [a for a in numbers if a > 20]
# print(numbers2)

# Вариант 2
# numbers = [10, 15, 20, 25, 30, 35]
# numbers2 = []
# for a in numbers:
#     if a > 20:
#         numbers2.append(a)
# print(numbers2)


# lists 3 hard
# numbers = [4, -2, 7, 0, -5, 9, -1]
# positive_numbers = [a for a in numbers if a > 0]
# negative_numbers = [b for b in numbers if b < 0]
# zero_numbers = [c for c in numbers if c == 0]
# print(positive_numbers)
# print(negative_numbers)
# print(zero_numbers)


# dictionaries 1 easy
# user = {
#     "name": "Ivan",
#     "age": 20,
#     "city": "Bishkek"
# }
# print(user["name"])
# print(user["age"])
# print(user["city"])

# dictionaries 2 medium
# users = [
#     {"name": "Ivan", "age": 19},
#     {"name": "Anna", "age": 25},
#     {"name": "Timur", "age": 17},
#     {"name": "Aibek", "age": 30},
# ]
# users_is_over18 = [
#     user["name"]
#     for user in users
#     if user["age"] > 18
# ]
# print(users_is_over18)

# dictionaries 3 hard
# products = [
#     {"name": "apple", "category": "fruit", "price": 50},
#     {"name": "banana", "category": "fruit", "price": 80},
#     {"name": "potato", "category": "vegetable", "price": 40},
#     {"name": "carrot", "category": "vegetable", "price": 60},
# ]
# vegetable = [
#     product["name"]
#     for product in products
#     if product["category"] == "vegetable"
# ]
# fruit = [
#     product["name"]
#     for product in products
#     if product["category"] == "fruit"
# ]
# print(vegetable)
# print(fruit)


# Кортеж 1 easy
# point = (10, 20)
# x, y = point
# print(f"x = {x}")
# print(f"y = {y}")

# Кортеж 2 medium
# points = [
#     (1, 2),
#     (3, 4),
#     (5, 6),
# ]
# sum_x = 0
# sum_y = 0
# for x, y in points:
#     sum_x += x
#     sum_y += y
# print(f"sum x = {sum_x}")
# print(f"sum y = {sum_y}")

# Кортеж 3 hard
# students = [
#     ("Ivan", 80),
#     ("Anna", 95),
#     ("Timur", 70),
#     ("Aibek", 88),
# ]
# max_m = students[0][1]
# name = students[0][0]
# for n, m in students:
#     if m > max_m:
#         max_m = m
#         name = n
# print(name, max_m)


# function 1 easy
# def greet(name):
#     return f"Hello, {name}"
# print(greet('Ivan'))

# function 2 medium
# def get_even_numbers(numbers):
#     ge_numbers = []
#     for n in numbers:
#         if n % 2 == 0:
#             ge_numbers.append(n)
#     return ge_numbers
# print(get_even_numbers([1, 2, 3, 4, 5, 6]))

# function 3 hard
# def calculate_total_price(cart):
#     total_price = 0
#     for price in cart:
#         total_price += price["price"] * price["quantity"]
#     return total_price
# cart = [
#     {"name": "apple", "price": 50, "quantity": 3},
#     {"name": "banana", "price": 80, "quantity": 2},
#     {"name": "milk", "price": 120, "quantity": 1},
# ]
# print(calculate_total_price(cart))


# try/except 1 easy 
# try:
#     num = int(input("Number "))
#     print(num)
# except ValueError:
#     print("Invalid number")

# try/except 2 medium
# numbers = [10, 20, 30]
# try:
#     index = int(input("Индекс: "))
#     print(numbers[index])
# except ValueError:
#     print("Индекс должен быть числом")
# except IndexError:
#     print("Индекс вне диапазона")

# try/except 3 hard
# def divide(a, b):
#     try:
#         a = float(a)
#         b = float(b)
#         if b == 0:
#             return "Cannot divide by zero"
#         return a / b
#     except ValueError:
#         return "Invalid input"
# print(divide("10", "2"))   
# print(divide("10", "0"))   
# print(divide("abc", "2"))  


# lc 1 easy
# numbers = [1, 2, 3, 4]
# result = [number * 2 for number in numbers]
# print(result)

# lc 2 medium
# words = ["python", "java", "go", "javascript"]
# word4 = [word for word in words if len(word) > 4]
# print(word4)

# lc 3 hard
# employees = [
#     {"name": "Ivan", "salary": 50000},
#     {"name": "Anna", "salary": 70000},
#     {"name": "Timur", "salary": 45000},
#     {"name": "Aibek", "salary": 90000},
# ]
# result = [emp["name"] for emp in employees if emp["salary"] >= 60000]
# print(result)


# Работа со строками 1 easy
# name = "timur"
# result = name.capitalize()
# print(result)

# Работа со строками 2 medium
# text = "  hello python  "
# result = text.strip().upper()
# print(result)

# Работа со строками 3 hard
# text = "python,java,go,javascript"
# words = text.split(",")
# print(words)
# result = " | ".join(words)
# print(result)

# Базовая аналитика на Python 1 easy
# sales = [100, 200, 150, 300, 250]
# total = sum(sales)
# minimum = min(sales)
# maximum = max(sales)
# average = sum(sales) / len(sales)
# print("sum:", total)
# print("min:", minimum)
# print("max:", maximum)
# print("avg:", average)

# Базовая аналитика на Python 2 medium
# sales = [
#     {"day": "Monday", "amount": 100},
#     {"day": "Tuesday", "amount": 200},
#     {"day": "Wednesday", "amount": 150},
#     {"day": "Thursday", "amount": 300},
# ]
# max_sale = sales[0]
# for item in sales:
#     if item["amount"] > max_sale["amount"]:
#         max_sale = item
# print(max_sale)

# Базовая аналитика на Python 3 hard
# orders = [
#     {"customer": "Ivan", "amount": 100},
#     {"customer": "Anna", "amount": 200},
#     {"customer": "Ivan", "amount": 150},
#     {"customer": "Timur", "amount": 300},
#     {"customer": "Anna", "amount": 50},
# ]
# result = {}
# for order in orders:
#     name = order["customer"]
#     amount = order["amount"]
#     if name in result:
#         result[name] += amount
#     else:
#         result[name] = amount
# print(result)



