# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

N = int(input())

for i in range(N):
    if 2**i<N:
        print(2**i)