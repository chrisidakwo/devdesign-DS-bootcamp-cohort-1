# Introduction to Python Libraries
## Week 3, Lesson 2

Welcome to Week 3, Lesson 2 of our Python Data Science Bootcamp! Today, we'll explore Python libraries - one of the key elements that make Python such a powerful language for data science.

## What Are Python Libraries?

A Python library is a collection of pre-written code that you can reuse rather than writing it from scratch. Think of libraries as toolboxes filled with specialized tools for specific jobs.

### Why Use Libraries?

1. **Save time**: Don't reinvent the wheel
2. **Reliability**: Libraries are tested by many developers
3. **Optimization**: Libraries often contain optimized implementations of algorithms
4. **Standardization**: Use industry-standard tools that others will recognize

### How to Import Libraries

There are several ways to import libraries in Python:

```python
# Import the entire library
import math

# Import specific functions from a library
from datetime import datetime

# Import with an alias (nickname)
import numpy as np
```

### Standard Library vs. Third-Party Libraries

- **Standard Library**: Comes installed with Python (math, datetime, os, etc.)
- **Third-Party Libraries**: Need to be installed separately (pandas, numpy, matplotlib, etc.)

Let's see a simple example of the power of libraries:

```python
# Calculating standard deviation WITHOUT libraries
numbers = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

# Manual calculation
mean = sum(numbers) / len(numbers)
squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
std_dev = (squared_diff_sum / len(numbers)) ** 0.5

print(f"Standard deviation (manual): {std_dev}")

# WITH the statistics library
import statistics
print(f"Standard deviation (library): {statistics.stdev(numbers)}")
```

## Essential Built-in Libraries for Data Science

Now let's explore some of the most useful built-in libraries for our data science work:

### 1. The Math Module

The `math` module provides access to mathematical functions and constants.

```python
import math

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number (e): {math.e}")

# Rounding functions
print(f"Ceiling of 4.3: {math.ceil(4.3)}")  # 5
print(f"Floor of 4.3: {math.floor(4.3)}")   # 4
print(f"Rounded 4.3: {round(4.3)}")         # 4
print(f"Rounded 4.5: {round(4.5)}")         # 4 (note: Python rounds to even number if exactly halfway)

# Power and logarithms
print(f"2^3: {math.pow(2, 3)}")            # 8.0
print(f"Square root of 16: {math.sqrt(16)}") # 4.0
print(f"Log base 10 of 100: {math.log10(100)}") # 2.0

# Trigonometry (uses radians)
print(f"Sin of 90° = Sin of π/2: {math.sin(math.pi/2)}")  # 1.0
print(f"Cos of 0°: {math.cos(0)}")                        # 1.0

# Converting between degrees and radians
print(f"45° in radians: {math.radians(45)}")              # ~0.785
print(f"1 radian in degrees: {math.degrees(1)}")          # ~57.3
```

#### Example: Using Math for Grade Normalization

```python
import math

def normalize_score(score, max_score=100, target_max=10):
    """Convert scores to a 0-10 scale and round to nearest 0.5"""
    raw_normalized = (score / max_score) * target_max
    # Round to nearest 0.5
    return round(raw_normalized * 2) / 2

student_scores = [87, 92, 65, 100, 74]
normalized_scores = [normalize_score(score) for score in student_scores]
print(f"Original scores: {student_scores}")
print(f"Normalized scores: {normalized_scores}")
```

### 2. The Datetime Module

The `datetime` module helps you work with dates and times.

