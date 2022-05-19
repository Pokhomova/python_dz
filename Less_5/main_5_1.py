# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print("введите что-нибудь")
with open("text1.txt", "w") as write_f:
    while True:
        my_var = input()
        if my_var == '':
            break
        write_f.write(my_var + '\n')
write_f.close()
