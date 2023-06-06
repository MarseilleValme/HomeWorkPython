# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
n = 20
list = []
diapazon = [5, 9]
list_index = []

for i in range(n):
    list.append(randint(0, 20))
print(list)
print(f'Заданному диапазону {diapazon} удовлетворяют')
for i in range(n):
    if list[i]>diapazon[0] and list[i]<diapazon[1]:
        print(f'list[{i}] = {list[i]}')