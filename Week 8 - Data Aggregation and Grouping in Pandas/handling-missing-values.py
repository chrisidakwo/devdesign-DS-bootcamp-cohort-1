import numpy as np
import pandas as pd
import random

np.random.seed(13)  # For reproducibility

# Load the Nigerian students dataset
students_df = pd.read_csv('../data/students.csv')

# You can copy a Pandas dataframe into a new variable. Changes made to the copy will not affect the parent/original instance
data_df = students_df.copy()

random_indices = np.random.choice(data_df.index, size=5, replace=False)

data_df.loc[random_indices, 'Mathematics'] = np.nan

# Check for missing values
print("Missing values in each column:")
print(data_df.isnull().sum())

# Fill missing values with mean of the column
data_df['Mathematics'] = data_df['Mathematics'].fillna(data_df['Mathematics'].mean())
print("\nAfter filling missing values:")
print(data_df.isnull().sum())

print('\nMissing values for the Mathematics column:')
print(data_df['Mathematics'].isnull().sum())


