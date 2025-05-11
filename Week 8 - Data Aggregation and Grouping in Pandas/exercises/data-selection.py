import pandas as pd

def load_student_data(path):
    "Loads student data from a CSV file specified in the path argument"

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
    results = df[
        (df['English Language'] > min_score) &
        (df['Literature in English'] > min_score) 
    ]

    return results[['student_id', 'first_name', 'last_name', 'English Language', 'Literature in English']]

def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../../data/students.csv')

    print('\n================= TASK 1: STUDENTS WITH HIGH ATTENDANCE RATE =================')
    ss1_high_attendance_rate = filter_by_attendance_rate(students_df)
    print(ss1_high_attendance_rate.head())

    print('\n================= TASK 2: STUDENTS EXCELLING IN HUMANITIES =================')
    humanities_excellence = find_humanities_excellence(students_df)
    print(humanities_excellence.head())


if __name__ == '__main__':
    main()

    