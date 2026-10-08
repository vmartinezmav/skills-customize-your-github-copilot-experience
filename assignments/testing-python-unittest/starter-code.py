import unittest


def add(first_number: int, second_number: int) -> int:
    return first_number + second_number


def is_even(number: int) -> bool:
    return number % 2 == 0


def calculate_discount(price: float, discount_percent: float) -> float:
    return price * discount_percent / 100


class TestBasicFunctions(unittest.TestCase):
    def test_adds_two_numbers(self):
        # TODO: Test add with positive and negative values.
        pass

    def test_detects_even_and_odd_numbers(self):
        # TODO: Test even, odd, and zero values with assertTrue/assertFalse.
        pass


class TestCalculateDiscount(unittest.TestCase):
    def test_calculates_regular_discount(self):
        # TODO: Check the final price after a regular discount.
        pass

    def test_handles_zero_and_full_discount(self):
        # TODO: Check 0% and 100% discounts.
        pass


if __name__ == "__main__":
    unittest.main()