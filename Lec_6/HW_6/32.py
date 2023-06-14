# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

lenlst = int(input())
n = [int(i) for i in input().split()]
range_min = int(input())
range_max = int(input())
lst = list()

print(n)

for i in range(lenlst):
    if n[i]>=range_min and n[i]<=range_max:
        lst.append(i)
print(*(lst))


# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])