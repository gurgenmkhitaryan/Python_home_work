# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def new_list(size_):
    ''' generate new list'''
    new_list = []
    for i in range(1, size_ + 1):
        new_list.append(i)
    return new_list


my_list = new_list(int(input('Введите размер списка: ')))
print(my_list)
count = 0
for i in range(1, len(my_list), 2):
        count += i
        print('i =', i)
print(f'Cумма чисел, стоящих на нечётных позициях = {count}.')



#  Найти сумму чисел списка стоящих на нечетной позиции

my_list = new_list(int(input('Введите размер списка: ')))
print(my_list)
sum_list = sum(my_list[item] for item in range(1, len(my_list), 2))
print(f'Cумма чисел, стоящих на нечётных позициях = {sum_list}.')

