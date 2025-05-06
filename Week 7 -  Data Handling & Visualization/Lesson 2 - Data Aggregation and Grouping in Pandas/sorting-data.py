import pandas as pd

students_df = pd.read_csv('../../data/students.csv')

# You can sort a single column (Mathematics scores, for example, from highest to lowest)
sorted_by_math = students_df.sort_values('first_name', ascending=False)

print("\nTop math students:")

# print(sorted_by_math[['student_id', 'first_name', 'last_name', 'class_level', 'Mathematics']].head())
# print('\n')


# Sort by multiple columns (class level, then Mathematics score)
sorted_multi = students_df.sort_values(['class_level', 'Mathematics', 'first_name'], ascending=[False, True, False])
print("\nSorted by class level, then Mathematics score:")
print(sorted_multi[['first_name', 'last_name', 'class_level', 'Mathematics']].head(10))
