"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


def prime_eratosfen(n):
    prime_lst = [2]
    chek_num = 3
    while len(prime_lst) < n:
        for i in prime_lst:
            if chek_num % i == 0: break
            if i > chek_num ** (1 / 2):
                prime_lst.append(chek_num)
                break
        chek_num += 1
    print("Алгоритм проверки - Решето Эратосфена(новый):", prime_lst[-1])
    return prime_lst[-1]


def prime_direct(n):
    prime_lst = [2]
    chek_num = 3
    while len(prime_lst) < n:
        i = 2
        while chek_num % i:
            if chek_num % i == 0: break
            if i == chek_num - 1: prime_lst.append(chek_num)
            i += 1
        chek_num += 1
    print("Алгоритм проверки - 'в лоб - деление на все числа':", prime_lst[-1])
    return prime_lst[-1]


print("Время расчета 3000-го простого числа")
print("Время расчета:", timeit.timeit("prime_eratosfen(3000)", setup="from __main__ import prime_eratosfen", number=1), "\n")
print("Время расчета:", timeit.timeit("prime_direct(3000)", setup="from __main__ import prime_direct", number=1), "\n")
print("Выводы: сложность алгоритмов одинаковая но алгоритм 'решето эратосфена' позволяет значитеьно сократить кол-во операций и "
      "сократить время реализации алгоритма до 20 раз при расчете 3000-го элемента")
