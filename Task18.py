# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
n = int(input('Введите кол-во элементов массива: '))
mass = []
for i in range(n):
    mass.append(randint(0, 10))
print(mass)
x = int(input('Введите искомое число: '))
diff = abs(x - mass[0])
for i in range(1, len(mass)):
    if abs(x - mass[i]) <= diff:
        diff = abs(x - mass[i])
        box = mass[i]
print(f'Самый близкий к X элемент: {box}')
