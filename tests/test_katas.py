import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        math_result = katas.add(2, 3)
        self.assertEqual(math_result, 5)

    def test_multiply(self):
        math_result = katas.multiply(3, 3)
        negative_result = katas.multiply(1, -2)
        positive_result = katas.multiply(-2, -2)
        self.assertEqual(math_result, 9)
        self.assertEqual(negative_result, -2)
        self.assertEqual(positive_result, 4)

    def test_power(self):
        math_result = katas.power(3, 3)
        negative_result = katas.power(-2, 3)
        self.assertEqual(math_result, 27)
        self.assertEqual(negative_result, -8)

    def test_factorial(self):
        math_result = katas.factorial(3)
        self.assertEqual(math_result, 6)

    def test_fibonacci(self):
        math_result = katas.fibonacci(10)
        self.assertEqual(math_result, 34)


if __name__ == '__main__':
    unittest.main()
