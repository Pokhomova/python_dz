# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    red_duration = 7
    yellow_duration = 2
    green_duration = 12

    __color: str = 'red'

    def running(self):
        self.__color = "red"
        print(f'Внимание! {self.__color} режим')
        time.sleep(TrafficLight.red_duration)
        self.__color = "yellow"
        print(f'Внимание! {self.__color} режим ')
        time.sleep(TrafficLight.yellow_duration)
        self.__color = "green"
        print(f'Внимание! {self.__color} режим')
        time.sleep(TrafficLight.green_duration)
        print(f'Я фсе')


cock = TrafficLight();
cock.running()
