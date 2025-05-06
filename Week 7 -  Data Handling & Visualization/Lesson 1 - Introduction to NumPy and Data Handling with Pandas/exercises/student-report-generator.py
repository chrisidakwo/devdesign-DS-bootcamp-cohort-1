import pandas as pd
from datetime import datetime
from fpdf import FPDF

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
    # df[column].fillna(students_df[column].mean(), inplace=True)
    df[column] = df[column].fillna(students_df[column].mean())

    return df


def process_data(df, score_cols):
    """Process the data to calculate the averages, grades, and identify performance patterns."""

    # the axis argument represents the x and y axes where 0 represents the y-axis and 1 represents the x-axis
    df['average_score'] = df[score_cols].mean(axis=1).round(2)

    # Use the 'apply()' method when you need to perform an operation on the row values of a column
    df['letter_grade'] = df['average_score'].apply(assign_grade)

    # Calculate the class average
    class_average = df['average_score'].mean()

    df['needs_support'] = df['average_score'] < class_average # True or False

    # Calculate subject raking for each student
    for subject in score_columns:
        subject_name = subject.replace('_score', '')
        rank_col = f"{subject_name}_rank"
        
        # Fill in missing values for each subject (e.g: math_score, english_score, etc.)
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
    """Generate performance summary by subject area"""
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
            'top_students': get_top_performers(df, subject, 5)[['student_id', 'first_name', 'last_name', subject]].to_dict('records'),
        }

    return summary


def format_class_profile_report(class_profile):
    """Format the class profile report for proper display"""

    profile = "\n" + ("=" * 10)
    profile += " CLASS PERFORMANCE PROFILE "
    profile += "=" * 10

    profile += f"\nReport Date: {class_profile['report_date']}"
    profile += f"\nTotal Students: {class_profile['total_students']}"

    profile += f"\n\nPERFORMANCE METRICS"
    profile += f"\nClass Average: {class_profile['class_average']:.2f}"
    profile += f"\nHighest Score: {class_profile['highest_score']:.2f}"
    profile += f"\nLowest Score: {class_profile['lowest_score']:.2f}"
    
    profile += f"\n\nGRADE DISTRIBUTION"
    for (grade, count) in sorted(class_profile['grade_distribution'].items()):
        percentage = class_profile['grade_percentages'][grade]
        profile += f"\n{grade}: {count} students ({percentage}%)"

    profile += f"\n\nSUBJECT AVERAGES"
    for (subject, avg) in class_profile['subject_averages'].items():
        profile += f"\n{subject.title()}: {avg:.2f}"

    profile += f"\n\nSTUDENTS NEEDING SUPPORT"
    profile += f"\n{class_profile['students_needing_support']} students ({(class_profile['students_needing_support'] / class_profile['total_students'] * 100):.1f}% of total class students)"

    if class_profile['gender_performance']:
        profile += f"\n\nPERFORMANCE BY GENDER"
        for (gender, avg) in class_profile['gender_performance'].items():
            profile += f"\n{gender}: {avg:.2f}"

    if class_profile['attendance_correlation'] is not None:
        profile += f"\n\nATTENDANCE CORRELATION"

        corr = class_profile['attendance_correlation']

        profile += f"\nThe correlation between attendance rate and students' performance is {corr:.2f}."

        if corr > 0.7:
            profile += "\nThe value shows strong positive correlation, meaning that higher attendance rate is strongly associated with better performance."
        elif corr > 0.4:
            profile += "\nThe value shows moderate positive correlation, meaning that higher attendance is somewhat associated with better performance."
        elif corr > 0.2:
            profile += "\nThe value shows weak positive correlation, meaning that higher attendance has a slight association with better performance."
        else:
            profile += "\nThe value shows little to no correlation, meaning that attendance does not appear strongly related to performance."

    profile += "\n"

    return profile


