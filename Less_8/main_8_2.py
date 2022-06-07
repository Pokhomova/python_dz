# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, divider):
        self.divisible = (divider)


divider = int(input("Введите делитель: "))
divisible = int(input("Введите делимое: "))

try:
    if divider == 0:
        raise OwnError("Делимое не должно быть нулем!")
except OwnError as err:
    print(err)
