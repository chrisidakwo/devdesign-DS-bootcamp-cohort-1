import pandas as pd

students_df = pd.read_csv('../../data/students.csv')

# Filter with multiple conditions using logical operators
high_performers = students_df[(students_df['Mathematics'] > 85) | (students_df['Physics'] > 75) & (students_df['class_level'] == 'SS1')]

print("Students with 85+ in Mathematics and 75+ in Physics:")
print(high_performers[['first_name', 'last_name', 'study_group', 'class_level', 'Mathematics', 'Physics']].head())


# Using query() method for more readable filtering
science_experts = students_df.query('Chemistry >= 85 and class_level == "SS2"')
print("\nSS2 students with 85+ in Chemistry:")
print(science_experts[['first_name', 'last_name', 'class_level', 'Government', 'Chemistry']].head())