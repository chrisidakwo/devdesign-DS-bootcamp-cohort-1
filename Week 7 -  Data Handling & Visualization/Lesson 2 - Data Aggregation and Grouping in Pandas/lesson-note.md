# Week 7, Lesson 2: Data Aggregation and Grouping in Pandas

## Learning Objectives
By the end of this lesson, you will be able to:
1. Master essential data manipulation techniques in Pandas (sorting, filtering, selecting)
2. Understand and apply grouping and aggregation methods to analyze data by categories
3. Apply functions to transform and clean data efficiently
4. Handle missing data appropriately
5. Create informative summaries of grouped data
6. Extract valuable insights from educational performance data

## Introduction

Welcome to the second lesson of Week 7! In our previous lesson, we introduced NumPy and the basics of Pandas. Today, we'll dive deeper into Pandas' powerful data manipulation capabilities, focusing on techniques that allow us to summarize, group, and analyze data in meaningful ways.

Real data scientists spend a significant portion of their time preparing, cleaning, and transforming data. The skills you'll learn today are essential for turning raw data into actionable insights, which is at the core of any data science project.

## Part 1: Advanced Data Selection and Filtering

#### Before we start:

 - Setup virtual environment

### Recap: Basic Data Access in Pandas

```python
import pandas as pd
import numpy as np

# Load the Nigerian students dataset
students_df = pd.read_csv('students.csv')

# Basic selection methods
print("First 5 rows:")
print(students_df.head())

# Selecting specific columns
scores = students_df[['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology']]
print("\nScore columns only:")
print(scores.head())
```

### Sorting Data

```python
# Sort by a single column (Mathematics scores from highest to lowest)
sorted_by_math = students_df.sort_values('Mathematics', ascending=False)
print("Top math students:")
print(sorted_by_math[['first_name', 'last_name', 'Mathematics']].head())

# Sort by multiple columns (class level, then Mathematics score)
sorted_multi = students_df.sort_values(['class_level', 'Mathematics'], 
                                       ascending=[True, False])
print("\nSorted by class level, then Mathematics score:")
print(sorted_multi[['class_level', 'first_name', 'last_name', 'Mathematics']].head())
```

### Advanced Filtering with Multiple Conditions

```python
# Filter with multiple conditions using logical operators
high_performers = students_df[(students_df['Mathematics'] > 85) & 
                              (students_df['Physics'] > 75)]
print("Students with 85+ in Mathematics and 75+ in Physics:")
print(high_performers[['first_name', 'last_name', 'Mathematics', 'Physics']].head())

# Students who excel in either Mathematics OR English Language
maths_or_english = students_df[(students_df['Mathematics'] > 90) | 
                               (students_df['English Language'] > 90)]
print("\nStudents with 90+ in either Mathematics or English Language:")
print(maths_or_english[['first_name', 'last_name', 
                       'Mathematics', 'English Language']].head())

# Using query() method for more readable filtering
science_experts = students_df.query('Chemistry >= 85 and class_level == "SS2"')
print("\nSS2 students with 85+ in Chemistry:")
print(science_experts[['first_name', 'last_name', 'Chemistry']].head())
```

### Using .loc and .iloc for Precise Data Selection

```python
# .loc - Label-based indexing
# Select rows with index labels 0, 1, 2 and columns 'first_name', 'last_name'
print(students_df.loc[0:2, ['first_name', 'last_name']])

# .iloc - Integer-based indexing
# Select rows 0, 1, 2 and columns 0, 1
print(students_df.iloc[0:3, 0:2])

# Combining .loc with conditions
girls_ss2 = students_df.loc[(students_df['gender'] == 'F') & 
                            (students_df['class_level'] == 'SS2')]
print("\nGirls in SS2:")
print(girls_ss2[['first_name', 'last_name']].head())
```

## Hands-on Exercise 1: Data Selection Challenge

**Real-world Context**: 
As a data scientist working for an educational consulting firm, you've been tasked with identifying students for special academic programs based on specific criteria. This exercise simulates the kind of targeted filtering data scientists perform when creating audience segments or identifying candidates for special interventions.

