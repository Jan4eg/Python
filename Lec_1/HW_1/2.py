# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a = int(input())
b = 0
c = a
while c % 10 != 0 or c > 0:
    b = b + (c % 10)
    c = c // 10

print (a, '->', b)
