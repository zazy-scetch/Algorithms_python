"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""


import random

m = 3
SIZE = 2*m + 1


array = [int(random.random()*100) for _ in range(SIZE)]
# array = [2, 2, 2, 2, 3] # для теста
print(array)

for i in array:
    more = 0
    less = 0
    k = 0      # pycharm ругается, добавил
    for k in array:
        if i < k:
            more += 1
        if i > k:
            less += 1
    if more == len(array) // 2 or less == len(array) // 2:
        print(f'Медиана - {i}')
        break
    elif i == array[len(array) - 1] and i == k:   # далее для списков с одинаковыми элементами кроме одного
        k = array[array.index(k) - 1]
        if less == len(array) - 1 or more == 1:
            if i > k:
                print(f'Медиана - {k}')
            elif i < k:
                print(f'Медиана - {i}')
            break
        elif more == len(array) - 1 or less == 1:
            if i > k:
                print(f'Медиана - {i}')
            elif i < k:
                print(f'Медиана - {k}')
            break