**Tasks**:
1. Find all students who are in SS1 and have an attendance rate above 92%
2. Identify students who are excelling in humanities (those with both English Language and Literature in English scores above 85)
3. Find students who might need academic support (those with at least two STEM subjects below 70)
4. Create a list of potential math tutors (students with Mathematics scores above 90 in SS3)
5. Sort the dataset by average score across all subjects they've taken (you'll need to calculate this first)

**Why This Matters**:
In data analytics, the ability to precisely select subsets of data based on complex criteria is essential. School counselors might use these techniques to identify students for advanced placement courses or academic intervention programs. Marketing analysts use similar approaches to segment customers for targeted campaigns. These filtering operations are among the most commonly used tools in a data scientist's daily workflow.

## Part 2: Grouping and Aggregation

### Understanding the GroupBy Operation

The `groupby()` method in Pandas is one of its most powerful features, allowing you to split data into groups based on some criteria, apply a function to each group independently, and then combine the results.

**Real-life Analogy**:
"Think of `groupby()` like sorting a deck of playing cards by suit. You first separate all the hearts, diamonds, clubs, and spades into different piles (the grouping step). Then, you can count how many cards are in each pile, find the highest card in each pile, or calculate the average card value for each suit (the aggregation step). Finally, you can put your results together in a new, summarized format that tells you about each suit rather than each individual card."

```python
# Basic groupby with a single column
gender_groups = students_df.groupby('gender')

# Calculate mean scores for each gender
gender_performance = gender_groups[['Mathematics', 'English Language', 'Physics', 'Chemistry']].mean()
print("Average scores by gender:")
print(gender_performance)

# Multiple aggregations at once
gender_stats = gender_groups['Mathematics'].agg(['mean', 'min', 'max', 'count'])
print("\nMath statistics by gender:")
print(gender_stats)

# Group by multiple columns
level_gender_groups = students_df.groupby(['class_level', 'gender'])
level_gender_performance = level_gender_groups['Mathematics'].mean()
print("\nAverage math score by class level and gender:")
print(level_gender_performance)
```

### Common Aggregation Functions

```python
# Group by class level
class_groups = students_df.groupby('class_level')

# Count of students in each class level
print("Number of students per class level:")
print(class_groups.size())

# Mean of all numeric columns by class level
print("\nAverage values by class level:")
print(class_groups.mean())

# Custom aggregations per column
custom_agg = {
    'attendance': ['min', 'max', 'mean'],
    'Mathematics': ['mean', 'median', 'std'],
    'English Language': ['mean', 'median', 'std'],
}
class_analysis = class_groups.agg(custom_agg)
print("\nCustom aggregations by class level:")
print(class_analysis)
```

### The Split-Apply-Combine Pattern

The GroupBy operation follows what's called the "split-apply-combine" pattern:

1. **Split**: The data is split into groups based on one or more keys
2. **Apply**: A function is applied to each group independently
3. **Combine**: The results are combined into a new data structure

This pattern is extremely powerful for data analysis and is used extensively in real-world data science.

### Grouped Filtering with .filter()

```python
# Find class levels with average Mathematics scores above 80
high_math_classes = students_df.groupby('class_level').filter(
    lambda x: x['Mathematics'].mean() > 80)
print("Class levels with math average above 80:")
print(high_math_classes['class_level'].unique())

# Find students in classes where average attendance is above 90%
good_attendance_classes = students_df.groupby('class_level').filter(
    lambda x: x['attendance'].mean() > 90)
print("\nStudents in classes with good average attendance:")
print(good_attendance_classes[['first_name', 'last_name', 'class_level', 
                             'attendance']].head())
```

## Hands-on Exercise 2: School Performance Analysis

**Real-world Context**:
You're working as a data analyst for a school, and the principal has requested a comprehensive analysis of student performance patterns. This analysis will inform resource allocation, curriculum development, and teacher professional development for the coming year. This exercise simulates a typical data aggregation task that data scientists perform when preparing reports for stakeholders.

