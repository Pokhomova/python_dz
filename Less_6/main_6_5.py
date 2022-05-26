# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов
# и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки!'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это{self.title}. Пишем ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это{self.title}. Рисуем карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Это{self.title}. Выделяем маркером'


p1 = Pen('Ручка')
p2 = Pencil('Карандаш')
p3 = Handle('Маркер')
print(p1.draw())
print(p2.draw())
print(p3.draw())
