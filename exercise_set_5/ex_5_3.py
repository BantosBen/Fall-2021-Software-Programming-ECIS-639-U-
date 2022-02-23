import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Read and process data then save it ib a file')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    args = parser.parse_args()

    INFILE = args.infile
    OUTFILE = args.outfile

    raw_data = np.loadtxt(INFILE)

    # TODO: remove the mean from raw_data
    raw_data -= np.mean(raw_data)
    # TODO: scale raw_data so that it has a standard devitation
    # of 1.
    processed = raw_data / np.std(raw_data)
    #
    # SAVE the processed data to a variable called `processed`

    # Here the program saves the processed data to the outfile
    np.savetxt(OUTFILE, processed, fmt='%.2e')
