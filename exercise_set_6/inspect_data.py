""" inspect_data.py"""
import pandas as pd

# Assure that the weather-ann-arbor.csv file is in the same directory with this
# module and run the module.
#
# Afterward, you will be able to experiment with the df variable using the
# interactive prompt.
df = pd.read_csv('weather-ann-arbor.csv', parse_dates=['Date'])
df = df[df['Element'] == 'TMIN'].min()['ID']
print(type(df))