# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

str1=str(input())
print(str1)
k=0
for elem in str1:
    if elem.isdigit():
        k += int(elem)
        print(elem)
print("k=" ,k)


# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f
    
    print(f, end=" ")

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline())]
print(result)


