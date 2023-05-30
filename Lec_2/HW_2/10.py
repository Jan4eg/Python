# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input())
sum_0 = 0
sum_1 = 0

for i in range(n):
    revers = int(input(f"Введите 0 - если {i+1}-я монета лежит решкой, 1 - если гербом к верху: "))
    if revers == 1:
        sum_0 += 1
    else:
        sum_1 += 1

print(min(sum_0, sum_1))

# n = int(input())
# count = 0

# for i in range(n):
#     coin = int(input())
#     if coin:
#         count += 1

# if count > n // 2:
#     count = n - count

# print(count)

# n = int(input())
# count = 0

# for i in range(n):
#     if int(input()):
#         count += 1

# print(min(count, n - count))


