import unittest

from math import isclose
from main import *

class TestComplexNumber(unittest.TestCase):
    #Проверяем правильность комплексного числа
    def test_absolute_value(self):
        num = ComplexNumber(3, 4)
        self.assertTrue(isclose(abs(num), 5.0, rel_tol=1e-9))

    #Проверяем правльность строки
    def test_str_representation(self):
        num = ComplexNumber(2, 3)
        self.assertEqual(str(num), "2 + 3i")
    
    #Проверяем правильность cos и sin
    def test_convert_to_trigonometric(self):
        num = ComplexNumber(1, 1)
        trig_representation = num.convert()
        self.assertTrue("cos" in trig_representation)
        self.assertTrue("sin" in trig_representation)

    #Проверяем на исключение 
    def test_invalid_complex_number(self):
        with self.assertRaises(ConvertError) as context:
            ComplexNumber(0, 0)
        self.assertEqual(str(context.exception), "Комплексное число должно быть ненулевым. Действительная часть = 0. Мнимая часть = 0")

if __name__ == "__main__":
    unittest.main()