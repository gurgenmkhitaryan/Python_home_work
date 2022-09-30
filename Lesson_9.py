# 5. Реализуйте алгоритм перемешивания списка.
# random.randint(2, 6)
# random.randrange(2, 6)


import random


def new_list(size_):
    new_list = []
    for i in range(1, size_ + 1):
        new_list.append(i)
    return new_list

my_list = new_list(6)
for i in range(len(my_list)):
    temp = my_list[i]