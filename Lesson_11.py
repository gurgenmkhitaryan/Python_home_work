# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def new_list(size_):
    new_list = []
    for i in range(1, size_ + 1):
        new_list.append(random.randint(0, 10))
    return new_list


size_list = int(input('Введите размер списка: '))
my_list = new_list(size_list)
mult_list = []

for i in range(size_list // 2):
    count = my_list[i] * my_list[- i - 1]
    mult_list.append(count)

if size_list % 2 != 0:
    mult_list.append(my_list[size_list // 2] ** 2)

print(f'Исходный список = {my_list} произведение пар чисел списка = {mult_list}')
