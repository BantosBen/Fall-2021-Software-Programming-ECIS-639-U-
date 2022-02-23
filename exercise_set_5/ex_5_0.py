def line_count(infile):
    file = open(infile, 'r')
    num_of_lines = len(file.readlines())
    print(num_of_lines)
    file.close()
