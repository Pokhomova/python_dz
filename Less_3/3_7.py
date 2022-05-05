# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().


def int_func(user_str):
    # Проверки
    if not user_str:
        raise ValueError(f'Должна быть не пустая строка')
    if not user_str.isascii():
        raise ValueError(f'Неверный формат {user_str}')
    if not user_str.islower():
        raise ValueError(f'Должны быть только строчные {user_str} ')
    if not user_str.isalpha():
        raise ValueError(f'Должны быть только буквы {user_str} ')

    # Разделяем на 0-й символ и всё остальное (с 1-го и до конца).
    # Первый символ приводим к верхнему регистру.
    # Склеиваем назад.
    head = user_str[0]
    tail = user_str[1:]
    return head.upper() + tail


def int_func_multiple_words(my_string):
    result = ""
    for word in my_string.split(" "):
        if result:
            result += " "
        result += int_func(word)
    return result

my_string = input("введите строку: ")
print(int_func_multiple_words(my_string))