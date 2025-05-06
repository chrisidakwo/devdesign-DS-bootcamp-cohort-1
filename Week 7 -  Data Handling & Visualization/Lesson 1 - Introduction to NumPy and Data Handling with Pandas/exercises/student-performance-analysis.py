import pandas as pd
import numpy as np
from scipy import stats

def fill_missing_values(df, column):
    # df[column].fillna(students_df[column].mean(), inplace=True)
    df[column] = df[column].fillna(df[column].mean())

    return df

def student_performance_analysis(file_path):
    """
    Analyze student performance data and generate reports.

    Args:
        file_path (str): Path to the student_records.csv file
    """
    # Load the student_records.csv file
    df = pd.read_csv(file_path)
    print(f"Loaded data with {df.shape[0]} students and {df.shape[1]} columns.")

    # Identify score columns (assuming they end with '_score')
    score_columns = [col for col in df.columns if col.endswith('_score')]

    # Calculate each student's average score
    df['average_score'] = df[score_columns].mean(axis=1).round(2)

    # Assign letter grades
    def assign_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    df['letter_grade'] = df['average_score'].apply(assign_grade)

    # Identify top performers in each subject
    top_performers = {}
    for subject in score_columns:
        subject_name = subject.replace('_score', '')

        # Sort and retrieve the top n rows for a column (in this case, a subject column) ordered by the specified columns in descending order.
        top_students = df.nlargest(3, subject)[['student_id', 'first_name', 'last_name', subject]]
        top_performers[subject_name] = top_students

        print(f"\nTop 3 students in {subject_name.capitalize()}:")
        print(top_students)

    # Analyze correlation between attendance and performance
    if 'attendance_rate' in df.columns:
        # Get the correlation coefficient between two variables in the DataFrame: the attendance rate and the average score of students
        attendance_corr = df['attendance_rate'].corr(df['average_score'])
        print(f"\nCorrelation between attendance and average score: {attendance_corr:.4f}")

        # Correlation with individual subjects
        print("\nCorrelation between attendance and individual subjects:")
        for subject in score_columns:
            subject_name = subject.replace('_score', '')
            corr = df['attendance_rate'].corr(df[subject])
            print(f"{subject_name}: {corr:.4f}")

    # Create "Student Report Card" data
    # Add rank for each subject
    for subject in score_columns:
        subject_name = subject.replace('_score', '')
        rank_col = f"{subject_name}_rank"

        # Fill in missing values for each subject (e.g: math_score, english_score, etc.)
        df = fill_missing_values(df, subject)

        # Create a ranking column for each student based on their performance in a subject
        df[rank_col] = df[subject].rank(method='min', ascending=False).astype(int)

    # Generate individual student report cards
    report_cards = []

    # df.iterrows() is a pandas DataFrame method that allows you to iterate through each row of a DataFrame, returning both the index and the row data
    for _, student in df.iterrows():
        report_card = f"""
STUDENT REPORT CARD
===================
Student ID: {student['student_id']}
Name: {student['first_name']} {student['last_name']}
Grade Level: {student['grade_level']}
Gender: {student['gender']}
Age: {student['age']}

ACADEMIC PERFORMANCE
-------------------
"""
        # Add each subject score and rank
        for subject in score_columns:
            subject_name = subject.replace('_score', '').title()
            rank_col = subject.replace('_score', '') + '_rank'
            report_card += f"{subject_name}: {student[subject]} (Rank: {student[rank_col]})\n"

        # Add overall performance
        report_card += f"""
Overall Average: {student['average_score']}
Letter Grade: {student['letter_grade']}
"""

        # Add attendance information if available
        if 'attendance_rate' in student:
            report_card += f"Attendance Rate: {student['attendance_rate']:.2f}\n"

        report_cards.append(report_card)

    # Print first report card as an example
    print("\nExample Student Report Card:")
    print(report_cards[0])

    # Save the processed data to student_report_cards.csv
    df.to_csv("../../../data/student_report_cards.csv", index=False)
    print("\nProcessed data saved to student_report_cards.csv")

    return df, report_cards


