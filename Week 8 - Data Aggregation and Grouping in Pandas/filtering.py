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
# TODO: Errors when filter expressions are joined
starts_with_n = students_df[students_df['last_name'].str.startswith('N')]
# starts_with_n = starts_with_n[starts_with_n['class_level'] == 'SS1']

# TODO: use another example of a string methods

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
# TODO: Include code for pattern matching with regex and links to resources for reading-up on regex

# Extract with capture groups
# TODO: Include code sample and some explanation

print('\n')
