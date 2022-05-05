# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

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

print(int_func(input("введите слова из маленьких латинских букв: ")))