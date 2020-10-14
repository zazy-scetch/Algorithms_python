"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Пример:
Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""


import random

SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 99
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')

min_column_value = []

for i in range(SIZE):
    column = []
    for o in range(SIZE):
        column.append(matrix[o][i])
    num_min = column[0]
    for p in column:
        if num_min >= p:
            num_min = p
    min_column_value.append(num_min)


max_num_min_column_value = min_column_value[0]

for i in min_column_value:
    if max_num_min_column_value <= i:
        max_num_min_column_value = i
print(f'\nМинимальные значения столбцов матрицы: {min_column_value}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_num_min_column_value}')
