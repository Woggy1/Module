import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        """Факторіал 0 повинен бути 1"""
        self.assertEqual(factorial(0), 1)

    def test_positive_number(self):
        """Перевірка факторіалу для позитивного числа"""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_large_number(self):
        """Перевірка факторіалу для великого числа"""
        self.assertEqual(factorial(10), 3628800)

    def test_negative_number(self):
        """Факторіал негативного числа повинен викликати помилку"""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        """Факторіал дробового числа повинен викликати помилку"""
        with self.assertRaises(ValueError):
            factorial(2.5)

if __name__ == "__main__":
    unittest.main()
