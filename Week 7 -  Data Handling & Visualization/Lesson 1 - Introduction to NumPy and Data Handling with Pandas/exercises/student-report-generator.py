import pandas as pd
from datetime import datetime
from pprint import pprint

students_df = pd.read_csv('../../files/students_record.csv')

report_date = datetime.now().strftime("%Y-%m-%d")

score_columns = [col for col in students_df.columns.tolist() if '_score' in col]

def assign_grade(score):
    grade = "F"

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"

    return grade

def fill_missing_values(df, column):
    df[column].fillna(students_df[column].mean(), inplace=True)

    return df


def process_data(df, score_cols):
    """Process the data to calculcate the averages, grades, and identify performance patterns."""

    # the axis argument represents the x and y axes where 0 represents the y-axis and 1 represents the x-axis
    df['average_score'] = df[score_cols].mean(axis=1).round(2)

    # Use the 'apply()' method when you need to perform an operation on the row values of a column
    df['letter_grade'] = df['average_score'].apply(assign_grade)

    # Calcuate the class average
    class_average = df['average_score'].mean()

    df['needs_support'] = df['average_score'] < class_average # True or False

    # Calculate subject raking for each student
    for subject in score_columns:
        subject_name = subject.replace('_score', '')
        rank_col = f"{subject_name}_rank"
        
        # Fill in missing values for each subject (e.g: math_score, english_score, etc)
        df = fill_missing_values(df, subject)

        # Calculate the rank of each value in the subject column
        # 'method=min' specifies how to handle ties - if 2 students have the same sc ore, they both get the same rank, and the next student will skip a rank
        # 'ascending=False' makes higher scores get a lower rank - an inverse of how the rank function works by default
        # 'astype(int)' converts the rank values to whole numbers/integers
        df[rank_col] = df[subject].rank(method="min", ascending=False).astype(int)

    return df


def generate_class_profile(df):
    # total students, class average, highest score, lowest score, subject averages, report date, grade percentages,
    # students that need support, gender performance, attendance_correlation
    # age performance, attendance performance
    """Generates a comprehensive class profile with key statistics"""
    
    return {
        'report_date': report_date,
        'total_students': len(df),
        'class_average': df['average_score'].mean(),
        'highest_score': df['average_score'].max(),
        'lowest_score': df['average_score'].min(),
        'grade_distribution': df['letter_grade'].value_counts().to_dict(),

        # 'value_counts(normalize=True) ' counts how many times a letter grade appears and converts such count to proportions of 0 to 1. Eg: If B appears 15 times out of 50 students, B would get a proportion of 0.3
        'grade_percentages': (df['letter_grade'].value_counts(normalize=True) * 100).round(2).to_dict(),
        'students_needing_support': df[df['needs_support']].shape[0],

        'subject_averages':  { col.replace('_score', ''): df[col].mean() for col in score_columns },
        'gender_performance': df.groupby('gender')['average_score'].mean().to_dict(), # { m: 44%, f: 56% }

        # Find out how the average score correlates with attendance_rate
        'attendance_correlation': df['average_score'].corr(df['attendance_rate'])
    }


def get_top_performers(df, subject, count = 3):
    """Get the top N performers in a specific subject, as provided"""
    
    return df.sort_values(subject, ascending=False).head(count)


def generate_performance_by_subject(df):
    """Generate performance summmary by subject area"""
    summary = {}

    for subject in score_columns:
        subject_name = subject.replace('_score', '')

        # Retrieve key subject statistics
        stats = df[subject].describe()

        # Grade distribution for the subject
        df[f"{subject_name}_grade"] = df[subject].apply(assign_grade)
        grade_dist = df[f"{subject_name}_grade"].value_counts().to_dict()

        summary[subject_name] = {
            'average': stats['mean'],
            'median': stats['50%'],
            'min': stats['min'],
            'max': stats['max'],
            'std_dev': stats['std'],
            'grade_distribution': grade_dist,
            'top_students': get_top_performers(df, subject)[['student_id', 'first_name', 'last_name', subject]].to_dict('records'),
        }

    return summary


def write_profile_to_file(df, path):
    "Write generated "

    class_profile = generate_class_profile(df)
    subject_summary = generate_performance_by_subject(df)

    summary = ""

    for (subject, data) in subject_summary.items():
        summary += "\n" + "=" * 50
        summary += f" {subject.upper()} PERFORMANCE SUMMARY "
        summary += "=" * 50

        summary += f"\nAverage Score: {data['average']:.2f}"
        summary += f"\nMedian Score: {data['median']:.2f}"
        summary += f"\nRange: {data['min']} to {data['max']}"
        summary += f"\nStandard Deviation: {data['std_dev']:.2f}"
        summary += "\n"

    return summary

df = process_data(students_df, score_columns)

print(write_profile_to_file(df, ''))

# pprint(generate_performance_by_subject(df))
