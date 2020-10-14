"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


# оставил print-ы в комментах, чтобы потом можно было вернуться, посмотреть еще раз как работает
# append заменяет +1 к индексу результирующего массива как в описании алгоритма сортировки.

from random import uniform


def func_merge_sort_merge(left, right):
    res_sort = []
    left_index = right_index = 0
    # print(f'{left=}, {right=}')
    for _ in range(len(left) + len(right)):
        # print(i)
        # print(left, right)
        if len(left) > left_index and len(right) > right_index:
            if left[left_index] <= right[right_index]:
                res_sort.append(left[left_index])
                left_index += 1
            else:
                res_sort.append(right[right_index])
                right_index += 1
        elif left_index == len(left):
            # print(f'{left_index=}')
            # print(f'{left=}')
            # print(f'{right_index=}')
            res_sort.append(right[right_index])
            right_index += 1
        elif right_index == len(right):
            # print(f'{right_index=}')
            # print(f'{right=}')
            # print(f'{left_index=}')
            res_sort.append(left[left_index])
            left_index += 1
        # print(f'{res_sort=}')
    return res_sort


def func_merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = func_merge_sort(array[:mid])
    right = func_merge_sort(array[mid:])
    return func_merge_sort_merge(left, right)


SIZE = 10

a = [round(uniform(0, 50 - 0.1), 2) for i in range(SIZE)]
print(a)
print(func_merge_sort(a))
