# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math


def num_result(number):
    count = 1
    result = 1
    new_list = []
    for i in range(number):
        result *= count
        count += 1
        new_list.append(result) 
    return new_list


digit = int(input('Введите число: '))
print(f'произведений чисел от 1 до {digit} ровно {num_result(digit)}: ')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


digit = int(input('Введите целое число: '))

numbers = list(map(lambda i: math.factorial (i), range (1, digit+1)))
print (numbers)