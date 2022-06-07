# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый
# тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod


class NotNumber(ValueError):
    pass


class WarehouseGroup:
    def __init__(self):
        self.items = []
        self.count = 0

    def append(self, item):
        self.count += 1
        self.items.append(item)

    def extract(self, i, place):
        try:
            print(f'{self.items[0]} уехал в {place}')
            self.items.pop(i)
            self.count -= 1
        except IndexError:
            print('Недостаточно товара!')

    def __str__(self):
        return f'{self.count} штук: {self.items.__str__()}'


class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        groupName = equipment.group_name()
        arrayOfEquipmentOfGroup = self._dict.setdefault(groupName, WarehouseGroup())
        arrayOfEquipmentOfGroup.append(equipment)

    def extract(self, name, place, count=1):
        if self._dict[name]:
            print(f'Было {self._dict[name]}')
            for i in range(0, count):
                self._dict.setdefault(name).extract(0, place)
            print(f'Осталось {self._dict[name]}')

    @abstractmethod
    def action(self):
        raise NotImplementedError()


class Equipment:
    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.brend} {self.model} {self.year}'


class Printer(Equipment):
    def __init__(self, series, brend, model, year):
        super().__init__(brend, model, year)
        self.series = series

    def __repr__(self):
        return f'{self.brend} {self.series} {self.model} {self.year}'

    @property
    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, brend, model, year):
        super().__init__(brend, model, year)

    @property
    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, brend, model, year):
        super().__init__(brend, model, year)

    @property
    def action(self):
        return 'Копирует'


sklad = Warehouse()
n = 0
while n != 4:
    x = int(input("Введите 1, если хотите добавить сканер, 2 - принтер, 3 - ксерокс, 4 -exit "))
    if x == 1:
        marka = input('Марка: ')
        model = input('Модель: ')
        try:
            year = input('год: ')
            if str.isdigit(year) is True:
                pass
            else:
                raise NotNumber(year)
        except NotNumber as ex:
            print('Не число!', ex)
            year = input('Повторите ввод: ')
        scaner = Scaner(marka, model, year)
        sklad.add_to(scaner)
    elif x == 2:
        printer = Printer(input('Серия: '), input('Марка: '), input('Модель: '), input('год: '))
        sklad.add_to(printer)
    elif x == 3:
        хerox = Xerox(input('Марка: '), input('Модель: '), input('год: '))
        sklad.add_to(хerox)
    else:
        n = 4

sklad.extract('Scaner', 'мастерская', 2)
print(sklad._dict)
