# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)
    
a = int(input())
b = int(input())
print(sum(a, b))

# def f(a, b):
#     if b < 0 < a:
#         a, b = b, a
#     if b == 0:
#         return a
#     return f(a + 1, b - 1)


# n = int(input())
# m = int(input())
# print(f(n, m))