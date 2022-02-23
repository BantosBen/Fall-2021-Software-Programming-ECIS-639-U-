import numpy as np

raw_data = np.loadtxt("ex_5_4-data.csv")
processed = raw_data.copy()
processed[processed < 0] = 0
np.savetxt("ex_5_4-processed.csv", processed, fmt='%.2e')
