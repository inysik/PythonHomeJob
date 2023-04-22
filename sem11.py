# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0


import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def f(x):
    return -12 * x**4 * np.sin(np.cos(x)) - 18 * x**3 + 5 * x**2 + 10 * x - 30

# Находим корни
roots = np.roots([-12, 0, 0, 5, 10, -30])
print("Корни уравнения f(x) = 0: ", roots)

# Находим интервалы возрастания и убывания
df = lambda x: -48 * x**3 * np.cos(np.cos(x)) + 12 * x**3 * np.sin(x) * np.sin(np.cos(x)) - 54 * x**2 + 10
critical_points = np.roots([df(1), df(2), df(3), df(4), df(5)])
intervals = np.split(np.sort(critical_points), np.where(np.diff(np.sign(df(critical_points))))[0] + 1)
increasing_intervals = []
decreasing_intervals = []
for interval in intervals:
    if df(interval[0]) > 0:
        increasing_intervals.append(interval)
    else:
        decreasing_intervals.append(interval)
print("Интервалы возрастания: ", increasing_intervals)
print("Интервалы убывания: ", decreasing_intervals)

# Строим график функции
x_values = np.linspace(-5, 5, 1000)
y_values = f(x_values)
plt.plot(x_values, y_values)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x)')
plt.show()

# Вычисляем вершину параболы
coefficients = [-12, 0, 0, 5, 10, -30]
a = coefficients[0]
b = coefficients[3]
c = coefficients[4]
vertex_x = -b / (2 * a)
vertex_y = f(vertex_x)
print("Вершина параболы: ({}, {})".format(vertex_x, vertex_y))

# Определяем промежутки, на которых f > 0 и f < 0
positive_intervals = []
negative_intervals = []
for interval in intervals:
    if f(interval[0]) > 0:
        positive_intervals.append(interval)
    else:
        negative_intervals.append(interval)
print("Промежутки, на которых f > 0: ", positive_intervals)
print("Промежутки, на которых f < 0: ", negative_intervals)
