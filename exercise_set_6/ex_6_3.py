""" ex_6_3.py """
import pandas as pd


def station_with_lowest_low(temp_df):
    """Filter the temp_df appropriately and return the ID (str) of the
    station with the lowest low temperature overall"""

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
    min_temp = temp_df[temp_df['Element'] == 'TMIN'].min()['ID']
    return min_temp


if __name__ == '__main__':
    import unittest

    class TestStationLow(unittest.TestCase):

        temp_df = pd.read_csv('weather-ann-arbor.csv', parse_dates=['Date'])

        def test_return_type(self):
            """Assert that the function returns a string type"""
            actual = station_with_lowest_low(self.temp_df)
            self.assertIsInstance(actual, str,
                                  msg=f'Expected type: str. Received type: {type(actual)}')

        def test_correct_station_id(self):
            """assert that the function returns the station
            with the lowest low temp (TMIN element)"""
            expected = 'USC00200032'
            actual = station_with_lowest_low(self.temp_df)
            self.assertEqual(actual, expected,
                             msg=f'Expected {expected} but received {actual}')

        def test_correct_station_id_reduced(self):
            arg = self.temp_df[self.temp_df.Date.dt.year == 2009]
            expected = 'USC00200032'
            actual = station_with_lowest_low(arg)
            self.assertEqual(actual, expected,
                             msg=f'Expected {expected} but received {actual}')

    unittest.main()


