import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_oper_neg(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)

    def test_oper_add01(self):
        """Запуск без переменных"""
        self.assertEqual(calc_me(None, 5, "+"), "ERROR: send me Number1")

    def test_oper_add02(self):
        """Запуск без переменных2"""
        self.assertEqual(calc_me(4, None, "+"), "ERROR: send me Number2")

    def test_oper_add03(self):
        """Принятие символов в переменных Число1 и Число2"""
        self.assertEqual(calc_me('2*9', 3, "+"), "ERROR: now it is does not supported")

    def test_oper_add03_1(self):
        """Принятие символов в переменных Число1 и Число2"""
        self.assertEqual(calc_me(5, '8#5', "+"), "ERROR: now it is does not supported")

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')


if __name__ == '__main__':
    unittest.main(verbosity=2)