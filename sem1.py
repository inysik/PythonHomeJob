#1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
n=int(input("enter num от 1 до 7:"))
if n==1 or n==2 or n==3 or n==4 or n==5:
    print("будни")
else:
    print("выходной")




#2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

if not (X or Y or Z) == (not X and not Y and not Z):
    print("True")
else:
    print("False")


#3 Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x=int(input("enter :"))
y=int(input("enter :"))


if x>0 and y>0:
    print("точка в первой чтверти")
else:
    if x<0 and y>0:
        print("точка находится во 2 четверти")
    else:
        if x<0 and y<0:
         print("точка в 3 чтверти")
        else:
                if x>0 and y<0:
                  print("точка в 4 четверти")
                else:
                     print("точка в начале координатных линий")


#4 Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).


x=int(input("enter четверть :"))

if x==1:
    print("точка принадлежит диапазону от 0 до плюс бесконечности по х и от ноля до плюс бесконечности по у")
else:
    if x==2:
      print("точка принадлежит диапазону от минус бесконечности до ноля х и от ноля до плюс бесконечности по у")      
    else:
              if x==3:
                     print("точка принадлежит диапазону отминус бесконечности до 0 х и отминус бесконечности до ноля по у")
              else:
                           if x==4:
                              print("точка принадлежит диапазону от 0 до плюс бесконечности по х и от ноля до минус бесконечности по у")
                           else:
                                     print("такой четверти не существует")

#5 Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x1=int(input("enter :"))
y1=int(input("enter :"))
x2=int(input("enter :"))
y2=int(input("enter :"))



num=(x1-x2)**2+(y1-y2)**2
sqrt = math.sqrt(num)
print(num)