# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

S = 0
P = 0

while S <= 0 and P <= 0:
    S = int(input("Введите сумму: "))
    P = int(input("Введите произведение: "))

# x = (S - int((S**2 - 4*P)**0.5)) // 2
# y = (S + int((S**2 - 4*P)**0.5)) // 2

# print(x, y)

#x**2 - S*x + P = 0

D = int((-S)**2 - 4 * P)
if D >= 0:
    x_1 = int((-(-S//2) - int(D**0.5)) / 1)
    if x_1 > 0:
        x_2 = int(P / x_1)
        print(x_1, x_2)
    else:
        print("корней нет")
else:
    print("корней нет")







