# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = abs(int(input("Введите целое положительное число ")))
max_number = user_number % 10
while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > max_number:
        max_number = user_number % 10
print(max_number)
