# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
from math import fabs

N = int(input("Введите число N (длину строки): "))
X = int(input("Введите число X: "))
result = 999

List_nums = [(random.randint(1, i+5)) for i in range(N)]

print(List_nums)

for i in range(0, len(List_nums)):
    if List_nums[i] == X:
        num = List_nums[i]
        break
    if (abs(List_nums[i] - X)) < result:
        result = abs(List_nums[i] - X)
        num = List_nums[i]
        
print(num) 