**Tasks**:
1. Group the student data by class level and calculate:
   - The average score for each subject
   - The number of students in each class level
   - The minimum and maximum scores in each subject
2. Identify which class level has the:
   - Highest average attendance
   - Best overall academic performance (across all subjects)
   - Largest gender performance gap in Mathematics
3. Find out if there's a correlation between attendance and academic performance (hint: use groupby with multiple conditions)
4. Create a summary report showing the performance metrics for each class level

**Why This Matters**:
Educational administrators regularly need summary statistics to make data-driven decisions. School leaders might use these analyses to allocate resources for remedial programs, identify successful teaching practices, or spot trends that require intervention. The ability to group and aggregate data is essential for transforming detailed student records into actionable insights that can guide policy decisions.

## Part 3: Data Transformation and Cleaning

### Handling Missing Values

```python
# Create a dataset with some missing values for demonstration
data = students_df.copy()
# Introduce some missing values
import numpy as np
np.random.seed(42)  # For reproducibility
random_indices = np.random.choice(data.index, size=5, replace=False)
data.loc[random_indices, 'Mathematics'] = np.nan

# Check for missing values
print("Missing values in each column:")
print(data.isnull().sum())

# Fill missing values with mean of the column
data['Mathematics'] = data['Mathematics'].fillna(data['Mathematics'].mean())
print("\nAfter filling missing values:")
print(data['Mathematics'].isnull().sum())

# Fill missing values with group means (more sophisticated)
# For example, fill with the mean for the student's class level
grouped_means = data.groupby('class_level')['Physics'].transform('mean')
data['Physics'] = data['Physics'].fillna(grouped_means)
```

### Creating New Columns with .apply() and .transform()

```python
# First, let's filter to only analyze rows where all core subjects are present
# (this handles the fact that students take different subjects based on study group)
core_subjects = ['English Language', 'Mathematics']
data_with_cores = data.dropna(subset=core_subjects)

# Add a new column with letter grades based on average score of core subjects
def assign_letter_grade(row):
    score = (row['English Language'] + row['Mathematics']) / 2
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

# Apply function row-wise
data_with_cores['letter_grade'] = data_with_cores.apply(assign_letter_grade, axis=1)
print("First few students with letter grades:")
print(data_with_cores[['first_name', 'last_name', 'letter_grade']].head())

# Using lambda functions for simple transformations
data_with_cores['is_honor_roll'] = data_with_cores.apply(
    lambda row: True if assign_letter_grade(row) in ['A', 'B'] else False, axis=1)
print("\nHonor roll students:")
print(data_with_cores[data_with_cores['is_honor_roll']][['first_name', 'last_name']].head())

# Create standardized scores (z-scores) for Mathematics
data_with_cores['math_z_score'] = (data_with_cores['Mathematics'] - data_with_cores['Mathematics'].mean()) / data_with_cores['Mathematics'].std()
print("\nMath Z-scores:")
print(data_with_cores[['first_name', 'last_name', 'Mathematics', 'math_z_score']].head())
```

### Using .transform() for Group-wise Operations

```python
# Calculate how each student compares to their class level average
class_avg_math = data_with_cores.groupby('class_level')['Mathematics'].transform('mean')
data_with_cores['math_vs_class_avg'] = data_with_cores['Mathematics'] - class_avg_math
print("Math scores compared to class level average:")
print(data_with_cores[['first_name', 'class_level', 'Mathematics', 'math_vs_class_avg']].head())

# Percentile rank within class level
def percentile_rank(x):
    return x.rank(pct=True) * 100

data_with_cores['math_percentile'] = data_with_cores.groupby('class_level')['Mathematics'].transform(percentile_rank)
print("\nMath percentile within class level:")
print(data_with_cores[['first_name', 'class_level', 'Mathematics', 'math_percentile']].head())
```

## Hands-on Exercise 3: Student Report Card Generator

