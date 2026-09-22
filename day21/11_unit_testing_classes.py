class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b


# What is unit testing?
# Unit testing is a software testing technique where individual units or components of a software application are tested in isolation to ensure that they function correctly.
# The goal of unit testing is to validate that each unit of the software performs as expected and meets its specified requirements.
# Unit tests are typically automated and written by developers to verify the correctness of their code.
# They help catch bugs early in the development process.

# Testing
import unittest


class TestCalculator(unittest.TestCase):
    # Set up the test environment
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(10, 20)

        self.assertEqual(result, 30)  # Check if the result is equal to 30

    def test_divide(self):
        result = self.calculator.divide(10, 2)

        self.assertEqual(result, 5)  # Check if the result is equal to 5
        # Check if dividing by zero raises a ValueError
        self.assertRaises(ValueError, self.calculator.divide, 10, 0)

        # Another way to check for exceptions using a context manager
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def tearDown(self):
        # Clean up the test environment
        del self.calculator


# Run the tests
if __name__ == "__main__":
    unittest.main()
