from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Функция для сложения двух чисел
def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)  # Вывод: 15 (1 + 2 + 3 + 4 + 5)