**Real-world Context**:
As an educational data specialist, you've been asked to create an automated report card system. This system needs to not only display individual student grades but also contextualize each student's performance relative to their peers. This exercise simulates the development of a data pipeline that would feed into a reporting or dashboard system for an educational institution.

**Tasks**:
1. Calculate each student's:
   - Average score across all subjects they've taken (handle missing values appropriately)
   - Letter grade based on their average score
   - Percentile rank within their class level
   - Performance relative to class level average for each subject
2. Identify students who:
   - Are in the top 10% of their class level
   - Are performing significantly below class level (more than 1 standard deviation below average)
   - Show high performance variance across subjects (students who excel in some subjects but struggle in others)
3. Create a summary dataframe that could be used to generate individual student report cards
4. Save the processed data to a CSV file that could be used by a reporting system

**Why This Matters**:
This exercise simulates a crucial function that data scientists perform in educational settings: transforming raw assessment data into meaningful feedback for students, parents, and teachers. The skills of data transformation, standardization, and contextualization are not only relevant in education but across many industries. For instance, similar techniques might be used in healthcare to compare patient outcomes against benchmarks, in finance to assess investment performance against market indices, or in marketing to evaluate campaign effectiveness across different segments.

## Key Takeaways

1. **Advanced Selection and Filtering**
   - Pandas provides powerful tools for selecting specific data points using `.loc[]`, `.iloc[]`, and boolean indexing.
   - Complex filters can be created by combining conditions with `&` (and), `|` (or).
   - The `.query()` method offers a more readable way to filter data.

2. **Grouping and Aggregation**
   - The `.groupby()` method follows the split-apply-combine pattern to analyze data by categories.
   - Multiple aggregations can be performed simultaneously on different columns.
   - You can group by multiple columns to create hierarchical summaries.

3. **Data Transformation and Cleaning**
   - Missing values can be handled strategically using `.fillna()` methods.
   - The `.apply()` function allows row-wise or column-wise operations with custom functions.
   - `.transform()` preserves the original DataFrame's index structure, making it ideal for adding new columns based on group calculations.

4. **Practical Applications**
   - These techniques form the backbone of real-world data analysis workflows.
   - Properly grouped and aggregated data helps stakeholders make informed decisions.
   - Data scientists frequently use these methods to transform raw data into actionable insights.

## Take-Home Exercise: School District Performance Analysis

**Real-world Context**:
You've been hired as a consultant for a large school district that wants to understand patterns in student performance across different schools. They're particularly interested in identifying factors that might influence academic success and finding schools that are performing exceptionally well despite challenges.

**Tasks**:

1. Download the provided district_data.csv file containing data from multiple schools including:
   - Student demographic information (grade, gender, socioeconomic status)
   - Academic performance (test scores in multiple subjects)
   - School information (size, location, resources)
   - Attendance and participation metrics

2. Perform a comprehensive analysis:
   - Calculate performance metrics for each school (average scores, passing rates)
   - Group students by various factors (school, grade level, socioeconomic status, etc.)
   - Identify the top and bottom performing schools
   - Investigate whether factors like school size or resources correlate with performance
   - Find "outlier" schools that perform better than expected given their resources
  
3. Create a summary report that includes:
   - Key performance metrics for each school
   - Analysis of factors correlated with academic success
   - Identification of schools that might have best practices to share
   - Recommendations for schools that might need additional support

4. Support your findings with appropriate data visualizations (this will help prepare you for our next lesson on data visualization)

**Submission**:
- Submit your Python script(s) and any generated CSV files
- Include a brief report (1-2 pages) summarizing your findings and methodology
- Be prepared to present a 2-minute summary of your most interesting finding in the next class

## Additional Resources
- [Pandas GroupBy Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
- [Pandas Data Selection](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
- [Real Python's Pandas GroupBy Tutorial](https://realpython.com/pandas-groupby/)
- [Towards Data Science: Pandas Apply, Map, and Filter Functions](https://towardsdatascience.com/apply-map-and-filter-functions-to-pandas-dataframes-90f9d5cfe9a)