```python
from datetime import datetime, date, time, timedelta

# Get current date and time
now = datetime.now()
print(f"Current datetime: {now}")

# Creating dates
today = date.today()
print(f"Today's date: {today}")

specific_date = date(2025, 4, 13)
print(f"Specific date: {specific_date}")

# Creating times
current_time = time(hour=15, minute=30, second=45)
print(f"Specific time: {current_time}")

# Creating datetime objects
event_datetime = datetime(2025, 4, 15, 9, 30, 0)
print(f"Event datetime: {event_datetime}")

# Formatting dates and times
formatted_date = now.strftime("%A, %B %d, %Y at %I:%M %p")
print(f"Formatted: {formatted_date}")  # e.g., "Sunday, April 13, 2025 at 10:30 AM"

# Parsing strings into datetimes
date_string = "2025-05-20 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date: {parsed_date}")

# Date arithmetic
tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

next_week = today + timedelta(weeks=1)
print(f"Next week: {next_week}")

# Time differences
exam_date = date(2025, 5, 15)
days_until_exam = (exam_date - today).days
print(f"Days until exam: {days_until_exam}")
```

#### Example: Birthday Calculator

```python
from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    
    # Calculate years
    years = today.year - birthdate.year
    
    # Check if birthday has occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1
    
    # Calculate months
    if today.month >= birthdate.month:
        months = today.month - birthdate.month
    else:
        months = today.month + 12 - birthdate.month
        
    # Check if day of month has occurred
    if today.day < birthdate.day:
        months -= 1
        if months < 0:
            months = 11
    
    # Calculate days
    # Get days in previous month
    if today.month == 1:
        prev_month = 12
        prev_month_year = today.year - 1
    else:
        prev_month = today.month - 1
        prev_month_year = today.year
        
    import calendar
    last_day_of_prev_month = calendar.monthrange(prev_month_year, prev_month)[1]
    
    if today.day >= birthdate.day:
        days = today.day - birthdate.day
    else:
        days = today.day + last_day_of_prev_month - birthdate.day
    
    return years, months, days

# Example usage
birth_date_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

years, months, days = calculate_age(birth_date)
print(f"You are {years} years, {months} months, and {days} days old.")
```

### 3. The Random Module

The `random` module helps generate random numbers and make random selections.

```python
import random

# Random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Random integer in range (inclusive)
random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")

# Random float in range
random_range = random.uniform(10.5, 20.5)
print(f"Random float between 10.5 and 20.5: {random_range}")

# Random choice from a sequence
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
lucky_student = random.choice(students)
print(f"Lucky student: {lucky_student}")

# Multiple random choices (with replacement)
selected_students = random.choices(students, k=3)
print(f"Selected for quiz: {selected_students}")

# Shuffling a list
random.shuffle(students)
print(f"Shuffled student list: {students}")

# Random sample (without replacement)
team = random.sample(students, k=2)
print(f"Team members: {team}")

# Setting a seed for reproducibility
random.seed(42)  # Any number can be used as the seed
print(random.randint(1, 100))  # This will always be the same number when seed is 42
print(random.randint(1, 100))  # This will always be the same number when seed is 42
```

#### Example: Lucky Draw Game

```python
import random

def lucky_draw(students, prizes):
    """Randomly award prizes to students"""
    # Make a copy to avoid modifying the original list
    remaining_students = students.copy()
    results = {}
    
    for prize, count in prizes.items():
        if count > len(remaining_students):
            count = len(remaining_students)
            
        winners = random.sample(remaining_students, count)
        results[prize] = winners
        
        # Remove winners so they don't win multiple prizes
        for winner in winners:
            remaining_students.remove(winner)
            
        if not remaining_students:
            break
            
    return results

# Example usage
students = [
    "Alice", "Bob", "Charlie", "David", "Eve", 
    "Frank", "Grace", "Hannah", "Ivan", "Julia"
]

prizes = {
    "First Prize": 1,
    "Second Prize": 2,
    "Third Prize": 3
}

result = lucky_draw(students, prizes)

for prize, winners in result.items():
    if len(winners) == 1:
        print(f"{prize}: {winners[0]}")
    else:
        print(f"{prize}: {', '.join(winners)}")
```

### 4. The Time Module

The `time` module provides time-related functions.

