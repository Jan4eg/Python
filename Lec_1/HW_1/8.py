# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите m: '))
m = int(input('Введите n: '))
k = int(input('Введите k: '))

# if k == n * m:
#     print('no')
# elif k < n and k < m:
#     print('no')
# elif k % n !=0 and k % m != 0:
#     print('no')
# else:
#     print('yes')

if (k % n == 0 or k % m == 0) and k < m * n:
    print("Yes")
else:
    print("No")