# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# from random import randint

# list_num = [randint(1, 10) for _ in range(int(input()))]
# max = 0
# print(list_num)

# for i in range(len(list_num)):
#     if (i != len(list_num)-1) and (n:=list_num[i] + list_num[i+1] + list_num[i-1]) > max:
#         max = n
#     elif (n:=list_num[i] + list_num[0] + list_num[i-1]) > max:
#         max = n
# print(max)

# n = int(input())
# bushes = [int(i) for i in input().split()]
# bush_max = 0

# for i in range(n):
#     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
#     if bush_sum > bush_max:
#             bush_max = bush_sum

# print(bush_max)

# # ----------------------------------

# n = int(input())
# bushes = [int(i) for i in input().split()]
# bush_max = 0

# for i in range(-1, n - 1):
#     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
#     if bush_sum > bush_max:
#             bush_max = bush_sum

# print(bush_max)