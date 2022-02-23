""" ex_6_2.py """
import pandas as pd


def filter_year(temp_df, year):
    """Filters rows from the temp for which the "Date" column has year `year`
    Returns the filtered DataFrame
    """

    # TODO: Remove these comments, delete the `pass` keyword and implement the solution
    # NOTE: For testing, the weather-ann-arbor.csv data will be loaded and
    # passed to your function for filtering.
    #
    # Make sure that weather-ann-arbor.csv is in the same directory as this module.
    #
    # Review the column headers in the file and optionally experiment with loading
    # the data yourself with the command:
    # df = pd.read_csv('weather-ann-arbor.csv', parse_dates=['Date'])
    # The `parse_dates` kwarg instructs pandas to convert values in the Date
    # column to pd.datetime types. See tests for a direct example of loading the
    # data
    temp_df = temp_df[temp_df['Date'].dt.year == year]
    return temp_df


if __name__ == '__main__':
    import unittest


    class TestFilterYear(unittest.TestCase):
        temp_df = pd.read_csv('weather-ann-arbor.csv', parse_dates=['Date'])

        def test_return_type(self):
            arg = self.temp_df
            actual = filter_year(arg, 2014)
            self.assertIsInstance(actual, pd.core.frame.DataFrame,
                                  msg='filter_year did not return a DataFrame')

        def test_2014(self):
            arg = self.temp_df
            expected = True
            actual = all(filter_year(arg, 2014)['Date'].dt.year == 2014)
            self.assertEqual(actual, expected,
                             msg='Expected all elements of the returned DF to be from year 2014')


    unittest.main()
