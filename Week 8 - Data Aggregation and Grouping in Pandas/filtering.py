import pandas as pd

# Load the Nigerian students dataset
students_df = pd.read_csv('../data/students.csv')

# Filter with multiple conditions using logical operators
maleFinalist = students_df[(students_df['class_level'] == 'SS3') & (students_df['gender'] == 'M')]
print('\n\nMale Finalists (Male students in SS3 class):')
print(maleFinalist[['first_name', 'last_name', 'study_group', 'class_level']].head())

print('\n\n')
high_performers = students_df[
    (students_df['Mathematics'] > 85) & 
    (students_df['Physics'] > 75)
]
print("Students with 85+ in Mathematics and 75+ in Physics:")
print(high_performers[['first_name', 'last_name', 'study_group', 'Mathematics', 'Physics']].head())

# Students who excel in either Mathematics OR English Language
maths_or_english = students_df[
    (students_df['Mathematics'] > 90) | 
    (students_df['English Language'] > 90)
]
print("\n\nStudents with 90+ in either Mathematics or English Language:")
print(maths_or_english[['first_name', 'last_name', 'Mathematics', 'English Language']].head())

# ~ The sigil symbol is used for negation
print('\n')
# not_science_students = students_df[students_df['study_group'] != 'Science']

not_science_students = students_df[~(students_df['study_group'] == 'Science')]
print(not_science_students[['first_name', 'last_name', 'study_group']].head())

print("\n\nList of science students")
print(not_science_students[['first_name', 'last_name', 'study_group']].head())
# print('\n\nNumber of science students', not_science_students.shape)
# print('Length of science students:', len(not_science_students.index), 'rows')

# Student whose mother are Carpenters, Teachers, and Bankers
selected_occupation = students_df[students_df['mother_occupation'].isin(['Carpenter', 'Teacher', 'Banker'])]
print("\n\nStudent whose mother are Carpenters, Teachers, and Bankers:")
print(selected_occupation[['first_name', 'last_name', 'mother_occupation']].head(50))
print('How many?', len(selected_occupation.index))

# String Operations

print('\n\n')
starts_with_n = students_df[students_df['last_name'].str.startswith('N')]
# starts_with_n = starts_with_n[starts_with_n['class_level'] == 'SS1']

# Below is an example of how string filter operations can be joined
# students_df[
#     (students_df['first_name'].str.startswith('A')) & 
#     (students_df['father_occupation'].str.contains('Doctor', na=False))
# ]

# Below is another example of a string methods that searches data in the `father_occupation` column for values that contain the word 'Engineer'
# na=False tells the method to, by default, exlude rows with NaN or non-string column value
# students_df[students_df['father_occupation'].str.contains('Engineer', na=False)]

print('\nHow many students have their last name starting with N?', len(starts_with_n.index))
print('')
starts_with_n = starts_with_n.sort_values('last_name')
print(starts_with_n[['first_name', 'last_name', 'class_level']].head(10))

print("\nLast name contains the string partial 'du'")
# You can use the 'case' argument to determine if the search should be case-sensitive or not
# case=True means that the search should be case-sensitive, while case=False means that the search should not be case-sensitive
str_contains = students_df[students_df['last_name'].str.contains('DU', case=False)]
print(str_contains[['first_name', 'last_name', 'class_level']].head(50))

# Regex - Regular Expressions

# Basic Regex Filtering
# Filter names that start with 'A' or 'O'
name_pattern = r'^[AO]'
students_with_a_or_o = students_df[students_df['first_name'].str.match(name_pattern)]
print("Students with names starting with A or O:")
print(students_with_a_or_o[['first_name', 'last_name']].head())

print('\n')

# Find names containing 'ola' anywhere in the name (case insensitive)
ola_pattern = r'ola'
ola_names = students_df[students_df['first_name'].str.contains(ola_pattern, case=False, regex=True)]
print("\nStudents with 'ola' in their name (case insensitive):")
print(ola_names[['first_name', 'last_name']].head())

print('\n')

# Filter students with traditional Nigerian name prefixes
prefix_pattern = r'^(Ade|Olu|Obi|Chi)'
traditional_names = students_df[students_df['first_name'].str.match(prefix_pattern, case=False)]
print("\nStudents with traditional name prefixes:")
print(traditional_names[['first_name', 'last_name']].head())

print('\n')

# Regex Filtering on Multiple Columns
# Find students where first name contains 'ch' AND last name ends with 'wu'
ch_pattern = r'ch'
wu_pattern = r'wu$'
ch_wu_students = students_df[
    students_df['first_name'].str.contains(ch_pattern, case=False, regex=True) &
    students_df['last_name'].str.contains(wu_pattern, case=False, regex=True)
]
print("\nStudents with 'ch' in first name and last name ending with 'wu':")
print(ch_wu_students[['first_name', 'last_name']].head())

# Extracting data using capture groups

# Capture groups are a powerful regex feature that let you extract specific parts of a string pattern. 
# Here are examples demonstrating how to use capture groups to extract data:

# Extract first letter of first name
students_df['first_initial'] = students_df['first_name'].str.extract(r'^([A-Z])')
print("Extracted first initials:")
print(students_df[['first_name', 'first_initial']].head())

print('\n')

# Extracting Multiple Groups
# Extract first and last letter of name
students_df[['first_letter', 'last_letter']] = students_df['first_name'].str.extract(r'^([A-Za-z]).*([A-Za-z])$')
print("\nFirst and last letters of names:")
print(students_df[['first_name', 'first_letter', 'last_letter']].head())

print('\n')

# NOTE: See the regex-resources.md file for links to resources on Regex
