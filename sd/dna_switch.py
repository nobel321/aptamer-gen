import numpy as np
import pandas as pd
import openpyxl
import csv
import random
import interpreter
import re
import seq_match

parsable_attributes = interpreter.ATTRIBUTES
BROKEN_SEQUENCE = None

target_index = 0
ph_index = 1
affinity_index = 2
buffer_index = 3

data_path = '../data/UTexas Aptamer Database dataset_Sept2023.xlsx'

# Read excel file into dataframe
df = pd.read_excel(data_path)

# Specify the input you are looking for
target = 'Reactive Blue 4'

# Get rows that contain the desired input
target_rows = df[df['Target'].str.contains(target, case=False, na=False)]

# Get pool type
pool_type = target_rows.iloc[0]['Pool Type']
print(type(pool_type), pool_type)

pool_seq = pool_type.strip("5'- -3'")

print(pool_type.strip("5'- -3'"))

BROKEN_SEQUENCE = pool_seq.split('-')

print(BROKEN_SEQUENCE[0])

# get values from other rows
ph_rows = df[df['pH'].astype(str).str.contains(parsable_attributes[ph_index], case=False, na=False)]
affinity_rows = df[df['Affinity'].astype(str).str.contains(parsable_attributes[affinity_index], case=False, na=False)]
# buffer_rows = df[df['Type of the buffer'].astype(str).str.contains(parsable_attributes[buffer_index], case=False, na=False)]

ph_seq = ph_rows.iloc[0]['Aptamer Sequence']
affinity_seq = affinity_rows.iloc[0]['Aptamer Sequence']
# buffer_seq = buffer_rows.iloc[0]['Aptamer Sequence']

ph_constant = ph_rows.iloc[0]['Pool Type']
affinity_constant = affinity_rows.iloc[0]['Pool Type']
# buffer_constant = buffer_rows.iloc[0]['Pool Type']

print(ph_seq, ph_constant, affinity_seq, affinity_constant)

ph_constant, ph_seq = seq_match.extract_between_constant_regions(ph_constant, ph_seq)

BROKEN_SEQUENCE[1] = ph_seq

print(''.join(BROKEN_SEQUENCE))