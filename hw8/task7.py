"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real: float, imag: float = 0):
        self.real = float(real)
        self.imag = float(imag)

    def as_tuple(self):
        return self.real, self.imag

    def __str__(self):
        return f"{self.real:n}{self.imag:+n}i"

    def __add__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)


c = Complex(0) + Complex(1, -1) + 3
assert c.as_tuple() == (4, -1)
print(c)
c = Complex(1, 3) * Complex(2, 1)
assert c.as_tuple() == (-1, 7)
print(c)
