# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет 
# счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# stroca = str(120030)
# if int(stroca[0]) + int(stroca[1]) + int(stroca[2]) == int(stroca[3]) + int(stroca[4]) + int(stroca[5]):
#     print('yes')
# else:
#     print('no')

ticket_num = int(input())

sum_first = 0
sum_last = 0

while ticket_num:
    digit = ticket_num % 10
    if ticket_num > 999:
        sum_first += digit
    else: 
        sum_last += digit
    ticket_num //= 10

print(f"Счастливый билет: {sum_first == sum_last}")
