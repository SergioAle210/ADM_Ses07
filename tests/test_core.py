"""Pruebas unitarias de los resultados y errores de la librería matemática."""

import unittest

from basic_math import factorial, gcd, is_prime, lcm, square


class TestSquare(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(square(3), 9)

    def test_negative_integer(self):
        self.assertEqual(square(-4), 16)

    def test_decimal(self):
        self.assertEqual(square(2.5), 6.25)

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_incompatible_types_raise_type_error(self):
        for value in ("3", None, [], 2 + 0j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    square(value)

    def test_booleans_raise_type_error(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    square(value)


class TestFactorial(unittest.TestCase):
    def test_factorial_of_three(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_negative_integer_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_nonintegers_raise_type_error(self):
        for value in (2.5, "5", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    factorial(value)

    def test_booleans_raise_type_error(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    factorial(value)


class TestIsPrime(unittest.TestCase):
    def test_two_is_prime(self):
        self.assertTrue(is_prime(2))

    def test_odd_prime(self):
        self.assertTrue(is_prime(17))

    def test_odd_composite_is_not_prime(self):
        self.assertFalse(is_prime(9))

    def test_even_composite_is_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_perfect_square_is_not_prime(self):
        self.assertFalse(is_prime(49))

    def test_values_below_two_are_not_prime(self):
        for value in (-7, 0, 1):
            with self.subTest(value=value):
                self.assertFalse(is_prime(value))

    def test_nonintegers_raise_type_error(self):
        for value in (2.5, "17", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    is_prime(value)

    def test_booleans_raise_type_error(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    is_prime(value)


class TestGcd(unittest.TestCase):
    def test_common_divisor(self):
        self.assertEqual(gcd(12, 18), 6)

    def test_coprime_integers(self):
        self.assertEqual(gcd(7, 5), 1)

    def test_negative_integers_give_positive_result(self):
        for a, b in ((-12, 18), (12, -18), (-12, -18)):
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), 6)

    def test_one_zero_argument(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_both_arguments_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_invalid_first_argument_raises_type_error(self):
        for value in ("12", 2.5, None, True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    gcd(value, 18)

    def test_invalid_second_argument_raises_type_error(self):
        for value in ("18", 2.5, None, True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    gcd(12, value)

    def test_zero_does_not_hide_invalid_argument(self):
        for value in ("5", 2.5, None, True, False):
            for a, b in ((0, value), (value, 0)):
                with self.subTest(a=a, b=b):
                    with self.assertRaises(TypeError):
                        gcd(a, b)


class TestLcm(unittest.TestCase):
    def test_common_multiple(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_coprime_integers(self):
        self.assertEqual(lcm(3, 5), 15)

    def test_negative_integers_give_positive_result(self):
        for a, b in ((-4, 6), (4, -6), (-4, -6)):
            with self.subTest(a=a, b=b):
                self.assertEqual(lcm(a, b), 12)

    def test_one_zero_argument(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)

    def test_both_arguments_zero(self):
        self.assertEqual(lcm(0, 0), 0)

    def test_invalid_first_argument_raises_type_error(self):
        for value in ("4", 2.5, None, True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    lcm(value, 6)

    def test_invalid_second_argument_raises_type_error(self):
        for value in ("6", 2.5, None, True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    lcm(4, value)

    def test_zero_does_not_hide_invalid_argument(self):
        for value in ("5", 2.5, None, True, False):
            for a, b in ((0, value), (value, 0)):
                with self.subTest(a=a, b=b):
                    with self.assertRaises(TypeError):
                        lcm(a, b)


if __name__ == "__main__":
    unittest.main()
