
# Вычислить число c заданной точностью d.
# Пример:
#     при d = 0.001,π = 3.141    10^(-1)≤d≤10^(-10).
# '''

import random
from math import pi

d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input("Integer: "))
for i in range(1, number+1):
    if (number % i == 0):
        print(i)


# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
res = []
n = [4, 5, 4, 5, 6, 7, 7, 2, 3, 12, 33, 55]
for i in n:
    if n.count(i) == 1:
        res += [i]
print(res)

# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
