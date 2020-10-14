"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


import timeit
import cProfile
import random
import numpy

"""
Разбил участки кода на функции, чтобы можно было каждую замерить в cProfile.
Чтобы генерация рандомного листа не влияла на время, попробуем сделать найденный возможно, 
более быстрый вариант через numpy.
Однако вариант с numpy показал не постоянство лучшего рез-та, но он точно не возрастает варианта с for.
Генерация списка по старой версии закомментирована. Результаты приведены для обоих случаев.
Где можно сделал append, немного, но увеличивает скорость. Предыдущее решение закомментировано.
Чтобы ради numpy и append не дублировать код, представляя его в виде доп. варианта, сделал уже в первом варианте.
"""

# 1й вариант. Почти все исходное сохранено из 3 урока (4 задание).

def func(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = numpy.random.randint(MIN_ITEM, MAX_ITEM, SIZE).tolist()
    # array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    # print(array)

    # считаем какие числа встречаются чаще и как часто, записываем результаты в новый массив
    array_2 = []

    def func_2(array, array_2):
        for i in array:
            how_often = 0
            for k in array:
                if i == k:
                    how_often += 1
            # array_2 = array_2 + [how_often]
            array_2.append(how_often)
        pos = len(array_2)
        a = array_2[pos - 1]
        pos_max = 0
        return array_2, pos_max, a, pos

    array_2, pos_max, a, pos = func_2(array, array_2)


    # ищем максимальное число повторений в исходном массиве (через второй массив)
    def func_3(array_2, pos_max, a, pos):
        for i in array_2:
            pos -= 1
            if a <= i:
                a = i
                pos_max = (len(array) - 1) - pos
        return array_2, pos_max, a, pos
    array_2, pos_max, a, pos = func_3(array_2, pos_max, a, pos)
    # print(pos_max)
    # print(array_2)

    pos_2 = 0
    array_3 = []


    # записываем числа, которые чаще всего повторяются в новый массив
    def func_4(array_2, array_3, pos_2, pos_max):
        for k in array_2:
            if k == array_2[pos_max]:
                # array_3 = array_3 + [array[pos_2]]
                array_3.append(array[pos_2])
            pos_2 += 1
        return array_2, array_3, pos_2, pos_max
    array_2, array_3, pos_2, pos_max = func_4(array_2, array_3, pos_2, pos_max)
    # print(pos_2)
    # print(array_3)


    # ищем уникальные в 3м массиве
    # unique = set(array_3) # наверно это уже читерство
    # unique = list(unique)
    def func_5(array_3):
        array_4 = [array_3[0]]
        for k in array_3[1:]:
            if k not in array_4:
                # array_4 = array_4 + [k]
                array_4.append(k)
        return array_4
    array_4 = func_5(array_3)
    return array_4

# Ниже данный код используется для вывода. В нашем случае предлагаю его не использовать в функции.
# if len(array_4) == len(array):
#     print("Нет повторяющихся чисел")
# else:
#     print('Чаще всего встречается(ются) число(а):')
#     for k in array_4:
#         print(f'{k}', end='\t')

# print(func(10))

print(timeit.timeit('func(10)', number=100, globals=globals()))     # 0.010545887000000032
# без numpy 0.003712160999999936 (в данном слуае быстрее)
print(timeit.timeit('func(100)', number=100, globals=globals()))    # 0.0694652710000001 больше в 23 раза.
# без numpy 0.090032738
print(timeit.timeit('func(1000)', number=100, globals=globals()))   # 5.102336329 - больше в 73 раза.
# без numpy 5.725997657000001
# На 50000 и более уже не стал тестировать, т.к. очень долго ждать.
print(timeit.timeit('func(10000)', number=100, globals=globals()))  # 504.513317272 - больше в 99 раз.
# без numpy 575.1423493689999
print(timeit.timeit('func(20000)', number=100, globals=globals()))  # 2219.452798484, увел. в 2, время возросло в 4.


cProfile.run('func(10)')    #   59 function calls in 0.000 seconds, без numpy 99 function calls in 0.000 seconds
#        1    0.000    0.000    0.000    0.000 task_1(old).py:19(func)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:29(func_2)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:45(func_3)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:60(func_4)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:74(func_5)
cProfile.run('func(100)')   #     143 function calls in 0.001 seconds, без numpy 645 function calls in 0.001 seconds
#        1    0.000    0.000    0.001    0.001 task_1(old).py:19(func)
#        1    0.001    0.001    0.001    0.001 task_1(old).py:29(func_2)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:45(func_3)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:60(func_4)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:74(func_5)
cProfile.run('func(1000)')      #     1062 function calls in 0.047 seconds,
# без numpy 6350 function calls in 0.051 seconds
#        1    0.000    0.000    0.047    0.047 task_1(old).py:19(func)
#        1    0.047    0.047    0.047    0.047 task_1(old).py:29(func_2)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:45(func_3)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:60(func_4)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:74(func_5)
#        1    0.000    0.000    0.000    0.000 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
#        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        1    0.000    0.000    0.000    0.000 {method 'tolist' of 'numpy.ndarray' objects}
# без numpy плюсом еще время на генерацию массива через for
#      1000    0.002    0.000    0.004    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.004    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)

# На 100000 и более уже не стал тестировать, т.к. очень долго ждать.
cProfile.run('func(10000)')     #   10278 function calls in 5.235 seconds,
# без numpy 62953 function calls in 5.061 seconds
#        1    0.000    0.000    5.235    5.235 task_1(old).py:19(func)
#        1    5.230    5.230    5.233    5.233 task_1(old).py:29(func_2)
#        1    0.001    0.001    0.001    0.001 task_1(old).py:45(func_3)
#        1    0.001    0.001    0.001    0.001 task_1(old).py:60(func_4)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:74(func_5)
#        1    0.000    0.000    0.000    0.000 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
#        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        1    0.000    0.000    0.000    0.000 {method 'tolist' of 'numpy.ndarray' objects}
# без numpy плюсом еще время на генерацию массива через for
#     10000    0.011    0.000    0.022    0.000 random.py:200(randrange)
#     10000    0.006    0.000    0.028    0.000 random.py:244(randint)
#     10000    0.007    0.000    0.011    0.000 random.py:250(_randbelow_with_getrandbits)

cProfile.run('func(20000)')     #   20509 function calls in 20.161 seconds,
# без numpy 125596 function calls in 22.591 seconds
#        1    0.000    0.000   20.160   20.160 task_1(old).py:19(func)
#        1   20.150   20.150   20.155   20.155 task_1(old).py:29(func_2)
#        1    0.002    0.002    0.002    0.002 task_1(old).py:45(func_3)
#        1    0.003    0.003    0.003    0.003 task_1(old).py:60(func_4)
#        1    0.000    0.000    0.000    0.000 task_1(old).py:74(func_5)
#        1    0.000    0.000    0.000    0.000 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
#        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        1    0.000    0.000    0.000    0.000 {method 'tolist' of 'numpy.ndarray' objects}
# без numpy плюсом еще время на генерацию массива через for
#     20000    0.026    0.000    0.050    0.000 random.py:200(randrange)
#     20000    0.013    0.000    0.063    0.000 random.py:244(randint)
#     20000    0.017    0.000    0.025    0.000 random.py:250(_randbelow_with_getrandbits)


"""
Выводы: 
1. Генерация списка - тоже время. Не удалость установить постоянную зависимость от выбранного метода генерации списка.
Пока обнаружено, что прямо влияет на кол-во function calls. Время с numpy уменьшается не постоянно, не в каждой попытке.
2. Append быстрее добавление в список через сложение.
3. Определили, что уже на этапе func(1000) сильно выбивается внутренняя функция func_2. Важно оптимизировать ее. 
4. Общий итог: время работы при увеличении объема в 10 раз увеличивается в 2,5 раза.
Кажется, что здесь квадратичная сложность О(n**2), т.к. 2 вложенных цикла, и на больших объемах (1000 -> 10000 -> 20000)
видно, что при увеличении в n раз время увеличивается в n*n.
но с ростом объемя разница между предыдущим временем выполнения и текущим сокращается, например,
начинается от в 3 раза и на 10000 время становится уже на в 1,3 раза увеличение, но возможно
это похоже на O(n*log(n)), где относительный вклад уменьшается с ростом n, но возможно это ошибочно, т.к. это заметно
только от перехода от маленьких данных к большим.
"""

# ---------------------------------------------------------------------

# Для обоих последующих вариантов сделаем оптимизации:
# Генерация массива с помощью numpy
# Замена array = array + [] на array.append()

# 2 вариант. Оптимизация: убрать 2 цикла, заменить на while и записать все в словарь (не плодим списки).
# Также сократить кол-во массивов и других циклов для нахождения списка часто повторяющихся чисел.

# def func(SIZE):
#     MIN_ITEM = 0
#     MAX_ITEM = 100
#     array = numpy.random.randint(MIN_ITEM, MAX_ITEM, SIZE).tolist()
#     # array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     # print(array)
#
#     # считаем какие числа встречаются чаще и как часто, записываем результаты в словарь
#     result = {}
#     def func_2(array):
#         n = 0
#         while n < len(array):
#             if array[n] in result:
#                 result[array[n]] += 1
#             else:
#                 result[array[n]] = 1
#             n += 1
#         return result
#     result = func_2(array)
#     # print(result)
#
#
#     # ищем максимальные значения в словаре
#     def func_3(result):
#         other_max_num_list = []
#         max_count = 1
#         max_num = 0
#         for key, value in result.items():
#             if value > max_count:
#                 max_count = value
#                 max_num = key
#             elif value == max_count:
#                 other_max_num_list.append(key)
#         return other_max_num_list, max_count, max_num
# #     other_max_num_list, max_count, max_num = func_3(result)
# #     print(f'Чаще всего встречается число - {max_num}, Другие числа с этой же частотой: {other_max_num_list}')
# #     return other_max_num_list, max_count, max_num
# #
# # func(100)
#
# print(timeit.timeit('func(10)', number=100, globals=globals()))         # 0.005311482000000006
# print(timeit.timeit('func(100)', number=100, globals=globals()))        # 0.009067771000000002
# print(timeit.timeit('func(1000)', number=100, globals=globals()))       # 0.057542096000000015
# print(timeit.timeit('func(10000)', number=100, globals=globals()))      # 0.537547702
# print(timeit.timeit('func(100000)', number=100, globals=globals()))     # 5.7161077659999995
# print(timeit.timeit('func(1000000)', number=100, globals=globals()))    # 63.747687472
# print(timeit.timeit('func(10000000)', number=100, globals=globals()))   # 591.686613611
#
# cProfile.run('func(10)')      #          27 function calls in 0.001 seconds
# #        1    0.000    0.000    0.000    0.000 task_1.py:187(func)
# #        1    0.000    0.000    0.000    0.000 task_1.py:196(func_2)
# cProfile.run('func(100)')     #          117 function calls in 0.000 seconds
# #        1    0.000    0.000    0.000    0.000 task_1.py:187(func)
# #        1    0.000    0.000    0.000    0.000 task_1.py:196(func_2)
# cProfile.run('func(1000)')    #          1017 function calls in 0.001 seconds
# #        1    0.000    0.000    0.001    0.001 task_1.py:187(func)
# #        1    0.001    0.001    0.001    0.001 task_1.py:196(func_2)
# cProfile.run('func(10000)')   #          10017 function calls in 0.007 seconds
# #        1    0.000    0.000    0.007    0.007 task_1.py:187(func)
# #        1    0.005    0.005    0.006    0.006 task_1.py:196(func_2)
# cProfile.run('func(100000)')  #          100017 function calls in 0.075 seconds
# #        1    0.000    0.000    0.074    0.074 task_1.py:187(func)
# #        1    0.057    0.057    0.070    0.070 task_1.py:196(func_2)
# #        1    0.002    0.002    0.003    0.003 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.002    0.002    0.002    0.002 {method 'tolist' of 'numpy.ndarray' objects}
# cProfile.run('func(1000000)')  #          1000017 function calls in 0.747 seconds
# #        1    0.001    0.001    0.744    0.744 task_1.py:187(func)
# #        1    0.580    0.580    0.707    0.707 task_1.py:196(func_2)
# #        1    0.018    0.018    0.018    0.018 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.017    0.017    0.017    0.017 {method 'tolist' of 'numpy.ndarray' objects}
# cProfile.run('func(10000000)')  #          10000017 function calls in 7.608 seconds
# #        1    0.009    0.009    7.577    7.577 task_1.py:187(func)
# #        1    5.937    5.937    7.231    7.231 task_1.py:196(func_2)
# #        1    0.166    0.166    0.166    0.166 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.170    0.170    0.170    0.170 {method 'tolist' of 'numpy.ndarray' objects}

"""
Видим линейную зависимость O(n). Увеличиваем в 10 раз объем данных, в 10 раз примерно увеличивается время выполнения.
Относительно первого варианта сразу видим, что примерно за то же самое время в первом варианте 10000-20000 объем, 
во втором 10 млн объем данных (размер списка).
"""

# 3й вариант. Заменим while на for.

# def func(SIZE):
#     MIN_ITEM = 0
#     MAX_ITEM = 100
#     array = numpy.random.randint(MIN_ITEM, MAX_ITEM, SIZE).tolist()
#     # array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     # print(array)
#
#     # считаем какие числа встречаются чаще и как часто, записываем результаты в словарь
#     result = {}
#
#     def func_2(array):
#         for n in array: # range(len(array)) - с range дольше на 20-30%
#             if n in result:
#                 result[n] += 1
#             else:
#                 result[n] = 1
#         return result
#     result = func_2(array)
#     # print(result)
#
#
#     # ищем максимальные значения в словаре
#     def func_3(result):
#         other_max_num_list = []
#         max_count = 1
#         max_num = 0
#         for key, value in result.items():
#             if value > max_count:
#                 max_count = value
#                 max_num = key
#             elif value == max_count:
#                 other_max_num_list.append(key)
#         return other_max_num_list, max_count, max_num
#     other_max_num_list, max_count, max_num = func_3(result)
#     # print(f'Чаще всего встречается число - {max_num}, Другие числа с этой же частотой: {other_max_num_list}')
#     return other_max_num_list, max_count, max_num
#
# # func(100)
#
# print(timeit.timeit('func(10)', number=100, globals=globals()))         # 0.0036338739999999814
# print(timeit.timeit('func(100)', number=100, globals=globals()))        # 0.007018330999999989
# print(timeit.timeit('func(1000)', number=100, globals=globals()))       # 0.02920872699999999
# print(timeit.timeit('func(10000)', number=100, globals=globals()))      # 0.20707798800000005
# print(timeit.timeit('func(100000)', number=100, globals=globals()))     # 2.466057012
# print(timeit.timeit('func(1000000)', number=100, globals=globals()))    # 27.175816785000002
# print(timeit.timeit('func(10000000)', number=100, globals=globals()))   # 260.792290854
#
# cProfile.run('func(10)')        #     28 function calls in 0.000 seconds
# #        1    0.000    0.000    0.000    0.000 task_1.py:271(func)
# #        1    0.000    0.000    0.000    0.000 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# cProfile.run('func(100)')       #     22 function calls in 0.000 seconds
# #        1    0.000    0.000    0.000    0.000 task_1.py:271(func)
# #        1    0.000    0.000    0.000    0.000 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# cProfile.run('func(1000)')      #     21 function calls in 0.000 seconds
# #        1    0.000    0.000    0.000    0.000 task_1.py:271(func)
# #        1    0.000    0.000    0.000    0.000 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# cProfile.run('func(10000)')     #     20 function calls in 0.002 seconds
# #        1    0.000    0.000    0.002    0.002 task_1.py:271(func)
# #        1    0.002    0.002    0.002    0.002 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# cProfile.run('func(100000)')    #         18 function calls in 0.025 seconds
# #        1    0.000    0.000    0.025    0.025 task_1.py:271(func)
# #        1    0.022    0.022    0.022    0.022 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# #        1    0.001    0.001    0.002    0.002 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.001    0.001    0.001    0.001 {method 'tolist' of 'numpy.ndarray' objects}
# cProfile.run('func(1000000)')   #         18 function calls in 0.248 seconds
# #        1    0.001    0.001    0.244    0.244 task_1.py:271(func)
# #        1    0.211    0.211    0.211    0.211 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# #        1    0.016    0.016    0.016    0.016 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.016    0.016    0.016    0.016 {method 'tolist' of 'numpy.ndarray' objects}
# cProfile.run('func(10000000)')  #         18 function calls in 2.804 seconds
# #        1    0.012    0.012    2.777    2.777 task_1.py:271(func)
# #        1    2.407    2.407    2.407    2.407 task_1.py:280(func_2)
# #        1    0.000    0.000    0.000    0.000 task_1.py:291(func_3)
# #        1    0.171    0.171    0.172    0.172 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
# #        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
# #        1    0.187    0.187    0.187    0.187 {method 'tolist' of 'numpy.ndarray' objects}


"""
Общий вывод.
Во 2 и 3м варианте на 10 и 100 почти одинаковое время (или при 100 в 2 раза дольше).
Начиная с 1000 идет увеличение почти (+-) в 10 раз.
Вариант 3 быстрее второго примерно в 2 раза. 
За счет цикла for вместо while (как минимум не нужен счетчик в виде переменной).
Вспомогательные циклы, функции, например генерация массива, могут замедлять общее выполнение алгоритма.
Итог: 
Вариант 1. Нелинейная (квадратичная) зависимость.
Вариант 2. Линейная зависимость, работает быстрее 1го.
вариант 3. Линейная зависимость (в 10 раз увеличили объем, в 10 раз возросло время выполнения), работает быстрее 2го. 
И быстрее 1го примерно в 170 раз при одном и том же объеме.
Потому что нет вложенных циклов, работаем с 1 словарем и 2 списками,
меньше циклов (всего 2 из всей задачи, вместо 5-6 изначальных). 
Проходимся по всему циклу один раз. Дальше уже по результатам прохода. В изначальном варианте было 2 обхода по одному
и тому же циклу (2 вложенных цикла).
"""