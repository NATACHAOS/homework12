import math

factorial = 1  # факториал через for
num = int(input("Введите число: "))
for i in range(1, num + 1):
    factorial *= i
print(factorial)

factorial = 1  # факториал через while
count = 1
num = int(input("Введите число: "))
while count <= num:
    factorial *= count
    count += 1
print(factorial)


def factorial(num):  # факториал с помощью рекурсии
    if num == 0: return 1
    return num * factorial(num - 1)


num = int(input("Введите число: "))

print(factorial(num))