```python
import time

# Current time in seconds since Jan 1, 1970 (Unix epoch)
current_time = time.time()
print(f"Current timestamp: {current_time}")

# Format local time
local_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(f"Formatted local time: {formatted_time}")

# Sleep/delay execution
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done waiting!")

# Measuring execution time
start_time = time.time()

# Some operation we want to time
for i in range(1000000):
    pass

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
```

#### Example: Timing Code Execution

```python
import time

def time_function(func, *args, **kwargs):
    """Time how long a function takes to run"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
    return result

# Example usage
def find_prime_numbers(n):
    """Find all prime numbers up to n"""
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

primes_100 = time_function(find_prime_numbers, 100)
primes_1000 = time_function(find_prime_numbers, 1000)
```

### 5. The Statistics Module

The `statistics` module provides functions for statistical calculations.

```python
import statistics

data = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

# Central tendency
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

# Measures of spread
std_dev = statistics.stdev(data)  # Sample standard deviation
variance = statistics.variance(data)  # Sample variance
print(f"Standard deviation: {std_dev}")
print(f"Variance: {variance}")

# For population calculations (instead of sample)
pop_std_dev = statistics.pstdev(data)
pop_variance = statistics.pvariance(data)
print(f"Population standard deviation: {pop_std_dev}")
print(f"Population variance: {pop_variance}")

# Quartiles
q1 = statistics.quantiles(data, n=4)[0]  # First quartile
q3 = statistics.quantiles(data, n=4)[2]  # Third quartile
print(f"First quartile: {q1}")
print(f"Third quartile: {q3}")
```

## Applying Libraries to our Student Performance Data Project

Now let's enhance our Student Performance Analyzer by applying these libraries.

### Step 1: Load Student Data

```python
import csv
import os
from datetime import datetime

def load_student_data(filename):
    """Load student data from a CSV file into a list of dictionaries."""
    students = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string values to appropriate types
                for key in row:
                    if key in ['Score', 'Attendance', 'Homework']:
                        row[key] = int(row[key])
                students.append(row)
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Create sample data file if it doesn't exist
def create_sample_data(filename):
    """Create a sample student data file if it doesn't exist."""
    if os.path.exists(filename):
        return
        
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Score', 'Attendance', 'Homework'])
        writer.writerow(['Alice', '92', '95', '90'])
        writer.writerow(['Bob', '85', '88', '82'])
        writer.writerow(['Charlie', '78', '92', '80'])
        writer.writerow(['David', '95', '98', '97'])
        writer.writerow(['Eve', '67', '75', '70'])
        
    print(f"Created sample data file: {filename}")

# Create the sample file
create_sample_data('student_data.csv')

# Load the data
students = load_student_data('student_data.csv')
print(f"Loaded {len(students)} student records.")
```

### Step 2: Add Timestamp and Calculate Days Until Next Grading

```python
from datetime import datetime, timedelta

def add_timestamp_to_report(report, days_to_next_grading=14):
    """Add timestamp and calculate days until next grading period."""
    now = datetime.now()
    next_grading = now + timedelta(days=days_to_next_grading)
    
    report['timestamp'] = now.strftime("%Y-%m-%d %H:%M:%S")
    report['next_grading_date'] = next_grading.strftime("%Y-%m-%d")
    report['days_to_next_grading'] = days_to_next_grading
    
    return report

# Create a basic report
report = {
    'title': 'Student Performance Report',
    'students': students
}

# Add timestamp information
report = add_timestamp_to_report(report)
print(f"Report generated at: {report['timestamp']}")
print(f"Next grading period: {report['next_grading_date']}")
print(f"Days until next grading: {report['days_to_next_grading']}")
```

### Step 3: Use Math Module to Normalize Scores

