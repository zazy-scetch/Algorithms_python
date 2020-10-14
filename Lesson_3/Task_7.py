"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""


arr = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]

if arr[0] > arr[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(2, len(arr)):
    if arr[i] < arr[min_1]:
        b = min_1
        min_1 = i
        if arr[b] < arr[min_2]:
            min_2 = b
    elif arr[i] < arr[min_2]:
        min_2 = i

print(f'Первый наименьший элемент: {arr[min_1]}')
print(f'Второй наименьший элемент: {arr[min_2]}')
