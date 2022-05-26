# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Поехали!'

    def stop(self):
        return f'Остановка'

    def turn(self, direction):
        return f'Машина повернула' + direction

    def show_speed(self):
        return f'Ого! {self.speed}км/ч'


class TownCar(Car):

    def __init__(self, speed, color, name, with_baby=True):
        super().__init__(speed, color, name)
        self.with_baby = with_baby

    def show_speed(self):
        if self.speed > 60:
            return f'Притормози  {self.name} - слишком быстро'
        else:
            return f"Ого! {self.speed}км/ч"


class WorkCar(Car):
    def __init__(self, speed, color, name, taxi=True):
        super().__init__(speed, color, name)
        self.taxi = taxi

    def show_speed(self):
        if self.speed > 40:
            return f'Притормози  {self.name} - слишком быстро'
        else:
            return f'Ого! {self.speed}км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmv = SportCar(100, 'Blue', 'bmv', True)
zap = TownCar(90, 'White', 'zap')
VAZ = WorkCar(70, 'Red', 'VAZ', True)
ford = PoliceCar(110, 'Black', 'Ford', True)
print(f'В 15:15 {bmv.turn(" Направо")}, в 15:34 {zap.turn(" Налево")}, а VAZ {VAZ.turn(" Направо")}')
print(f'{VAZ.go()}  {VAZ.show_speed()}')
print(f'{zap.name}  {zap.color}')
print(f'В {zap.name} есть детское кресло? {zap.with_baby}')
print(f'{VAZ.name} полицейская машина? {VAZ.is_police}')
print(f'{ford.name}  полицейская машина? {ford.is_police}')
print(ford.show_speed())
print(bmv.show_speed())
print(ford.show_speed())
