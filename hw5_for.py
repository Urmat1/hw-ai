# task 1 
# task1 = [1, 2, 3, 4, 5]
# for a in task1:
#     if a % 2:
#         print(a)

# task 2
# A
# n = 5
# list1 = []
# for list_ in range(1, n+1):
#     list1.append(f'{list_}')
# print(list1)

# # B
# for a in range(len(list1)):
#     if a % 2 == 1:
#         list1[a] = str(int(list1[a]) * 10) 
# print(list1)  

# task 3 
# task = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
# task3 = []
# for a in range(1, len(task), 2):
#     task3.append(task[a])
#     print(task3)

# task 4 
# ls = [11, 23, 45, 7, 9]
# for a in ls[::-1]:
#     print(a)

# task 5 
# n = 17
# 1 вариант 
# users = []
# for a in range(1, n+1):
#     if a < 10:
#         users.append(f'ID_000{a}')
#     elif a >= 10:
#         users.append(f'ID_00{a}')
#     elif a >= 100:
#         users.append(f'ID_0{a}')
#     else:
#         users.append(f'ID_{a}')
# print(users)
# 2 вариант
# users_id = [
#     f'ID_000{a}' if a < 10
#     else f'ID_00{a}' if a >= 10
#     else f'ID_0{a}' if a >= 100
#     else f'ID_{a}'
#     for a in range(1, n+1)
#     ]
# print(users_id)

# task 6
# address = 'г. Бишкек, ул. Абдрахманова, д. 25'
# вариант 1 
# x = [address.split()]
# for a in x:
#     print(f"city\n>>> {a[1]}")
#     print(f"street\n>>> {a[3]}")
#     print(f"house_number\n>>> {a[5]}")

# вариант 2 
# parts = address.replace(',', '').split()
# city = street = ""
# house_number = 0
# for p in parts:
#     if p == "Бишкек":
#         city = p
#     elif p == "Абдрахманова":
#         street = p
#     elif p.isdigit():
#         house_number = int(p)
# print(city)
# print(street)
# print(house_number)

# task 7
# users = [23, 24, 43, 25, 83]
# вариант 1 
# users_id = [f'ID_{i}' for i in users ]
# print(users_id)
# вариант 2
# users_id = []
# for i in users:
#     users_id.append(f'ID_{i}')
# print(users_id)

# task 8
# my_str = 'abcdefg12345'
# str_ = 'abc'
# r = ""
# for x in my_str:
#     if x in str_:
#         r += x
# print(r)

# task 9
# вариант 1 
# builders = 24
# t = range(1, 24+1)
# price = []
# for a in t:
#     t2 = builders - a
#     result = 4*a**2 + t2**2
#     price.append(result)
#     print(f"Если количество строителей на первый обьект {a},\nA на второй обьект {t2},\nTо стоимость составляет {result} USD")
# print(f'Минимальные траты составят {min(price)} USD')
    
# вариант 2
# builders = 24
# price = []
# for t in range(1, builders+1):
#     s = 4*t**2 + (builders - t)**2
#     price.append(s)
# print(min(price))

# task 10
# id_list = ['ID_23', 'ID_24', 'ID_43', 'ID_25', 'ID_83']
# task10 = []
# for a in id_list:
#     task10.append(a[3:])
# print(task10)

# task 11
# nums = [2, 4, 6, 8, 6, 4, 5]
# result = numbers = [2, 4, 6, 8, 6, 4, 5]
# task11 = []
# for i in range(len(numbers)):
#     if i == 0:
#         task11.append(numbers[-1] + numbers[1])
#     elif i == len(numbers) - 1:
#         task11.append(numbers[-2] + numbers[0])
#     else:
#         task11.append(numbers[i - 1] + numbers[i + 1])

# print(task11) 

# task 12
# task12 = []
# for x in range(-100, 101):
#     if x**2 - 11*x + 30 == 0:
#         task12.append(x)

# print(task12)


# task 13
# task13 = []
# for x in range(-101, 100):
#     y = x**2 - 8*x + 3
#     task13.append(y)
# print(min(task13))

# task14
# task14 = []
# b_y = None
# b_x = None
# for x in range(-101, 100):
#     y = x**2 - x - 6
#     if b_y is None or y < b_y:
#         b_y = y
#         b_x = x
#         task14 = b_x
# print(task14)

# task15
# for x in range(-101, 100):
#     y1 = 2*x - 3
#     y2 = -x + 6
#     if y1 == y2:
#         print(x)

# task16
# task16 = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
# t = [task16[x] for x in range(len(task16)) if x % 2 == 0]
# print(t)

# task17
# list_ = [1, 3, '1', 4, '89', 5, '9', 7, "75", 12]
# task17 = 0
# for x in list_:
#     if isinstance(x, str):
#         task17 += int(x)
#     else:
#         task17 += x
# print(task17)

# task18
# list_ = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
# i = len(list_) // 2
# for x in range(len(list_) -1, i - 1, -1):
#     print(list_[x])

# task19
# best_summa = None
# best_d = None
# for d in range(0, 23):           
#     p1 = d / 22 * 100            
#     p2 = (25 - d) / 23 * 100     
#     summa = p1 + p2             
#     if best_summa is None or summa > best_summa:
#         best_summa = summa
#         best_d = d
# print(f"Девочек в первый класс: {best_d}, во второй: {25 - best_d}")
# print(f"Максимальная сумма процентов: {best_summa}")

# task20
# builders = 24
# price = []
# for t in range(1, builders+1):
#     s = 4*t**2 + (builders - t)**2
#     price.append(s)
# print(min(price))

# task21
# import math
# best_dist = None
# best_t = None
# for t in range(0, 600):
#     i = t / 10
#     v1 = 5 - (40/60)*i
#     v2 = 3 - (30/60)*i
#     km = math.sqrt(( v1**2 + v2**2 ))
#     if best_dist is None or km < best_dist:
#         best_dist = km
#         best_t = i
# print(f'Лучшая дистанция {best_dist}')
# print(f'Лучшее время {best_t}')