```python
import math

def normalize_scores(students, max_score=100, target_max=10):
    """Normalize student scores to a 0-10 scale."""
    for student in students:
        raw_normalized = (student['Score'] / max_score) * target_max
        # Round to nearest 0.5
        student['normalized_score'] = round(raw_normalized * 2) / 2
    return students

# Normalize scores
students = normalize_scores(students)

# Display normalized scores
for student in students:
    print(f"{student['Name']}: Original={student['Score']}, Normalized={student['normalized_score']}")
```

### Step 4: Add Statistics Using the Statistics Module

```python
import statistics

def calculate_statistics(students):
    """Calculate statistical measures for student scores."""
    scores = [student['Score'] for student in students]
    attendance = [student['Attendance'] for student in students]
    homework = [student['Homework'] for student in students]
    
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
        'homework': {
            'mean': statistics.mean(homework),
            'median': statistics.median(homework)
        }
    }
    
    return stats

# Calculate statistics
stats = calculate_statistics(students)

# Display statistics
print("\nClass Statistics:")
print(f"Score Mean: {stats['scores']['mean']:.2f}")
print(f"Score Median: {stats['scores']['median']}")
print(f"Score Standard Deviation: {stats['scores']['std_dev']:.2f}")
print(f"Score Range: {stats['scores']['min']} - {stats['scores']['max']}")
print(f"Attendance Mean: {stats['attendance']['mean']:.2f}%")
print(f"Homework Mean: {stats['homework']['mean']:.2f}%")
```

### Step 5: Use Random to Select Star Students

```python
import random

def select_random_students(students, num_to_select=1):
    """Randomly select students for recognition."""
    if num_to_select > len(students):
        num_to_select = len(students)
        
    return random.sample(students, num_to_select)

# Select student of the day
student_of_the_day = select_random_students(students)[0]
print(f"\nStudent of the Day: {student_of_the_day['Name']}")

# Select team for class presentation
presentation_team = select_random_students(students, 2)
team_names = [student['Name'] for student in presentation_team]
print(f"Presentation Team: {', '.join(team_names)}")
```

### Step 6: Time the Execution of our Analysis

```python
import time

def time_analysis():
    """Time how long the entire analysis takes."""
    start_time = time.time()
    
    # All analysis steps
    students = load_student_data('student_data.csv')
    students = normalize_scores(students)
    stats = calculate_statistics(students)
    report = {'title': 'Student Performance Report', 'students': students, 'statistics': stats}
    report = add_timestamp_to_report(report)
    student_of_the_day = select_random_students(students)[0]
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"\nAnalysis completed in {execution_time:.4f} seconds")

# Time the analysis
time_analysis()
```

### Step 7: Putting It All Together - Complete Student Performance Analyzer

