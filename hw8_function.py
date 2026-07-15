# task 1
# def func1():
#     print('hello')
# func1()

# task 2 
# def func2(a, b):
#     return a + b
# func2(1, 2)

# task 3
# def wallet(a, b):
#     print(f'На {a}, потрачено {b}')
# wallet('Хлеб', '300')

# task 4
# def func4(str):
#     print(str.replace(',', '.').replace(' ', '"'))
# func4("hello, world")

# task 5
# def add(a, b):
#     return a + b
# def div(a, b):
#     return a // b
# print(div(add(4, 5), 3))
    
# task 6
# def mult(list_):
#     result = 1
#     for n in list_:
#         result *= n
#     return result
# print(mult([1, 2, 3, 4, 5]))

# task 7
# def str_check(str):
#     if 'data science' in str:
#         print(True)
#     else:
#         print(False)
# str_check('Hello world data science')

# task 8
# bd = ['Emil', 'Rena', 'Aliya', 'Hur']
# def check(a):
#     if a in bd:
#         print('yes')
#     else: 
#         print('no')
# check('Aman')

# task 9
# def func9(a):
#     return a, a**2
# print(func9(2))

# task 10
# users = [
#   { 'name': 'Ron', 'age': 18, 'work': 'IT-backend developer'},
#   { 'name': 'Sam', 'age': 23, 'work': 'Doctor'},
#   { 'name': 'Bob', 'age': 26, 'work': 'Driver'},
#   { 'name': 'John', 'age': 39, 'work': 'Teacher'},
#   { 'name': 'Jack', 'age': 29, 'work': 'IT-frontend developer'}
# ]   
# def employee(users):
#     result = []
#     for a in users:
#         if a['age'] > 21 and 'IT' in a['work']:
#             result.append(a['name'])
#     return result
# print(employee(users))

# task 11
# def arg_types(a, b):
#     return type(a), type(b)
# print(arg_types('hello world', True))

# task 12
# def check_nan(list_):
#     result = []
#     for a in list_:
#         if a != 'nan':
#             result.append(a)
#     return result
# print(check_nan([1, 2, 2, 3, 'nan', 12, 23, 'nan']))
