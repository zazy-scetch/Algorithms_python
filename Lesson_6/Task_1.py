"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


# 64-битная. Python 3.8.2.


# ***********************ПЕРВЫЙ БЛОК**********************
"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random
import sys
import numpy
from collections import Counter

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
# считаем какие числа встречаются чаще, записываем результаты в новый массив
array_2 = []
for i in array:
    how_often = 0
    for x in array:
        if i == x:
            how_often += 1
    array_2 = array_2 + [how_often]
pos = len(array_2)
a = array_2[pos - 1]
pos_max = 0

# ищем максимальное число повторений в исходном массиве (через второй массив)
for j in array_2:
    pos -= 1
    if a <= j:
        a = j
        pos_max = (len(array) - 1) - pos

# print(array_2)

pos_2 = 0
array_3 = []

# записываем числа, которые чаще всего повторяются в новый массив
for k in array_2:
    if k == array_2[pos_max]:
        array_3 = array_3 + [array[pos_2]]
    pos_2 += 1

# print(array_3)

# ищем уникальные в 3м массиве
# unique = set(array_3) # наверно это уже читерство
# unique = list(unique)
array_4 = [array_3[0]]
for n in array_3[1:]:
    if n not in array_4:
        array_4 = array_4 + [n]

# print(array_4)
h = 0
if len(array_4) == len(array):
    print("Нет повторяющихся чисел")
else:
    print('Чаще всего встречается(ются) число(а):')
    for h in array_4:
        print(f'{h}', end='\t')


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(SIZE, MIN_ITEM, MAX_ITEM, array, array_2, i, how_often, x, pos, a, pos_max, j, pos_2, array_3, k, n, array_4, h)

"""
~1484 байт (т.к. random, и кол-во часто встречающихся может меняться, а так же 0 меньше по памяти). Почти 1,5 килобайта.
Если уникальны все числа, то память 2092 байт.
Очень плохо для работы с изначальным списком в 10 чисел.
Особенно забавно, что список из одних единиц почти равен по размеру списка из чисел от 0 до 100.
Заметил, что array_3 и array_4 по кол-ву элементов и диапазону чисел равен array, но сама оболочка занимет меньше места.
И как минимум 3 раза гоняем списки с одним и тем же размером) Особенно когда все уникальны и не находим повторений.
При SIZE=1000 размер 74 килобайта. 
Для чистоты в разных массивах разные переменные для итераций. Также некоторые пришлось вынести за циклы или ветвления.
"""

# 2 вариант. Изначально оптимизированный по скорости, но не по памяти. Сейчас пробую оптимизировать по памяти.
# Закомментировал генерацию списка, чтобы оценивать алгоритмы на одинаковых входных данных.

# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = numpy.random.randint(MIN_ITEM, MAX_ITEM, SIZE).tolist()
# print(array)

# считаем какие числа встречаются чаще и как часто, записываем результаты в словарь. Убрал дополнительный цикл.
# Добавил  Counter.
result = Counter(array)
print(result)

# ищем максимальные значения в словаре
other_max_num_list = []
max_count = 1
max_num = 0
for key, value in result.items():
    if value > max_count:
        max_count = value
        max_num = key
        if other_max_num_list:
            other_max_num_list.clear()
        continue
    elif 1 < max_count == value:
        other_max_num_list.append(key)

print(f'\n{result}')

if max_count == 1:
    print("Нет повторяющихся чисел")
elif not other_max_num_list:
    print(f'Чаще всего встречается число - {max_num}')
else:
    print(f'Чаще всего встречается число - {max_num}, Другие числа с этой же частотой: {other_max_num_list}')


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(SIZE, MIN_ITEM, MAX_ITEM, array, result, n, other_max_num_list, max_count, max_num, key, value)

"""
~1620 байт (если найдено хоть одно число, если ничего не найдено, то 1672). Больше на 136 байт. 
Все из-за словаря. Здесь Counter вместо возможного цикла с обычным словарем. 
Думаю тут не сильно память выше, но скорость может быть выше.
Кстати, с обычным словарем: 1604 и 1656 соответственно.
Пустой список 56 байт.
"""