def format_subject_performance_report(subject_summary, students_len):
    """Format the subject performance report for proper display"""

    summary = ""

    for (subject, data) in subject_summary.items():
        summary += "\n" + ("=" * 10)
        summary += f" {subject.upper()} PERFORMANCE SUMMARY "
        summary += "=" * 10

        summary += f"\nAverage Score: {data['average']:.2f}"
        summary += f"\nMedian Score: {data['median']:.2f}"
        summary += f"\nRange: {data['min']} to {data['max']}"
        summary += f"\nStandard Deviation: {data['std_dev']:.2f}"

        summary += "\n\nGrade Distribution"
        for grade, count in sorted(data['grade_distribution'].items()):
            percentage = (count / students_len) * 100
            summary += f"\n{grade}: {count} students ({percentage:.1f}%)"

        summary += "\n\nTop Performing Students:"
        for i, student in enumerate(data['top_students'], 1):
            summary += f"\n{i}. {student['first_name']} {student['last_name']} (ID: {student['student_id']}): {student[subject+'_score']:.0f}"

        summary += "\n"

    return summary


def output_to_file(path, content, file_type = "txt"):
    """
    Write the provided content to the provided file path, depending on the specified file type.
    """

    if file_type == "txt":
        with open(path, 'w') as file:
            file.write(content)
    elif file_type == "pdf":
        pdf = FPDF(format="A4")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Helvetica", size=10)

        # Define margins and line height
        line_height = 5
        left_margin = 10

        lines = content.split('\n')

        for line in lines:
            # Handle section headers (lines with many = characters)
            if '=' in line and len(line) - len(line.replace('=', '')) > 5:
                if not "class performance profile" in line.lower():
                    pdf.cell(0, 7, "", new_x="LMARGIN", new_y="NEXT")

                line = line.replace('= ', '')
                line = line.replace(' =', '')
                line = line.replace('=', '')
                pdf.set_font("Helvetica", 'B', 12)  # Bold text for headers
                pdf.set_x(left_margin)
                pdf.cell(0, line_height, line, align='L', new_x="LMARGIN", new_y="NEXT")

                pdf.set_font("Helvetica", size=10)  # Reset font
                pdf.cell(0, 5, "", new_x="LMARGIN", new_y="NEXT")
            else:
                # Handle indentation (assumes 2-space indentation for sub lists)
                indent = 0
                if line.startswith('  '):
                    indent = 5
                
                # Add the line to the PDF
                pdf.set_x(left_margin + indent)
                pdf.multi_cell(0, line_height, line)

        pdf.output(path)


def write_to_file(class_profile, subject_summary, path):
    """Format and export the class profile and subjects performance reports to text and PDF files"""

    profile_report_txt = format_class_profile_report(class_profile)
    subject_performance_txt = format_subject_performance_report(subject_summary, class_profile['total_students'])

    full_report = profile_report_txt + subject_performance_txt

    # Write the full report to text file
    output_to_file(path, full_report)

    # Write report to PDF file
    output_to_file('../../../data/reports/class-report.pdf', full_report, 'pdf')


def split_data_by_gender(df):
    """Filters student records by gender and exports each gender group to a separate CSV file."""

    # Get unique gender values
    genders = df['gender'].unique()
    print(f"Found {len(genders)} unique gender values: {genders}")

    # Group by gender and save to separate files
    for gender in genders:
        # Filter the DataFrame for the current gender
        gender_df = df[df['gender'] == gender]
        
        # Create a filename based on gender
        filename = f"student_records_{gender}.csv"
        
        # Export to CSV
        gender_df.to_csv(filename, index=False)
        print(f"Exported {len(gender_df)} records to {filename}")


if __name__ == '__main__':
    # Initialize and process CSV data
    dFrame = process_data(students_df, score_columns)

    # Generate class profile report
    profile_report = generate_class_profile(dFrame)

    # Generate subjects' performance report
    performance_summary = generate_performance_by_subject(dFrame)

    # Generate 
    write_to_file(profile_report, performance_summary, '../../../data/reports/class-report.txt')
