""" ex_6_1.py """
import pandas as pd


def filter_month(ser_a, month):
    """Returns elements of pd.Series `ser_a` which have month
    number `month`."""

    # TODO: Erase these comments and implement the solution
    # See Accessor information in slides and Pandas docs for hints
    ser_a = ser_a[ser_a.dt.month == month]
    return ser_a


# What follows are one or more tests for your function.
# These will be run when you run your module from the commandline
# or from IDLE with Run -> Run Module
# Do not edit these lines
if __name__ == '__main__':
    import unittest
    from datetime import datetime


    class TestFilterMonth(unittest.TestCase):
        dates = pd.Series([datetime(2021, m, d) for m in range(1, 13)
                           for d in [1, 15]])

        def test_jan(self):
            arg = self.dates
            expected = True
            actual = all(filter_month(arg, month=1).dt.month == 1)
            self.assertEqual(actual,
                             expected,
                             msg='Expected all return elements to be in January.')

        def test_may(self):
            arg = self.dates
            expected = True
            actual = all(filter_month(arg, month=5).dt.month == 5)
            self.assertEqual(actual,
                             expected,
                             msg='Expected all return elements to be in May.')


    unittest.main()
