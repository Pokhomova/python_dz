# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, str_data):
        self.str_data = str_data

    @staticmethod
    def check_number_date(da_y, mon_th, yea_r):
        if 1 <= da_y <= 31:
            if 1 <= mon_th <= 12:
                if 2022 >= yea_r >= 0:
                    return f'Верно!'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    @classmethod
    def ddmmyyyy(cls, str_data):
        new_date = []

        for i in str_data.split('/'):
            if i != '/': new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    def __str__(self):
        return f'Текущая дата {MyDate.ddmmyyyy(self.str_data)}'

today = MyDate('11/1/2001')
print(today)
print(MyDate.check_number_date(11, 11, 2022))
print(MyDate.check_number_date(11, 13, 2011))
print(MyDate.ddmmyyyy('11/11/2011'))
print(MyDate.ddmmyyyy('11/11/2020'))
print(MyDate.check_number_date(1, 11, 2000))
