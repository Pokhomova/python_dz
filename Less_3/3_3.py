# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    data = [var_1, var_2, var_3]
    sorted(data)
    data.remove(1)
    return (sum(data))
print(my_func(2, 1, 4))
