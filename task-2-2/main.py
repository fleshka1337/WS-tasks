from math import sqrt, atan

class ConvertError(Exception):
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

    def __str__(self):
        return f"Комплексное число должно быть ненулевым. Действительная часть = {self.real}. Мнимая часть = {self.imagine}"

class ComplexNumber:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

        if real == 0 and imagine == 0:
            raise ConvertError(real, imagine)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imagine ** 2)

    def __str__(self):
        return f"{self.real} + {self.imagine}i"

    def convert(self):
        magnitude = abs(self)
        angle = atan(self.real / self.imagine)
        return f"{magnitude}(cos({angle}) + sin({angle}))"

def main():
    try:
        num = ComplexNumber(0, 0)
        print(num.convert())
    except ConvertError as e:
        print(e)

    try:
        num = ComplexNumber(2, 0)
        print(num.convert())
    except ZeroDivisionError:
        print("Перевод невозможен - нулевая мнимая часть")

    num = ComplexNumber(2, 2)
    print(f"Комплексное число 1: {num}")
    print(f"Комплексное число 1 в тригонометрической форме: {num.convert()}")

if __name__ == "__main__":
    main()