```python
import csv
import os
import time
import math
import random
import statistics
from datetime import datetime, timedelta

def create_student_performance_report(data_file):
    """Create a complete student performance report with all enhancements."""
    
    # Start timing
    start_time = time.time()
    
    # Load student data
    students = load_student_data(data_file)
    if not students:
        return None
    
    # Normalize scores
    students = normalize_scores(students)
    
    # Calculate weighted final scores (40% exams, 30% attendance, 30% homework)
    for student in students:
        student['final_score'] = (
            0.4 * student['Score'] + 
            0.3 * student['Attendance'] + 
            0.3 * student['Homework']
        )
        
        # Assign letter grades
        if student['final_score'] >= 90:
            student['grade'] = 'A'
        elif student['final_score'] >= 80:
            student['grade'] = 'B'
        elif student['final_score'] >= 70:
            student['grade'] = 'C'
        elif student['final_score'] >= 60:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'
    
    # Calculate statistics
    stats = calculate_statistics(students)
    
    # Select random star students
    student_of_the_day = select_random_students(students)[0]
    most_improved = random.choice(students)  # In a real scenario, we'd compare to previous data
    
    # Create the report
    report = {
        'title': 'Student Performance Report',
        'students': students,
        'statistics': stats,
        'student_of_the_day': student_of_the_day['Name'],
        'most_improved': most_improved['Name']
    }
    
    # Add timestamp
    report = add_timestamp_to_report(report)
    
    # Calculate execution time
    end_time = time.time()
    report['execution_time'] = end_time - start_time
    
    return report

def save_report_to_file(report, filename='performance_report.txt'):
    """Save the report to a text file."""
    with open(filename, 'w') as file:
        # Header
        file.write(f"{report['title'].upper()}\n")
        file.write("=" * 50 + "\n\n")
        
        # Timestamp information
        file.write(f"Generated on: {report['timestamp']}\n")
        file.write(f"Next grading period: {report['next_grading_date']}\n")
        file.write(f"Days until next grading: {report['days_to_next_grading']}\n\n")
        
        # Statistics
        file.write("CLASS STATISTICS\n")
        file.write("-" * 50 + "\n")
        stats = report['statistics']
        file.write(f"Score Mean: {stats['scores']['mean']:.2f}\n")
        file.write(f"Score Median: {stats['scores']['median']}\n")
        file.write(f"Score Standard Deviation: {stats['scores']['std_dev']:.2f}\n")
        file.write(f"Score Range: {stats['scores']['min']} - {stats['scores']['max']}\n")
        file.write(f"Attendance Mean: {stats['attendance']['mean']:.2f}%\n")
        file.write(f"Homework Mean: {stats['homework']['mean']:.2f}%\n\n")
        
        # Recognition
        file.write("STUDENT RECOGNITION\n")
        file.write("-" * 50 + "\n")
        file.write(f"Student of the Day: {report['student_of_the_day']}\n")
        file.write(f"Most Improved: {report['most_improved']}\n\n")
        
        # Individual student details highlight
        file.write("STUDENT DETAILS\n")
        file.write("-" * 50 + "\n")
        file.write(f"{'Name':<15} {'Exam':<8} {'Attend':<8} {'HW':<8} {'Final':<8} {'Grade':<5} {'Normalized':<10}\n")
        file.write("-" * 65 + "\n")
        
        for student in sorted(report['students'], key=lambda x: x['final_score'], reverse=True):
            file.write(f"{student['Name']:<15} {student['Score']:<8} {student['Attendance']:<8} "
                      f"{student['Homework']:<8} {student['final_score']:.1f}    {student['grade']:<5} "
                      f"{student['normalized_score']:<10}\n")
        
        # Execution information
        file.write(f"\nReport generated in {report['execution_time']:.4f} seconds\n")
    
    print(f"Report saved to {filename}")

# Run the entire system
report = create_student_performance_report('student_data.csv')
if report:
    save_report_to_file(report)
    print("Student Performance Analyzer completed successfully!")
```

## Summary and Key Takeaways

In this session, we've explored several essential Python libraries and how they can enhance our Student Performance Analyzer:

1. **Math Module**: For mathematical operations and normalizing scores
2. **Datetime Module**: For handling dates, times, and calculating time differences
3. **Random Module**: For selecting random students and adding elements of chance
4. **Time Module**: For measuring execution time and performance
5. **Statistics Module**: For calculating statistical measures from student data

These libraries allow us to:
- Perform complex calculations easily
- Work with dates and times effectively
- Add randomness and selection mechanisms
- Measure and optimize performance
- Calculate statistical insights

By leveraging these libraries, we've transformed our basic Student Performance Analyzer into a more powerful tool that provides richer insights and features.

## Take-Home Exercise: Student Statistics Dashboard

Create a "Student Statistics Dashboard" that:

1. Loads student data from a CSV file
2. Calculates key statistics using the statistics module
3. Shows when the data was last updated using datetime
4. Includes a "student of the day" feature using random
5. Times how long the analysis takes using time
6. Rounds and formats all values appropriately using math

Submit your solution as a Jupyter Notebook with proper documentation. Include sample data and explain your approach.

Bonus: Add visualizations or additional features that might be useful for analyzing student performance data!
