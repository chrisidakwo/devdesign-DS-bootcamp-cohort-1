import pandas as pd

columns = ['student_id', 'first_name', 'class_level', 'gender']

def load_student_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)


def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../data/students.csv')
    gender_groups = students_df.groupby('gender')

    # Calculate mean scores for each gender
    gender_performance = gender_groups[['Mathematics', 'English Language', 'Physics', 'Chemistry']].mean()
    print("Average scores by gender:")
    print(gender_performance)

    # Multiple aggregations at once
    gender_stats = gender_groups['Mathematics'].agg(['mean', 'min', 'max', 'count', 'std'])
    print("\nMath statistics by gender:")
    print(gender_stats)

    print('\n\n')

    # Group by multiple columns
    level_gender_groups = students_df.groupby(['class_level', 'gender'])
    level_gender_performance = level_gender_groups['Mathematics'].mean()
    print("\nAverage math score by class level and gender:")
    print(level_gender_performance)

    print('\n\n')

    # Group by class level
    class_groups = students_df.groupby('class_level')

    # Count of students in each class level
    print("Number of students per class level:")
    print(class_groups.size())

    # Mean of all numeric columns by class level
    print("\nAverage values by class level:")
    print(class_groups[[
        'English Language', 'Agriculture', 'Computer Science', 'Mathematics', 'French', 'Government',
        'Civic Education', 'Literature in English', 'Economics', 'Physics', 'Biology', 'History', 'Yoruba',
        'Geography', 'Hausa', 'Further Mathematics', 'Chemistry', 'Igbo',
    ]].mean())

    # Custom aggregations per column
    custom_agg = {
        'attendance': ['min', 'max', 'mean'],
        'Mathematics': ['mean', 'median', 'std'],
        'English Language': ['mean', 'median', 'std'],
        'Chemistry': ['max', 'median', 'count'],
    }
    class_analysis = class_groups.agg(custom_agg)
    print("\nCustom aggregations by class level:")
    print(class_analysis)


if __name__ == '__main__':
    main()
