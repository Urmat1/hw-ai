# task 22
# ls = [[0], [1, 2], [3, 5], [5, 6], [7, 8, 9]]
# a = ls[0]
# b = ls[0]                   
# for x in ls:                 
#     if len(x) > len(a): 
#         a = x
#     elif len(x) < len(b):
#         b = x
# print(a)
# print(b)

# task 23
# ls = [20, -40, 30, -20, 20, 30, 40, 50, 20, 60, 60, -70, -20]
# task23 = []
# for x in ls:
#     if ls.count(x) > 1:
#         task23.append(x)
# print(task23)

# task 24
# nums = ['one', 'two', 'three', 'four', 'five']
# task24 = []
# for x in nums:
#     task24.append(x[::-1])
# print(task24)    

# task 25
# task25 = [[0, 2, 4, 5], [1, 2, 2, 8, 9], [3, 5, 3], [5, 6, 9, 12], [7, 82, 12, 9]]
# for x in task25:
#     # print(x)
#     for y in x[:]:
#         if y % 2 == 0:
#             x.remove(y)
# print(task25)

# task 26
# ls = ['one', 'two', 'three', 'four', 'five']
# task26 = []
# for x in ls:
#     task26.append(x.upper())
# print(task26)

# task 27
# list_ = [2, 4, 97, 20, 10, 35, 23, 10, 1000]
# ls = list_[0]
# task27 = []
# for x in list_:
#     if x < ls:
#         ls = x
# task27.append(ls)
# print(task27)

# task 28
# for x in range(-100, 100):
#     for a in range(-100, 100):
#         y1 = x**2 - 6*x + 1
#         y2 = a*x
#         if y1 == y2:
#             print(f'a={a}')

# task 29
best = 0
best_config = None
for k in range(101):
    A1 = k * 3              
    B1 = (100 - k) * 1     
    for m in range(101):
        A2 = int(m ** 0.5)         
        B2 = int((100 - m) ** 0.5) 
        A = A1 + A2    
        B = B1 + B2    
        products = min(A, B // 3)  
        if products > best:
            best = products
            best_config = (k, m)
print(f"Максимум изделий: {best}")
print(f"Конфигурация: {best_config}")