# 3 Вариант.
# Пробуем убрать словарь. Сделать список из списков.
# Закомментировал генерацию списка, чтобы оценивать алгоритмы на одинаковых входных данных.

# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = numpy.random.randint(MIN_ITEM, MAX_ITEM, SIZE).tolist()
# print(array)

# считаем какие числа встречаются чаще и как часто, записываем результаты в список.
result = []
count = 1
for n in array:
    for k in result:
        if n == k[0]:
            k[1] += 1
            print(n, k[1])
    result.append([n, count])
print(result)

# # ищем максимальные значения в списках
max_num = 0
other_max_num_list = []
for item in result:
    for j in item:
        if item[1] > 1:
            max_num = item[0]
            count = item[1]
            if other_max_num_list:
                other_max_num_list.clear()
            continue
        elif 1 < item[1] == count:
            other_max_num_list.append(item[0])

if count == 1:
    print("Нет повторяющихся чисел")
elif not other_max_num_list:
    print(f'Чаще всего встречается число - {max_num}')
else:
    print(f'Чаще всего встречается число - {max_num}, Другие числа с этой же частотой: {other_max_num_list}')


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(SIZE, MIN_ITEM, MAX_ITEM, array, result, n, k, max_num, other_max_num_list)

# ~1688 байт. При всех уникальных 1684 байта.
# Данный вариант показывает обратную картину, когда при всех уникальных память
# (что при размере 10 и диапазоне от 0 до 100 не редкость) меньше, чем если бы мы нашли числа.

"""
Итоги по 1 блоку.
64-битная. Python 3.8.2.
Т.к. задания с random, то рез-ты разные немного могут быть.
1. ~1484 байта.
2. ~1620 байт. 
3. ~1688 байт.
В 3м варианте, где список в списке, размер списка равен изначальному, хоть мы и добавили внутрь еще списки. 
Но пришлось добавить еще циклы. Что может повлиять на скорость. 
На мой взгляд оптимальный второй вариант, т.к. нам важны скорости в своременном мире, а память все дешевле.
Заметил важное - в зависимости от рез-та меняется занимаемая память. И важно при написании алгоритма учитывать какой
результат будет встречаться чаще всего, то столько памяти чаще всего и будет занято при работе программы.
"""

# ***********************ВТОРОЙ БЛОК**********************
# Вдруг для задания нельзя было использовать одну и ту же задачу, есть другая задача.

"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
Обусловлено считать пользователя идеальным, проверок на ошибки не делаем
"""

a = int(input('Введите трехзначное число: '))

b = a // 100
c = a % 100 // 10
d = a % 10
s = b + c + d
m = b * c * d

print('Сумма цифр числа =', s, '\nПроизведение цифр числа =', m)


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(a, b, c, d, s, m)

# 2 вариант.

a = int(input('Введите трехзначное число: '))

s = (a // 100) + (a % 100 // 10) + (a % 10)
m = (a // 100) * (a % 100 // 10) * (a % 10)

print('Сумма цифр числа =', s, '\nПроизведение цифр числа =', m)


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(a, s, m)

# 3 Вариант.
a = int(input('Введите трехзначное число: '))

print(f'Сумма цифр числа = {(a // 100) + (a % 100 // 10) + (a % 10)}')
print(f'Произведение цифр числа = {(a // 100) * (a % 100 // 10) * (a % 10)}')


def show(*args):
    sums = 0
    for i in args:
        print(f'type={type(i)}, size={sys.getsizeof(i)}, obj={i}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
                    sums += sys.getsizeof(key) + sys.getsizeof(value)
                    print(sums)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
                    sums += sys.getsizeof(item)
                    print(sums)
        sums += sys.getsizeof(i)
        print(sums)


show(a)

"""
Итоги по 2 блоку. 
1. 168 байт. Много переменных.
2. 84 байта. Все еще много переменных.
3. 28 байт. Обошлось все одной переменной. Победитель. Максимальная оптимизация за счет снижения кол-ва переменных.
"""
