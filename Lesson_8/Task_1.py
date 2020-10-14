"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
Пример:
строка: рара
подстроки:
рар
ра
р
а
ар
ара
Итог: 6 подстрок
"""


import hashlib
import random

n = random.randrange(100)
alpha = "abcdefghijklmnopqrstuvwxyz "
s = ""
for i in range(n):
    g = random.randrange(27)
    s += alpha[g]

r = set()

N = len(s)
for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print("Количество различных подстрок в строке '%s' равно %d" % (s, len(r)))
