"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
Для извлечения цифр числа используйте арифм. операции
Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

n = int(input("Введите натуральное число:"))
cn = 0
nc = 0
while n > 0:
    if n % 2 == 0:
        cn += 1
    else:
        nc += 1
    n = n//10
print(f"Четных числе в числе: {cn}, нечетных: {nc}")


# попробуем рекрсией


def recursion(n,cn,nc):
    if n == 0:
        print(f"Четных числе в числе: {cn}, нечетных: {nc}")
    else:
        if n % 2 == 0:
            recursion(n//10, cn+1, nc)
        else:
            recursion(n//10, cn, nc+1)

n = int(input("Введите натуральное число:"))

recursion(n, 0, 0)
