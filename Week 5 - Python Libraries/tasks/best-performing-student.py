import os
import csv
from pprint import pprint
import statistics

STUDENT_DATA_FILE = os.path.abspath('Week 5 - Python Libraries/files/students_record.csv')
CLASS_REPORT_FILE = os.path.abspath('Week 5 - Python Libraries/files/class_report.txt')

def loadStudentData(filename):
    """Load student data from a CSV file into a list of dictionaries."""

    students = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for key in row:
                if key in ['age', 'grade_level', 'math_score', 'science_score', 'english_score', 'history_score']:
                    row[key] = int(row[key])

                if key == 'attendance_rate':
                    # Convert attendance to percentage values
                    row[key] = float(row[key]) * 100

            students.append(row)

    return students

def mapScoreToGradeLetter(score):
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

def normalizeStudentsRecord(students, max_score = 100, target_max = 25):
    """Normalize student scores to a 0-25 scale."""
    for student in students:
        student['english_score'] = (student['english_score'] / max_score) * target_max
        student['history_score'] = (student['history_score'] / max_score) * target_max
        student['math_score'] = (student['math_score'] / max_score) * target_max
        student['science_score'] = (student['science_score'] / max_score) * target_max

        student['total_score'] = student['english_score'] + student['history_score'] + student['math_score'] + student['science_score']
        student['grade'] = mapScoreToGradeLetter(student['total_score'])

    return students


def calculateStatistics(students):
    """Calculate statistical measures for student scores."""

    # "List comprehension" to extract scores and attendance rates
    scores = [student['total_score'] for student in students]
    attendance = [student['attendance_rate'] for student in students]

    stats = {
        'scores': {
            'mean': statistics.mean(scores),
            'median': statistics.median(scores),
            'std_dev': statistics.stdev(scores) if len(scores) > 1 else 0,
            'min': min(scores),
            'max': max(scores)
        },
        'attendance': {
            'mean': statistics.mean(attendance),
            'median': statistics.median(attendance)
        },
    }
    
    return stats


def getStudentTotalScore(student):
    return student['total_score']


def getBestPerformingStudent(students):
    """Returns the best performing student using the total score"""
    # bestStudent = max(students, key = lambda student:student['total_score'])
    bestStudent = max(students, key = getStudentTotalScore)

    return f"{bestStudent['first_name']} {bestStudent['last_name']}"


def generateClassReport(students):
    with open(CLASS_REPORT_FILE, 'w') as file:
        file.write("CLASS REPORT\n")
        file.write("=" * 50 + "\n\n")

        stats = calculateStatistics(students)
        studentRecog = getBestPerformingStudent(students)

        # Statistics
        file.write("CLASS STATISTICS\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Number of Students: {len(students)}\n")
        file.write(f"Score Mean: {stats['scores']['mean']:.2f}\n")
        file.write(f"Score Median: {stats['scores']['median']}\n")
        file.write(f"Score Standard Deviation: {stats['scores']['std_dev']:.2f}\n")
        file.write(f"Score Range: {stats['scores']['min']} - {stats['scores']['max']}\n")
        file.write(f"Attendance Mean: {stats['attendance']['mean']:.2f}%\n")
        file.write(f"Attendance Median: {stats['attendance']['median']:.2f}%\n\n")

        # Recognition
        file.write("STUDENT RECOGNITION\n")
        file.write("-" * 50 + "\n")
        file.write(f"Best Performing Student: {studentRecog}\n\n")

        # Individual student details highlight
        file.write("STUDENT DETAILS\n")
        file.write("-" * 50 + "\n")
        file.write(f"{'Name':<24} {'Score':<8} {'Attend':<8} {'Grade':<5}\n")
        file.write("-" * 65 + "\n")
        
        for student in sorted(students, key=lambda x: x['total_score'], reverse=True):
            studentName = student['first_name'] + ' ' + student['last_name']

            file.write(f"{studentName:<24} {student['total_score']:<8} {student['attendance_rate']:<8} "
                    f"{student['grade']:<5}\n")

    print(f"Report saved to {CLASS_REPORT_FILE}")


studentsDict = loadStudentData(STUDENT_DATA_FILE)  

# Generate class report and save to a text file
generateClassReport(normalizeStudentsRecord(studentsDict))
