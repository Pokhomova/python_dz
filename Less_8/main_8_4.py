# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class Sklad:
    def __init__(self):
        self._dict = {}


class Equipment:
    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        self.year = year
        self.group = self.__class__.__name__

    def __repr__(self):
        return f'{self.brend} {self.model} {self.year}'

    @abstractmethod
    def action(self):
        raise NotImplementedError()


class Printer(Equipment):
    def __init__(self, series, brend, model, year):
        super().__init__(brend, model, year)
        self.series = series

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


sklad = Sklad()
