# Advanced File System Management
## Week 5, Lesson 2

---

# Agenda

* The OS Module
* Work with CSV files using Python's csv module
* Handle different file encodings and delimiters
* Programmatically manage directories and files
* Apply proper error handling for file operations
* Set up and use Jupyter Notebook via Anaconda

---

# Brief Review of File Handling

* Last week: Basic file operations
  * Opening, reading, writing, and closing files
  * File modes (r, w, a)
  * Context managers (`with` statement)
* Today: Advancing to structured data & complex operations

---


# The OS Module
## Introduction to the OS Module

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List contents of current directory
contents = os.listdir()
print(f"Directory contents: {contents}")

# Check if a file exists
if os.path.exists('example.txt'):
    print("The file exists!")
else:
    print("The file does not exist.")
```

---

# Navigating Directories

```python
import os

# Change to a different directory
os.chdir('../data')  # Go up one level and into 'data' folder
print(f"New directory: {os.getcwd()}")

# Go back to original directory
os.chdir('../project')
print(f"Back to: {os.getcwd()}")

# Get absolute path from relative path
abs_path = os.path.abspath('example.txt')
print(f"Absolute path: {abs_path}")
```

---

# Creating and Removing Directories

```python
import os

# Create a new directory
try:
    os.mkdir('new_folder')
    print("Directory created successfully!")
except FileExistsError:
    print("The directory already exists!")

# Create nested directories
os.makedirs('data/raw/2023', exist_ok=True)  # exist_ok=True prevents errors if exists

# Remove directory
os.rmdir('new_folder')  # Only works if directory is empty

# Remove directory and all contents (be VERY careful with this!)
import shutil
shutil.rmtree('data/raw', ignore_errors=True)
```

---

# Working with Paths

```python
import os

# Join paths safely (handles different OS path separators)
data_file = os.path.join('data', 'students', 'grades.txt')
print(data_file)  # 'data/students/grades.txt' or 'data\\students\\grades.txt'

# Split path into directory and filename
directory, filename = os.path.split('/home/user/data/grades.txt')
print(f"Directory: {directory}")  # '/home/user/data'
print(f"Filename: {filename}")    # 'grades.txt'

# Get file extension
name, extension = os.path.splitext('report.pdf')
print(f"Name: {name}, Extension: {extension}")  # 'report', '.pdf'
```

---

# Listing Directory Contents with Details

```python
import os
from datetime import datetime

def list_directory(path='.'):
    """List contents of a directory with details."""
    print(f"Contents of {os.path.abspath(path)}:")
    print(f"{'Name':<30} {'Size':<10} {'Modified':<20} {'Type':<10}")
    print("-" * 70)
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        size = os.path.getsize(full_path)
        mod_time = datetime.fromtimestamp(os.path.getmtime(full_path))
        item_type = "Directory" if os.path.isdir(full_path) else "File"
        
        print(f"{item:<30} {size:<10,} {mod_time.strftime('%Y-%m-%d %H:%M'):<20} {item_type:<10}")

# Run the function
list_directory()
```

---

# Demo: Using the OS Module

```python
import os

def create_project_structure(project_name):
    """Create a data science project folder structure."""
    # Create main project directory
    os.makedirs(project_name, exist_ok=True)
    
    # Create subdirectories
    directories = [
        'data/raw',
        'data/processed',
        'notebooks',
        'src',
        'results',
        'models'
    ]
    
    for directory in directories:
        path = os.path.join(project_name, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
    
    # Create a README file
    with open(os.path.join(project_name, 'README.md'), 'w') as file:
        file.write(f"# {project_name.title()}\n\nA data science project.")
    
    print(f"\nProject '{project_name}' structure created successfully!")

# Create a new project
create_project_structure('student_analysis')
```

---

# Section 4: Student Report Generator (Part 3)
## Saving Student Reports to a File

```python
def save_report_to_file(student_data, filename='student_report.txt'):
    """Save student report to a text file."""
    with open(filename, 'w') as file:
        file.write("STUDENT PERFORMANCE REPORT\n")
        file.write("=" * 30 + "\n\n")
        
        file.write(f"Total Students: {len(student_data)}\n")
        file.write(f"Average Score: {sum(student_data.values()) / len(student_data):.2f}\n\n")
        
        file.write("INDIVIDUAL SCORES\n")
        file.write("-" * 30 + "\n")
        
        for name, score in student_data.items():
            grade = get_letter_grade(score)
            file.write(f"{name:<20} {score:<5} {grade}\n")
            
    print(f"Report saved successfully to {filename}")
```

---

# Appending New Student Records

```python
def add_student_record(name, score, filename='student_report.txt'):
    """Append a new student record to existing report file."""
    grade = get_letter_grade(score)
    
    # Check if file exists, create if it doesn't
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("STUDENT PERFORMANCE REPORT\n")
            file.write("=" * 30 + "\n\n")
            file.write("INDIVIDUAL SCORES\n")
            file.write("-" * 30 + "\n")
    
    # Append the new record
    with open(filename, 'a') as file:
        file.write(f"{name:<20} {score:<5} {grade}\n")
    
    print(f"Student record for {name} added to {filename}")
```

---

# Reading and Updating Student Records

```python
def update_student_data(filename='student_report.txt'):
    """Read student data from file and update dictionary."""
    student_data = {}
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Skip header lines
            data_lines = [line for line in lines if line.strip() and not line.startswith(('=', '-', 'S'))]
            
            for line in data_lines:
                parts = line.strip().split()
                if len(parts) >= 2:
                    name = parts[0]
                    try:
                        score = float(parts[1])
                        student_data[name] = score
                    except ValueError:
                        continue
        
        return student_data
    
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty data.")
        return {}
```

# CSV Files in Data Science

* CSV = Comma-Separated Values
* Standard format for tabular data (interoperable)
* Used extensively in data science for:
  * Data exchange between systems
  * Dataset storage and sharing
  * Input for data analysis pipelines
* Structured with headers and rows

---

# The `csv` Module

```python
import csv

# Reading CSV files
with open('students.csv', 'r') as file:
    # Basic reader
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # row is a list of values
        
    # Dictionary reader - maps headers to values
    file.seek(0)  # Go back to the beginning of the file
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row)  # row is a dictionary {header: value}
```

---

# Writing to CSV Files

```python
import csv