def statistical_distribution_analysis():
    """
    Generate and analyze a simulated dataset of test scores.
    """
    # Generate a simulated dataset of 100 test scores
    # Using a slightly right-skewed distribution to simulate typical test scores
    np.random.seed(42)  # For reproducibility
    scores = np.random.normal(75, 12, 100).round(1)

    # Ensure scores are within 0-100 range by "clipping" (or capping) any values that exceed the range boundaries
    scores = np.clip(scores, 0, 100)

    print("\nPART 2: STATISTICAL DISTRIBUTION ANALYSIS")
    print("===========================================")

    # Calculate statistics
    mean_score = np.mean(scores)
    median_score = np.median(scores)

    # Calculate the mode (most frequently occurring value) of the test scores using SciPy's mode() function.
    mode_score = stats.mode(scores)[0]
    std_dev = np.std(scores)

    print(f"Mean: {mean_score:.2f}")
    print(f"Median: {median_score:.2f}")
    print(f"Mode: {mode_score:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    # Identify scores within standard deviations
    within_1_std = np.sum((scores >= mean_score - std_dev) & (scores <= mean_score + std_dev))
    within_2_std = np.sum((scores >= mean_score - 2 * std_dev) & (scores <= mean_score + 2 * std_dev))
    within_3_std = np.sum((scores >= mean_score - 3 * std_dev) & (scores <= mean_score + 3 * std_dev))

    print(f"\nScores within 1 standard deviation of the mean: {within_1_std} ({within_1_std / len(scores):.2%})")
    print(f"Scores within 2 standard deviations of the mean: {within_2_std} ({within_2_std / len(scores):.2%})")
    print(f"Scores within 3 standard deviations of the mean: {within_3_std} ({within_3_std / len(scores):.2%})")

    # Create normalized version of scores (0-1 scale)
    min_score = np.min(scores)
    max_score = np.max(scores)
    normalized_scores = (scores - min_score) / (max_score - min_score)

    print(f"\nNormalized scores (first 5): {normalized_scores[:5]}")

    # Analysis of what the distribution tells about test difficulty
    print("\nANALYSIS OF TEST DIFFICULTY")
    print("===========================")
    print("Based on the statistical analysis of our simulated test scores:")
    print(f"1. The mean score is {mean_score:.2f} with a standard deviation of {std_dev:.2f}.")
    print(
        f"2. The median score is {median_score:.2f}, which is {'higher than' if median_score > mean_score else 'lower than' if median_score < mean_score else 'equal to'} the mean.")

    # Skewness analysis
    # Quantify the distribution of the scores. Does the distribution tend towards a positive or negative value
    skewness = stats.skew(scores)
    print(
        f"3. The distribution has a skewness of {skewness:.4f}, indicating a {'right-skewed' if skewness > 0.5 else 'left-skewed' if skewness < -0.5 else 'relatively symmetric'} distribution.")

    # Difficulty analysis based on mean
    if mean_score > 85:
        difficulty = "The test appears to be relatively easy, with a high average score."
    elif mean_score < 65:
        difficulty = "The test appears to be challenging, with a low average score."
    else:
        difficulty = "The test appears to be of moderate difficulty, with an average score in the middle range."

    print(f"4. {difficulty}")

    # Distribution analysis
    # Percentile tells you what percentage of scores fall below a certain value
    # np.percentile(scores, [25, 50, 75]) calculates three percentiles at once:
    # 25th percentile (First Quartile or Q1): 25% of scores fall below this value
    # 50th percentile (Median or Q2): 50% of scores fall below this value (the middle score)
    # 75th percentile (Third Quartile or Q3): 75% of scores fall below this value
    percentiles = np.percentile(scores, [25, 50, 75])

    # The Inter-quartile Range (IQR) is the difference between the 75th and 25th percentiles (Q3 - Q1). It tells you the range of the middle 50% of your data.
    iqr = percentiles[2] - percentiles[0]
    print(
        f"5. The inter-quartile range (IQR) is {iqr:.2f}, suggesting {'high' if iqr > 30 else 'moderate' if iqr > 15 else 'low'} variability in student performance.")

    print("\nCONCLUSION:")
    if skewness > 0.5:
        conclusion = "The right-skewed distribution indicates the test was challenging for most students, with fewer students achieving high scores."
    elif skewness < -0.5:
        conclusion = "The left-skewed distribution indicates the test was relatively easy for most students, with fewer students receiving low scores."
    else:
        if std_dev < 10:
            conclusion = "The symmetric distribution with low standard deviation suggests a test where most students performed similarly, indicating good test design but possibly limited discrimination between skill levels."
        else:
            conclusion = "The symmetric distribution with substantial standard deviation indicates a well-balanced test that effectively distinguishes between different student ability levels."

    print(conclusion)

    return scores, normalized_scores


# Run both analyses
if __name__ == "__main__":
    # Part 1: Enhanced Student Performance Analysis
    student_performance_analysis("../../files/students_record.csv")

    # Part 2: Statistical Distribution Analysis
    statistical_distribution_analysis()