# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите значение X отличное от нуля = "))
y = int(input("Введите значение Y отличное от нуля = "))

if x == 0 or y == 0:
    print("Одно или оба числа равны нулю. Запустите программу повторно")
elif x > 0 and y > 0:
    print("Точка с координатами (", x, ";", y,
          ") находится в первой четверти плоскости")
elif x < 0 and y > 0:
    print("Точка с координатами (", x, ";", y,
          ") находится во второй четверти плоскости")
elif x < 0 and y < 0:
    print("Точка с координатами (", x, ";", y,
          ") находится в третьей четверти плоскости")
else:
    print("Точка с координатами (", x, ";", y,
          ") находится в четвёртой четверти плоскости")
