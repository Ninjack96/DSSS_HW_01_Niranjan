import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operators = {'+','-','*'}
        for _ in range(1000):
            result = function_B()
            self.assertIn(result, operators)

    def test_function_C(self):
            test_cases = [
                (4, 2, '+', '4 + 2', 6),
                (6, 3, '-', '6 - 3', 3),
                (9, 2, '*', '9* 2', 18)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = function_C(num1, num2, operator)
                self.assertEqual(PROBLEM, expected_problem) 
                self.assertEqual(ANSWER, expected_answer)

if __name__ == "__main__":
    unittest.main()
