# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки
# Пример:
# Для n = 6 -> 14.072



def new_list(size_):
    new_list = []
    for i in range(1, size_ + 1):
        new_list.append((1 + 1 / i) ** i)
    return new_list


def sum_list(list_):
    sum_ = 0
    for i in list_:
        sum_ += i
    return sum_


num = int(input('Введите количество элементов списка: '))
result = (round(sum_list(new_list(num)), 3))
print(f"{result:.{3}f}")


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки
# Пример:
# Для n = 6 -> 14.072

num = int(input('Введите количество элементов списка: '))

list = [round((1+1/x)**x, 2) for x in range(1,num+1)]

# print (f'Список: {list}')
print(f'Сумма элементов списка: {sum(list)}')