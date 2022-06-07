# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod

class WarehouseGroup:
    def __init__(self):
        self.items = []
        self.count = 0

    def append(self, item):
        self.count += 1
        self.items.append(item)

    def pop(self, i):
        try:
            self.items.pop(i)
            self.count -= 1
        except IndexError:
            pass

    def __str__(self):
        return f'{self.count} штук: {self.items.__str__()}'

class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        groupName = equipment.group_name()
        arrayOfEquipmentOfGroup = self._dict.setdefault(groupName, WarehouseGroup())
        arrayOfEquipmentOfGroup.append(equipment)

    def extract(self, name, place, count = 1):
        if self._dict[name]:
            print(f'Было {self._dict[name]}')
            for i in range(0, count):
                print(f'{self._dict[name].items[0]} уехал в {place}')
                self._dict.setdefault(name).pop(0)
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
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90)
sklad.add_to(scaner)
scaner = Scaner('hp', '311', 97)
sklad.add_to(scaner)
scaner = Scaner('hp', '330', 99)
sklad.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Scaner', 'мастерская', 2)
print()
print(sklad._dict)
