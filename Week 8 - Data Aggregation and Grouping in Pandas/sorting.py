import pandas as pd

# Load the Nigerian students dataset
students_df = pd.read_csv('../data/students.csv')

# Basic selection methods
print("First 5 rows:")
print(students_df.head())

print('\n')

# Selecting specific columns
scores = students_df[['first_name', 'last_name', 'English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology']]
print("\nScore columns only:")
print(scores.head(20))

print('\n\n')
# Sort by a single column (Mathematics scores from highest to lowest)

print('SORTED BY FIRST NAME\n')
fname_sort = students_df.sort_values('first_name')
print(fname_sort[['first_name', 'last_name', 'English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology']].head(20))

print('\nSORTED BY FIRST NAME AND LAST NAME\n')
fl_name_sort = students_df.sort_values(['first_name', 'last_name', 'English Language'])
print(fl_name_sort[['first_name', 'last_name', 'English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology']].head(20))



# Sort by multiple columns (class level, then Mathematics score)
# sorted_multi = students_df.sort_values(['class_level', 'Mathematics'], 
#                                        ascending=[True, False])

# sorted_by_math = students_df.sort_values('Mathematics', ascending=False)


# print("Top math students:")
# print(sorted_by_math[['first_name', 'last_name', 'Mathematics']].head())