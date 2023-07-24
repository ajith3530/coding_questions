class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"real({self.x} + imaginary({self.y}))"


complex_1 = Complex(1, 2)
complex_2 = Complex(1, 3)
complex_3 = complex_1 + complex_2

print(complex_3)

