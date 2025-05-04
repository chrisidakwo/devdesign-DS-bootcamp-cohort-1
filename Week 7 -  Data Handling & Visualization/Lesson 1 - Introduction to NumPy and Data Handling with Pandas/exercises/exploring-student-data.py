import pandas as pd
from pprint import pprint

print('\n')
print('Loading students records from CSV...')

students_df = pd.read_csv('../../files/students_record.csv')

print('\n============== DATA EXPLORATION ==============')

(rows, columns) = students_df.shape

print(f"\n{rows} rows, {columns} columns")

print('\n------ COLUMN NAMES ------')
pprint(students_df.columns.tolist())

print('\n------ DATA TYPES ------')
pprint(students_df.dtypes)

print(students_df.head())

print('\n Missing values in each column')
print(students_df.isnull().sum())

print('\n============== BASIC STATISTICS ==============')

# subject_columns = []
# for col in students_df.columns:
#     if '_score' in col:
#         subject_columns.append(col)

subject_columns = [col for col in students_df.columns.tolist() if '_score' in col]

print(students_df.describe())

students_df['average_score'] = students_df[subject_columns].mean(axis=1).round(2)

top_students = students_df.sort_values('average_score', ascending=False).head(5)

print('\n------ TOP 5 STUDENTS ------')
print(top_students[['student_id', 'first_name', 'last_name', 'average_score']])


print('\n============== PASS/FAIL STATUS ==============')

def determine_pass_or_fail(score):
    return score > 75

    # if score > 75:
    #     return True
    # else
    #     return False

    # return True if score > 75 else False

students_df['pass_fail'] = students_df['average_score'].apply(determine_pass_or_fail)

pass_fail_counts = students_df['pass_fail'].value_counts()

print(
    'Pass Percentage:',
    (pass_fail_counts[True] / len(students_df) * 100).round(2)
)

def calculate_pass_percentage(group):
    """
    Counts how many students have True in their pass_fail column, divides by the total number of students in that grade (or group), and multiplies by 100 to get a percentage
    """

    # pass_count = (group == True).sum()

    # Although the commented code above gives you the same result as the code below, the one below is a preferred and safer means
    # of getting the count of students with True in their respective pass_fail column.
    # It's even more self-explanatory than the one above
    pass_count = group.value_counts().get(True, 0)

    pass_percentage = (pass_count / len(group)) * 100
    return round(pass_percentage, 2)


grade_level_groups = students_df.groupby('grade_level')['pass_fail']
grade_level_pass = grade_level_groups.apply(calculate_pass_percentage)
print(grade_level_pass.to_dict())

grade_level_avg = students_df.groupby('grade_level')['average_score'].mean().round(2)
print('\n------ AVERAGE SCORE BY GRADE LEVEL ------')
print(grade_level_avg)

# students_df.to_csv('../../files/students_updated_record.csv', index=False)