""" ex_6_0.py """
import pandas as pd


def max_of_sum(ser_a, ser_b):
    """Return the maximum value of the sum of pd.Series types
    ser_a and ser_b
    """
    # TODO: Remove this line and the 'pass' keyword and implement solution
    ser_sum = ser_a.add(ser_b)
    return ser_sum.max()


# What follows is unit test code for your function
# This code will run when you run your Python module
if __name__ == '__main__':
    import unittest


    class TestMaxOfSum(unittest.TestCase):

        def test_ranges(self):
            ser_a = pd.Series(range(1, 101))
            ser_b = pd.Series(range(101, 201))
            expected = 300
            actual = max_of_sum(ser_a, ser_b)
            self.assertEqual(actual, expected,
                             msg=f'expected {expected} got ')


    unittest.main()
