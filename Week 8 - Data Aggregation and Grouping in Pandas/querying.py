import pandas as pd

# Load the Nigerian students dataset
students_df = pd.read_csv('../data/students.csv')

# Using query() method for more readable filtering
science_experts = students_df.query('Chemistry >= 85 or class_level == "SS2"')
print("\nSS2 students with 85+ in Chemistry:")
print(science_experts[['first_name', 'last_name', 'class_level', 'Chemistry']].head())

# Use "!=" not-equal-to symbol
female_students = students_df.query("gender != 'M'")
print("\nFemale Students")
print(female_students[['first_name', 'last_name', 'gender']].head())

# Find column value in array
not_in_classes = students_df.query('class_level.isin(["SS1", "SS3"])')
print("\nStudents in SS1 and SS3")
print(not_in_classes[['first_name', 'last_name', 'class_level']].head())

# Negation
not_ss1_students = students_df.query('not (class_level == "SS1")')
print("\nNot SS1 Students")
print(not_ss1_students[['first_name', 'last_name', 'class_level']].head())

# Negate on multiple conditions
ss2_math_performers = students_df.query('not ((class_level == "SS2") and (Mathematics >= 80))')
print("\nSS2 students with high maths performance")
print(ss2_math_performers[['first_name', 'last_name', 'class_level', 'Mathematics']].head())

# Negate with the sigil (~) operator for Series
not_in_classes = students_df.query('~class_level.isin(["SS1", "SS3"])')
print("\nStudents not in SS1 and SS3")
print(not_in_classes[['first_name', 'last_name', 'class_level']].head())

# String Operations
print('')
first_names_with_D = students_df.query('first_name.str.startswith("D")')
print("\nStudent first names that start with the letter 'D'")
print(first_names_with_D[['first_name', 'last_name', 'class_level']].head())

print('')
father_occupation = students_df.query('father_occupation.str.contains("Engineer", na=False)')
print("\nStudents whose father's occupation that contains the word 'Engineer'")
print(father_occupation[['first_name', 'last_name', 'father_occupation']].head())

print('')
first_names_not_with_D = students_df.query('not first_name.str.startswith("D")')
print("\nStudents whose first name does not that start with the letter 'D'")
print(first_names_with_D[['first_name', 'last_name', 'class_level']].head())

print('')
father_occupation = students_df.query('not father_occupation.str.contains("Engineer", na=False)')
print("\nStudents whose father's occupation does not contain the word 'Engineer'")
print(father_occupation[['first_name', 'last_name', 'father_occupation']].head())

print('')