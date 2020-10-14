"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю
Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""


arr = [-55, -69, -5, 72, -41, -58, -3, -79, 58, 74, 1]
i = 0
index = -1
while i < len(arr):
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(f'Максимальный отрицательный элемент в данном массиве = {arr[index]}, его индекс {index}')
