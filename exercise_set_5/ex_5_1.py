import argparse
from ex_5_0 import line_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read file and print number of lines')
    parser.add_argument('infile')
    args = parser.parse_args()
    line_count(args.infile)
