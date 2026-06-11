# task 1 
# number = int(input('Введите число: '))
# if number > 0:
#     print(True)
# else: 
#     print(False)

# task 2 
# mark = int(input("how many points: "))
# if mark >= 90:
#     print('Отлично, 5')
# elif 80 <= mark < 90:
#     print('Здорово, 4')
# elif 70 <= mark < 80:
#     print('Хорошо, 3')
# elif 60 <= mark < 70:
#     print('Вам стоит подучить материал')
# else: 
#     print('Вы не сдали экзамен')

# task 3
# x = 102
# y = 36
# z = 90
# if x <= y and x <= z:
#     print(x)
# elif y <= x and y <= z:
#     print(y)
# else:
#     print(z)

# task 4
# x = int(input('x '))
# y = int(input('y '))

# if x // y:
#     print(x // y)
# else: 
#     print(x + y)

# task 5
# a = 4
# b = 9
# c = 6

# if a + b > c and a + c > b and b + c > a:
#     print('yes')
# else:
#     print('no')

# task 6
# a = 58
# b = 5
# c = 63

# if a + b == c:
#     print(True)
# else: 
#     print(False)

# task 7
# b = int(input('Числитель '))
# a = int(input('Знаменатель '))
# x = b / a

# if 2 <= x < 10:
#     print(True)
# else:
#     print(False)

# task 8 
# x = float(input('Введите рациональное число '))

# if x < 4 or x >= 5:
#     print(True)
# else:
#     print(False)

# task 9 
# a = float(input('Введите число '))
# x = [2, 4, 6, 8, 10]
# if a in x: 
#     print(True)
# else: 
#     print(False)

# task 10 
# x = float(input('Введите рациональное число '))
# if -10 < x < 5 or 5 < x <= 7 or x > 8:
#     print(True)
# else: 
#     print(False)

# task 11
# import sympy as sp

# x = sp.Symbol('x', real=True)
# # С неравенством помогала нейросеть
# expr = sp.Ge((x**2 - 3*x)/(x + 5), (x - 3)/(7 - x))
# solution = sp.solve_univariate_inequality(expr, x, relational=False)
# a = float(input('Введите рациональное число '))
# print(solution)

# if -5 < a <= 1 or 3 <= a <= 5 or a > 7:
#     print(True)
# else:
#     print(False)

# task 12
# import sympy as sp

# x = sp.Symbol('x', real=True)
# s1 = sp.solve_univariate_inequality(x**2 - 3*x <= 0, x, relational=False)
# s2 = sp.solve_univariate_inequality(x**2 - 6*x + 8 > 0, x, relational=False)
# solution = s1.intersect(s2)

# a = float(input('Введите рациональное число '))
# print(a in solution)

# task 13
# a = float(input('Введите рациональное число '))

# if a <= 2 or a > 8:
#     print(True)
# else:
#     print(False)


