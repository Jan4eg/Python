# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

num_1, num_2 = int(input()), int(input())

print(f'{(n_1:= [random.randint(1, i+10) for i in range(num_1)])}' '\n' f'{(n_2:=[random.randint(1, i+10) for i in range(num_2)])}') 
print((sorted(set((set(n_1)).intersection(set(n_2))), reverse = False)))