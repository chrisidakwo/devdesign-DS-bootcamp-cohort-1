# Data Handling and Visualization with NumPy, Pandas, Matplotlib, and Seaborn

# Week 6, Lesson 1: Introduction to NumPy and Data Handling with Pandas

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand what NumPy is and why it's essential for data science
2. Create and manipulate NumPy arrays
3. Understand Pandas DataFrame structure and basic operations
4. Load CSV data into Pandas DataFrames
5. Perform basic data cleaning and exploration
6. Apply these concepts to the Student Report Generator project

## Introduction

Welcome to Week 6! We're now transitioning from basic Python programming to specialized tools for data science. Today, we'll explore two fundamental yet powerful libraries:

- **NumPy**: Provides efficient numerical computations and array operations
- **Pandas**: Enables powerful data manipulation and analysis

These libraries form the foundation of the Python data science ecosystem and are used daily by professionals in the field.

## Part 1: Introduction to NumPy

### What is NumPy?

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides:

- A powerful N-dimensional array object
- Sophisticated broadcasting functions
- Tools for integrating C/C++ code
- Linear algebra, Fourier transform, and random number capabilities

### Why NumPy?

Think of Python lists as individual storage boxes where you keep items separately. Each box needs its own label, lock, and handling instructions. NumPy arrays are like a well-organized warehouse storage system where all items of the same type are stored efficiently in a grid with a single management system. This makes operations much faster and memory-efficient.

Key benefits:
- Much faster than Python lists for numerical operations
- Uses less memory
- Convenient and readable syntax for mathematical operations
- Core foundation for most Python data science libraries

### Creating NumPy Arrays

```python
import numpy as np

# Creating arrays from Python lists
numbers = np.array([1, 2, 3, 4, 5])
print("1D array:", numbers)
# Output: 1D array: [1 2 3 4 5]

# Creating a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array (matrix):")
print(matrix)
# Output:
# [
#  [1 2 3]
#  [4 5 6]
#  [7 8 9]
# ]

# Creating arrays with specific patterns
zeros = np.zeros(5)  # Array of 5 zeros
print("Zeros array:", zeros)
# Output: Zeros array: [0. 0. 0. 0. 0.]

ones = np.ones((3, 3))  # 3x3 matrix of ones
print("Ones matrix:")
print(ones)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# Range of values
range_array = np.arange(0, 10, 2)  # Start, stop, step
print("Range array:", range_array)
# Output: Range array: [0 2 4 6 8]

# Linearly spaced values
linear_space = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print("Linearly spaced:", linear_space)
# Output: Linearly spaced: [0.   0.25 0.5  0.75 1.  ]

# Random numbers
random_array = np.random.rand(1)  # 5 random numbers between 0 and 1
print("Random array:", random_array)
# Output: Random array: [0.42 0.78 0.19 0.9  0.45] (values will vary)
```

### NumPy Array Operations

```python
# Basic math operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print("a + b =", a + b)  # [5, 7, 9]
print("a * b =", a * b)  # [4, 10, 18]

# Scalar operations (applied to all elements)
print("a * 2 =", a * 2)  # [2, 4, 6]

# Statistical methods
data = np.array([15, 23, 42, 18, 37, 29])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

# Finding positions
print("Position of minimum:", np.argmin(data))
print("Position of maximum:", np.argmax(data))
```

## Hands-on Exercise 1: NumPy Fundamentals

### Student Test Score Analysis

**Real-world Context**: 
As a data scientist working in education analytics, you often need to quickly analyze test results to identify patterns and outliers. This exercise simulates a scenario where you've received raw test scores and need to extract meaningful insights to report to school administrators.

**Tasks**:
1. Create a NumPy array of 10 random integers between 50 and 100 (representing student test scores)
2. Calculate the mean, median, and standard deviation of the scores
3. Find the highest and lowest scores and their positions in the array
4. Create a 3x3 matrix representing scores for 3 students across 3 subjects (Math, Science, English)
5. Calculate the average score for each student (row-wise mean)
6. Calculate the average score for each subject (column-wise mean)

**Why This Matters**:
The 3x3 matrix represents a common data structure (e.g. in educational assessment) where rows might represent individual students and columns represent different subjects or test components. By calculating row-wise means, you can assess individual student performance across subjects. Column-wise means help identify which subjects have higher or lower overall performance, potentially highlighting curriculum areas that need attention.

