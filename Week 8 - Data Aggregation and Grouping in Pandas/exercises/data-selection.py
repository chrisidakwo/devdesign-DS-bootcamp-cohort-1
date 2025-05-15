import numpy as np
import pandas as pd

def load_student_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)


def filter_by_attendance_rate(df, class_level = 'SS1', min_attendance_rate = 92):
    results = df[
        (df['class_level'] == class_level) &
        (df['attendance'] > min_attendance_rate)
    ]

    return results[['student_id', 'first_name', 'last_name', 'class_level', 'attendance']]

# 'Literature in English'
# 'English Language'

def find_humanities_excellence(df, min_score = 85):
    # TODO: Include an alternative `find_humanities_excellence` function that takes in a subject list and filters the dataframe with those subjects

    results = df[
        (df['English Language'] > min_score) &
        (df['Literature in English'] > min_score) 
    ]

    return results[['student_id', 'first_name', 'last_name', 'English Language', 'Literature in English']]

def find_students_needing_support(df, stem_subjects=None, max_score=70):
    """Find students who might need academic support (those with at least two STEM subjects below 70)"""

    # TODO: Use filter approach, if possible
    # science_students = df[df['study_group'] == 'Science']

    if stem_subjects is None:
        stem_subjects = ['Mathematics', 'Chemistry', 'Biology', 'Physics', 'Computer Science', 'Further Mathematics']

    science_students = df[df['study_group'] == 'Science']

    students = [] # List of students needing support

    # for index, student in df.iterrows():
    for index, student in science_students.iterrows():
        # Count STEM subjects below threshold
        low_subjects = []

        for subject in stem_subjects:
            subject_score = student[subject]

            # if subject in df.columns and pd.notna(subject_score):
            if subject in df.columns:
                if subject_score < max_score:
                    low_subjects.append(subject)


        # If at least two subjects are below the threshold (max_score), add to the list
        if len(low_subjects) >= 2:
            student_info = {
                'student_id': student['student_id'],
                'first_name': student['first_name'],
                'last_name': student['last_name'],
                'low_subjects': ', '.join(low_subjects),
                'low_subjects_count': len(low_subjects),
            }

            students.append(student_info)

    # Convert students list to DataFrame and return
    return pd.DataFrame(students)


def find_potential_math_tutors(df, class_level, min_score):
    """Create a list of potential math tutors (students with Mathematics scores above 90 in SS3)"""
    result = df[
        (df['class_level'] == class_level) &
        (df['Mathematics'] > min_score)
    ]

    return result[['student_id', 'first_name', 'last_name', 'Mathematics']]


def calc_average_score(df):
    """Sort the dataset by average score across all subjects they've taken"""
    subject_columns = [
        'English Language', 'Agriculture', 'Computer Science', 'Mathematics', 'French', 'Government',
        'Civic Education', 'Literature in English', 'Economics', 'Physics', 'Biology', 'History', 'Yoruba',
        'Geography', 'Hausa', 'Further Mathematics', 'Chemistry', 'Igbo'
    ]

    # Dynamically retrieve subjects
    # data_list = df.columns.tolist()
    # Retrieve the last 18 items (reading from the back) and then reverse the result
    # subject_columns_2 = data_list[-1:-19:-1][::-1]

    # Create a copy of the dataframe to avoid warnings and retain initial dataframe
    result_df = df.copy()


    def calculate_student_average(row):
        scores = [row[subject] for subject in subject_columns if pd.notna(row[subject])]

        scores = []
        for subject in subject_columns:
            subject_score = row[subject]
            if pd.notna(subject_score):
                scores.append(subject_score)

        if scores:
            return sum(scores) / len(scores)
        else:
            return np.nan


    result_df['average_score'] = result_df.apply(calculate_student_average, axis=1)

    result_df = result_df.sort_values(by='average_score', ascending=False)

    return result_df


def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../../data/students.csv')

    print('\n================= TASK 1: STUDENTS WITH HIGH ATTENDANCE RATE =================')
    ss1_high_attendance_rate = filter_by_attendance_rate(students_df)
    print(ss1_high_attendance_rate.head())

    print('\n================= TASK 2: STUDENTS EXCELLING IN HUMANITIES =================')
    humanities_excellence = find_humanities_excellence(students_df)
    print(humanities_excellence.head())

    print('\n================= TASK 3: STUDENTS NEEDING ACADEMIC SUPPORT =================')
    students_needing_support = find_students_needing_support(students_df)
    print(f'\nFound {len(students_needing_support)} students needing academic support in STEM subjects')

    print('\n================= TASK 4: POTENTIAL MATH TUTORS =================')
    class_level = 'SS3'
    min_score = 90

    students_low_on_maths = find_potential_math_tutors(students_df, class_level, min_score)
    print(f'\nFound {len(students_low_on_maths)} students that need math tutors in {class_level}, with scores below {min_score}')

    print('\n================= TASK 5: STUDENTS SORTED BY AVERAGE SCORE =================')
    students_with_agg = calc_average_score(students_df)
    top_students = students_with_agg[['first_name', 'last_name', 'average_score']].head(50)
    print(top_students)

    # print('\n')
    # print(students_df[['first_name', 'last_name']].head(3))
    #
    # print('\n')
    # print(students_df.loc[7:15, ['first_name', 'last_name']])
    #
    # print('\n')
    # print(students_df.iloc[0:7, 0:4])


if __name__ == '__main__':
    main()

    