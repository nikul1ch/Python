# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input("Введите значение X = "))
# y = int(input("Введите значение Y = "))
# z = int(input("Введите значение Z = "))
import random

x = random.choice([True, False])
y = random.choice([True, False])
z = random.choice([True, False])

print(x)
print(y)
print(z)

print(~(x or y or z) == ~x and ~y and ~z)
