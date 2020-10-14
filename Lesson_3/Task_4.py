"""
Задание_4. Определить, какое число в массиве встречается чаще всего
Подсказка: можно применить ф-цию max с параметром key
"""

arr = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18, 12, 45, 25, 26, 51, 23, 41, 26]
num = arr[0]
max_count = 1
for i in range(len(arr) - 1):
    count = 1
    for k in range(i+1, len(arr)):
        if arr[i] == arr[k]:
            count += 1
    if count > max_count:
        max_count = count
        num = arr[i]

if max_count > 1:
    print(f'Число {num} повторяется {max_count} раз(а)')
else:
    print('Нет повторяющихся элементов')
