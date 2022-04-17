# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input("Введите число: ")
number_count = int(user_number) + \
               int(user_number + user_number) + \
               int(user_number + user_number + user_number)
print(number_count)
