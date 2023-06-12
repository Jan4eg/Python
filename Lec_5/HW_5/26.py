# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def degree(A, B):
#     if B == 0:
#         return 1
#     else:
#         B -= 1
#         return degree(A, B) * A
    

# A = int(input())
# B = int(input())

# print(degree(A, B))

def pow_num(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow_num(a, b + 1) * 1 / a
    return pow_num(a, b - 1) * a


print(pow_num(int(input()), int(input())))