# Sample data
data = [
    ['Name', 'Score', 'Grade'],  # Headers
    ['Alice', 92, 'A'],
    ['Bob', 85, 'B'],
    ['Charlie', 78, 'C']
]

# Using csv.writer
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once
    
# Using csv.DictWriter
students = [
    {'Name': 'David', 'Score': 95, 'Grade': 'A'},
    {'Name': 'Eve', 'Score': 88, 'Grade': 'B'}
]

with open('output_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Score', 'Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(students)  # Write all rows at once
```

---

# Handling Different CSV Formats

```python
# Custom delimiters (semicolon-separated)
with open('european_data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

# Handling quotes
with open('complex_data.csv', 'r') as file:
    reader = csv.reader(
        file,
        quotechar='"',  # Character used for quotes
        quoting=csv.QUOTE_MINIMAL  # When to quote fields
    )
    for row in reader:
        print(row)
```

---

# Common CSV Challenges

* Inconsistent delimiters
* Mixed data types
* Missing values
* Encoding issues (UTF-8, Latin-1, etc.)
* Malformed rows (too many or too few columns)
* Quoted fields with delimiters inside

---

# File Encodings

```python
# Specifying encoding when opening files
with open('data.csv', 'r', encoding='utf-8') as file:
    content = file.read()
    
# Handling encoding errors
try:
    with open('data.csv', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    # Try a different encoding
    with open('data.csv', 'r', encoding='latin-1') as file:
        content = file.read()
```

---

# HANDS-ON EXERCISE 1
## CSV Data Exploration

1. Open the provided `student_scores.csv` file
2. Read and print all records
3. Calculate the average score
4. Find the top 5 students with highest scores
5. Count how many students got each grade (A, B, C, etc.)

---

# Advanced Directory Operations

The `os` module provides functions for interacting with the operating system:

```python
import os

# Current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files and directories
contents = os.listdir(current_dir)
print(f"Directory contents: {contents}")

# Create a new directory
os.mkdir("new_folder")

# Create nested directories
os.makedirs("data/raw/2023", exist_ok=True)

# Remove a directory
os.rmdir("new_folder")  # Only if empty

# Check if a path exists
if os.path.exists("file.txt"):
    print("The file exists!")
```

---

# Working with File Paths

```python
import os

# Join paths (works on all operating systems)
data_path = os.path.join("data", "students", "scores.csv")
print(data_path)  # Correct path separator for your OS

# Split path into directory and filename
directory, filename = os.path.split("/data/students/scores.csv")
print(f"Directory: {directory}, Filename: {filename}")

# Get file extension
name, extension = os.path.splitext("report.pdf")
print(f"Name: {name}, Extension: {extension}")

# Get absolute path
rel_path = "data/scores.csv"
abs_path = os.path.abspath(rel_path)
print(f"Absolute path: {abs_path}")
```

---

# Advanced File Operations with `shutil`

```python
import shutil
import os

# Copy a file
shutil.copy2("source.txt", "destination.txt")

# Copy an entire directory
shutil.copytree("source_dir", "destination_dir")

# Move a file
shutil.move("old_location.txt", "new_location.txt")

# Remove a directory and all its contents
shutil.rmtree("directory_to_delete")

# Get file information
file_stats = os.stat("file.txt")
print(f"Size: {file_stats.st_size} bytes")
print(f"Last modified: {file_stats.st_mtime}")
```

---

# Error Handling in File Operations

Common file-related exceptions:
* `FileNotFoundError`
* `PermissionError`
* `IsADirectoryError`
* `FileExistsError`
* `UnicodeDecodeError`

---

# Robust File Handling

```python
import os

try:
    with open("data.csv", "r") as file:
        content = file.read()
        # Process file content
except FileNotFoundError:
    print("The file doesn't exist. Creating an empty one...")
    with open("data.csv", "w") as file:
        file.write("Name,Score,Grade\n")
except PermissionError:
    print("You don't have permission to access this file.")
except UnicodeDecodeError:
    print("Encoding issue. Try specifying a different encoding.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File processed successfully!")
finally:
    print("File operation attempted.")
```

---

# HANDS-ON EXERCISE 2
## File Organizer

Create a script that:
1. Creates directories: `TextFiles`, `Images`, `Others`
2. Scans a given folder for files
3. Moves files to appropriate folders based on extension:
   * .txt, .csv → TextFiles
   * .jpg, .png → Images
   * Everything else → Others
4. Uses proper error handling

---

# Introduction to Anaconda

* Complete distribution for Python data science
* Key benefits:
  * Package management (conda)
  * Environment management
  * Pre-installed libraries
  * Cross-platform compatibility
  * GUI interface (Anaconda Navigator)
* Simplifies the setup process for beginners

---

# Installing Anaconda

1. Download Anaconda from [anaconda.com](https://www.anaconda.com/download)
2. Follow installation prompts:
   * Windows: Run the .exe installer
   * macOS: Run the .pkg installer
   * Linux: Run the bash script
3. Verify installation: `conda --version`
4. Launch Anaconda Navigator

---

# Anaconda Navigator

![Anaconda Navigator interface showing Jupyter Notebook, JupyterLab, and other applications](https://docs.anaconda.com/_images/nav-defaults.png)

---

# Jupyter Notebook

* Interactive computing environment
* Documents contain:
  * Live code
  * Visualizations
  * Narrative text
  * Equations
* Perfect for:
  * Data cleaning and exploration
  * Statistical modeling
  * Data visualization
  * Teaching and learning

---

# Jupyter Interface

* Cell types:
  * Code (Python execution)
  * Markdown (formatted text)
  * Raw (unformatted text)
* Key shortcuts:
  * Shift+Enter: Run cell
  * Esc: Command mode
  * B: Create cell below
  * M: Change to Markdown
  * Y: Change to Code

---

# HANDS-ON EXERCISE 3
## Exploring Jupyter

1. Launch Jupyter Notebook through Anaconda Navigator
2. Create a new notebook
3. Add a Markdown cell with the title and your name
4. Create a code cell that imports csv and os modules
5. Write code to list all files in the current directory
6. Save the notebook

---

# Student Performance Analyzer (Mini-Project)

Let's build on our Student Report Generator:
* Convert to use CSV files
* Structure:
  1. Load student data from CSV
  2. Process and analyze data
  3. Save results to a new CSV
* We'll start implementation in class
* You'll complete it as a take-home exercise

---

# CSV Structure for Student Data

```
Name,Score,Attendance,Homework
Alice,92,95,90
Bob,85,88,82
Charlie,78,92,80
David,95,98,97
Eve,67,75,70
```

---

# Mini-Project: Implementation Start

```python
import csv

def load_student_data(filename):
    """Load student data from a CSV file into a list of dictionaries."""
    students = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric strings to numbers
                row['Score'] = int(row['Score'])
                row['Attendance'] = int(row['Attendance'])
                row['Homework'] = int(row['Homework'])
                students.append(row)
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Call the function with our file
students = load_student_data('student_data.csv')
print(f"Loaded {len(students)} student records.")
```

---

# Take-Home Exercise

1. Complete the Student Performance Analyzer:
   * Calculate statistics (avg, min, max for each column)
   * Find top performers overall and in each category
   * Add a "Final Grade" based on weighted scores
   * Save results to a new CSV file

2. Create a Jupyter Notebook that explains:
   * Reading and writing files
   * Working with CSV data
   * Organizing files with OS and shutil

---

# Summary

Today we covered:
* CSV file handling with the `csv` module
* Directory and file operations with `os` and `shutil`
* Error handling for robust file operations
* Anaconda installation and setup
* Introduction to Jupyter Notebook
* Started the Student Performance Analyzer project

---

# Additional Resources

* [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
* [Anaconda Documentation](https://docs.anaconda.com/)
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
* [Real Python: Working with CSV Files](https://realpython.com/python-csv/)
* [DataCamp: Python Directory and File Management](https://www.datacamp.com/community/tutorials/python-directory-management)

---

# Questions?

