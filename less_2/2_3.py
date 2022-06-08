# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_seazon = int(input("Введите номер месяца: "))

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if user_seazon in winter: print('Зима!')
if user_seazon in spring: print('Весна!')
if user_seazon in summer: print('Лето!')
if user_seazon in autumn: print('осень!')

user_seazon = int(input("Введите номер месяца: "))

seazon = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seazon.keys():
    if user_seazon in seazon[key]:
        print(key)