## Part 2: Introduction to Pandas

### What is Pandas?

Pandas (Python Data Analysis Library) is built on top of NumPy and provides easy-to-use data structures and data analysis tools. It's designed to make working with structured data seamless and intuitive.

### Why Pandas?

If NumPy is like an efficient warehouse, Pandas is like a complete inventory management system. It not only stores your data efficiently but also labels everything with row and column names, lets you search and filter based on any criteria, handles missing items gracefully, and can import/export data from various sources.

Key features:
- DataFrames: 2D labeled data structures similar to spreadsheets or SQL tables
- Series: 1D labeled arrays
- Powerful data alignment and integration capabilities
- Robust handling of missing data
- Intuitive reading and writing of data between in-memory structures and file formats
- Flexible reshaping and pivoting of datasets

### Creating Pandas DataFrames

```python
import pandas as pd
import numpy as np

# Create a simple DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Boston', 'Chicago', 'Denver', 'Seattle'],
    'Score': [85, 92, 78, 95, 89]
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)

# Creating a DataFrame from a NumPy array
array_data = np.random.randint(60, 100, size=(5, 4))
df2 = pd.DataFrame(array_data, 
                  columns=['Math', 'Science', 'English', 'History'],
                  index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])
print("\nDataFrame from array:")
print(df2)
```

### Reading Data from CSV Files

```python
# Reading CSV into DataFrame
students_df = pd.read_csv('student_records.csv')
print("First 5 rows of the DataFrame:")
print(students_df.head())
```

### Basic DataFrame Operations

```python
# Basic information about the DataFrame
print("DataFrame shape (rows, columns):", students_df.shape)
print("\nColumn names:", students_df.columns.tolist())
print("\nData types:")
print(students_df.dtypes)

# Summary statistics
print("\nSummary statistics:")
print(students_df.describe())

# Accessing columns
print("\nMath scores:")
print(students_df['math_score'])

# Accessing rows
print("\nFirst 3 rows:")
print(students_df.iloc[0:3])  # Integer location-based indexing

# Accessing specific cell
print("\nFirst student's math score:", students_df.iloc[0, 6])

# Conditional selection
high_scores = students_df[students_df['math_score'] > 90]
print("\nStudents with math scores over 90:")
print(high_scores[['first_name', 'last_name', 'math_score']])
```

### Basic Data Cleaning

```python
# Checking for missing values
print("Missing values in each column:")
print(students_df.isnull().sum())

# Handling missing values (if any)
# Example: Filling NA values with mean
if students_df['math_score'].isnull().sum() > 0:
    students_df['math_score'].fillna(students_df['math_score'].mean(), inplace=True)

# Renaming columns
students_df = students_df.rename(columns={'math_score': 'mathematics_score'})
print("\nRenamed columns:", students_df.columns.tolist())

# Creating new columns
students_df['average_score'] = (students_df['mathematics_score'] + 
                               students_df['science_score'] + 
                               students_df['english_score'] + 
                               students_df['history_score']) / 4
print("\nAverage scores:")
print(students_df[['first_name', 'last_name', 'average_score']].head())
```

## Hands-on Exercise 2: Exploring Student Data

**Real-world Context**:
In educational data science or business analytics, your first task with any new dataset is often exploratory data analysis (EDA). This process helps you understand the structure, quality, and characteristics of the data before performing more advanced analyses. For instance, when working with a school district, you might receive raw student performance data that needs to be validated, cleaned, and transformed before it can inform policy decisions.

**Tasks**:
1. Load the student_records.csv file into a Pandas DataFrame
2. Explore the data structure (number of rows/columns, data types)
3. Calculate basic statistics for numerical columns (mean, max, min, std dev)
4. Identify top 5 students by average score across all subjects
5. Create a new column for "Pass/Fail" based on whether the average score is above 75
6. Find the percentage of students passing in each grade level

**Why This Matters**:
This exercise mirrors the typical first steps a data scientist takes when receiving educational data. School administrators often need quick summary statistics on student performance to identify areas of concern. Creating derived metrics like pass/fail rates and segmenting analysis by grade levels helps educators understand where to focus improvement efforts.

## Part 3: Student Report Generator - Pandas Upgrade

Let's upgrade our Student Report Generator from previous weeks to use the powerful features of Pandas:

```python
import pandas as pd
import numpy as np

def analyze_student_data(csv_file):
    """Analyze student data using Pandas."""
    # Load the data
    try:
        df = pd.read_csv(csv_file)
        print(f"Successfully loaded data with {df.shape[0]} students and {df.shape[1]} columns.")
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    
    # Basic data exploration
    print("\n=== BASIC DATA EXPLORATION ===")
    print(f"First few records:")
    print(df.head())
    
    print("\nColumn names:")
    print(df.columns.tolist())
    
    # Calculate average scores
    score_columns = ['math_score', 'science_score', 'english_score', 'history_score']
    df['average_score'] = df[score_columns].mean(axis=1).round(2)
    
    # Add letter grades
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
    
    # Statistical summary
    print("\n=== STATISTICAL SUMMARY ===")
    print(df[score_columns + ['average_score']].describe())
    
    # Top students
    print("\n=== TOP STUDENTS ===")
    top_students = df.sort_values('average_score', ascending=False).head(3)
    print(top_students[['student_id', 'first_name', 'last_name', 'average_score', 'letter_grade']])
    
    # Students below average
    average = df['average_score'].mean()
    below_avg = df[df['average_score'] < average]
    print(f"\nNumber of students below average ({average:.2f}): {below_avg.shape[0]}")
    
    # Performance by gender
    print("\n=== PERFORMANCE BY GENDER ===")
    gender_performance = df.groupby('gender')['average_score'].mean().round(2)
    print(gender_performance)
    
    # Grade distribution
    print("\n=== GRADE DISTRIBUTION ===")
    grade_counts = df['letter_grade'].value_counts()
    grade_percentage = (grade_counts / len(df) * 100).round(1)
    grade_df = pd.DataFrame({'Count': grade_counts, 'Percentage': grade_percentage})
    print(grade_df)
    
    return df

# Test the function
student_data = analyze_student_data('student_records.csv')
```

## Hands-on Exercise 3: Student Report Generator (Pandas Upgrade)

**Real-world Context**:
Education departments and school analytics teams routinely need to generate comprehensive reports on student performance. These reports inform teacher evaluations, curriculum development, and student intervention programs. As a data scientist in this field, you would be tasked with creating automated reporting systems that transform raw academic data into actionable insights for various stakeholders.

**Tasks**:
1. Enhance the Student Report Generator using Pandas to:
   - Import student data from the CSV file
   - Calculate each student's average score and letter grade
   - Identify students who need additional support (scoring below class average)
   - Create a performance summary by subject area
   - Generate a "class profile" with key statistics
2. Export the processed data to a CSV file that could be used by teachers or administrators

**Why This Matters**:
This exercise simulates the development of an automated reporting system that might be used by schools to track student progress. In a professional setting, data scientists often create these kinds of data pipelines that automatically process incoming data (such as weekly test scores) and generate standardized reports. Such systems might feed into dashboards for administrators, detailed reports for teachers, or simplified summaries for parents and students.

## Take-Home Exercise

**Real-world Context**:
You've been hired as a data consultant by a school district looking to improve their academic performance tracking system. The superintendent wants to understand patterns in student achievement and identify opportunities for targeted interventions. Your task is to develop a prototype analysis system that could be expanded for district-wide use.

**Tasks**:

1. Enhanced Student Performance Analysis
   - Load the student_records.csv file
   - Calculate each student's average score
   - Assign letter grades (A: ≥90, B: 80-89, C: 70-79, D: 60-69, F: <60)
   - Identify top performers in each subject
   - Analyze if there's a correlation between attendance and performance
   - Create a "Student Report Card" that includes all this information
   - Save the processed data to a new CSV file named "student_report_cards.csv"

2. Statistical Distribution Analysis
   - Generate a simulated dataset of 100 test scores (representing a larger school population)
   - Calculate mean, median, mode, and standard deviation
   - Identify how many scores fall within 1, 2, and 3 standard deviations of the mean
   - Create a normalized version of the scores (0-1 scale)
   - Write a brief analysis of what the distribution tells you about the test's difficulty level

**Submission**:
- Submit your Python script(s) and any generated CSV files
- Include comments explaining your code and your analysis of the findings
- Be prepared to discuss your implementation in the next class

## Additional Resources
- NumPy documentation: https://numpy.org/doc/
- Pandas documentation: https://pandas.pydata.org/docs/
- Real Python tutorial on NumPy: https://realpython.com/numpy-tutorial/
- Real Python tutorial on Pandas: https://realpython.com/pandas-python-explore-dataset/