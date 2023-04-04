import os
import sys

import pandas as pd
import glob

files_in = sys.argv[1]

files = glob.glob(files_in)

cleaned_dir = 'cleaned'

if not os.path.exists(cleaned_dir):
    os.mkdir(cleaned_dir)

for file in files:
    df = pd.read_csv(file, sep=';', header=None, skiprows=3, decimal=',', dtype=float)
    df = df.dropna()
    df.columns = ['Zeit (ms)', 'Voltage']
    cleaned_file = os.path.splitext(os.path.basename(file))[0] + "_cleaned.csv"
    cleaned_file = os.path.join(cleaned_dir, cleaned_file)
    df.to_csv(cleaned_file, index=False)
