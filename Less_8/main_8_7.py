# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + bi'

    def __add__(self, other):
        print(f'Сумма комплексных чисел {z_1} и {z_2}')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел {z_1} и {z_2}')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
