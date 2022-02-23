''' ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- TODO: shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`

See also TODO items below.
'''
import numpy as np

if __name__ == '__main__':
    INFILE = 'ex_5_2-data.csv'
    OUTFILE = 'ex_5_2-processed.csv'

    raw_data = np.loadtxt(INFILE)

    # TODO: remove the mean from raw_data
    raw_data -= np.mean(raw_data)
    # TODO: scale raw_data so that it has a standard devitation
    # of 1.
    processed = raw_data/np.std(raw_data)
    #
    # SAVE the processed data to a variable called `processed`

    # Here the program saves the processed data to the outfile
    np.savetxt(OUTFILE, processed, fmt='%.2e')
