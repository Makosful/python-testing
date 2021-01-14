import unittest
import calc


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        data = [{'p_one': 10, 'p_two': 5, 'res': 14},
                {'p_one': -1, 'p_two': 1, 'res': 1},
                {'p_one': -1, 'p_two': -1, 'res': -2}, ]
        for d in data:
            with self.subTest(d=d):
                self.assertEqual(calc.add(d.get('p_one'), d.get('p_two')), d.get('res'))

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_subtract_one_negative(self):
        self.assertEqual(calc.subtract(-1, 1), -2)

    def test_subtract_both_negative(self):
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)

    def test_multiply_one_negative(self):
        self.assertEqual(calc.multiply(-1, 1), -1)

    def test_multiply_both_negative(self):
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)

    def test_divide_one_negative(self):
        self.assertEqual(calc.divide(-1, 1), -1)

    def test_divide_both_negative(self):
        self.assertEqual(calc.divide(-1, -1), 1)

    def test_divide_with_remainder(self):
        self.assertEqual(calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
