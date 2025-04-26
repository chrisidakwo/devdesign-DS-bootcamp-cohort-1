# Advanced File System Management
## Week 6, Lesson 1

## 1. Introduction to Anaconda and Jupyter Notebook

### What is Anaconda?

Anaconda is a distribution of Python and R for scientific computing that aims to simplify package management and deployment. It includes:

- Python interpreter
- Package manager (conda)
- Many pre-installed "data science" libraries
- Development environments
- Tools like Jupyter Notebook

It's particularly useful for beginners because it eliminates many installation and configuration headaches.

### Installing Anaconda

1. Download Anaconda from [anaconda.com](https://www.anaconda.com/download)
2. Follow the installation instructions for your operating system
3. Verify installation by opening Anaconda Navigator or running `conda --version` in your terminal/command prompt

### Jupyter Notebook

Jupyter Notebook is an open-source web application (based off IPython) that allows you to create and share Python documents that contain:

- Live code
- Equations
- Visualizations
- Narrative text

It's perfect for:
- Data cleaning and transformation
- Numerical simulation
- Data visualization
- Machine learning
- Sharing your work with others

### Launching Jupyter Notebook

1. Open Anaconda Navigator and click on the "Launch" button under Jupyter Notebook
2. Alternatively, open your terminal/command prompt and run: `jupyter notebook`
3. Your default web browser will open with the Jupyter dashboard

### Creating Your First Notebook

1. In the Jupyter dashboard, navigate to your desired folder
2. Click the "New" button and select "Python 3" to create a new notebook
3. You'll see an empty cell where you can start typing code

### Cell Types in Jupyter

Jupyter notebooks consist of cells, which can be of different types:

- **Code cells**: Contain Python code that can be executed
- **Markdown cells**: Contain formatted text (headings, lists, links, etc.)
- **Raw cells**: Contain unformatted text that won't be processed

### Basic Jupyter Operations

- To run a cell: Press `Shift+Enter` or click the "Run" button
- To change cell type: Use the dropdown menu or keyboard shortcuts (`Y` for code, `M` for markdown)
- To add a new cell: Click the "+" button or press `B` (below) or `A` (above) in command mode
- To save your notebook: Press `Ctrl+S` or click the save icon

## 2. Hands-on Exercises

### Exercise 1: CSV Data Exploration

Let's practice working with CSV files:

```python
import csv

def analyze_student_data(filename):
    """Analyze student data from a CSV file."""
    students = []
    
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert score from string to integer
            row['Score'] = int(row['Score'])
            students.append(row)
    
    # Calculate average score
    total_score = sum(student['Score'] for student in students)
    average_score = total_score / len(students)
    print(f"Average score: {average_score:.2f}")
    
    # Find top 5 students
    top_students = sorted(students, key=lambda x: x['Score'], reverse=True)[:5]
    print("\nTop 5 students:")
    for i, student in enumerate(top_students, 1):
        print(f"{i}. {student['Name']} - {student['Score']}")
    
    # Count students by grade
    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for student in students:
        score = student['Score']
        if score >= 90:
            grades['A'] += 1
        elif score >= 80:
            grades['B'] += 1
        elif score >= 70:
            grades['C'] += 1
        elif score >= 60:
            grades['D'] += 1
        else:
            grades['F'] += 1
    
    print("\nGrade distribution:")
    for grade, count in grades.items():
        print(f"{grade}: {count} students")

# Test the function
analyze_student_data('student_scores.csv')
```

### Exercise 2: File Organizer

Let's create a script that organizes files based on their extensions:

```python
import os
import shutil

def organize_files(directory):
    """
    Organize files in a directory based on their extensions.
    Creates directories for different file types and moves files accordingly.
    """
    # Create directories if they don't exist
    text_dir = os.path.join(directory, "TextFiles")
    image_dir = os.path.join(directory, "Images")
    others_dir = os.path.join(directory, "Others")
    
    for dir_path in [text_dir, image_dir, others_dir]:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Created directory: {dir_path}")
    
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Define file types
    text_extensions = ['.txt', '.csv', '.log', '.md']
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    
    # Move files to appropriate directories
    for file in files:
        source = os.path.join(directory, file)
        _, extension = os.path.splitext(file)
        extension = extension.lower()
        
        try:
            if extension in text_extensions:
                shutil.move(source, os.path.join(text_dir, file))
                print(f"Moved {file} to TextFiles")
            elif extension in image_extensions:
                shutil.move(source, os.path.join(image_dir, file))
                print(f"Moved {file} to Images")
            else:
                # Skip directories we created
                if file not in ["TextFiles", "Images", "Others"]:
                    shutil.move(source, os.path.join(others_dir, file))
                    print(f"Moved {file} to Others")
        except Exception as e:
            print(f"Error moving {file}: {e}")
    
    print("\nOrganization complete!")

# Test the function
organize_files('.')  # Organize files in the current directory
```

### Exercise 3: Exploring Jupyter Notebook

Let's create our first Jupyter Notebook:

1. Launch Jupyter Notebook through Anaconda Navigator
2. Create a new notebook
3. Add a markdown cell with the following content:
   ```markdown
   # My First Jupyter Notebook
   
   This is a markdown cell where I can write formatted text.
   
   ## About me
   
   My name is [Your Name]
   
   I'm learning Python for Data Science!
   ```
4. Add a code cell with the following content:
   ```python
   # Import modules
   import os
   import csv
   
   # List all files in the current directory
   files = os.listdir()
   print("Files in the current directory:")
   for file in files:
       print(f" - {file}")
   ```
5. Run both cells and observe the results
6. Save your notebook with a meaningful name

## 3. Mini-Project: Student Performance Data Analyzer

Let's start building our Student Performance Data Analyzer, which will load student data from a CSV file, analyze it, and save the results.

Here's a starter implementation:

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
                # Convert numeric strings to numbers
                for key in ['Score', 'Attendance', 'Homework']:
                    if key in row:
                        row[key] = int(row[key])
                students.append(row)
        print(f"Successfully loaded {len(students)} student records.")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def analyze_student_data(students):
    """Perform basic analysis on student data."""
    if not students:
        print("No data to analyze.")
        return {}
    
    # Calculate statistics
    num_students = len(students)
    
    # Score statistics
    scores = [s['Score'] for s in students]
    avg_score = sum(scores) / num_students
    min_score = min(scores)
    max_score = max(scores)
    
    # Attendance statistics
    attendance = [s['Attendance'] for s in students]
    avg_attendance = sum(attendance) / num_students
    
    # Homework statistics
    homework = [s['Homework'] for s in students]
    avg_homework = sum(homework) / num_students
    
    # Top performers (overall score)
    top_students = sorted(students, key=lambda x: x['Score'], reverse=True)[:3]
    
    # Store results
    analysis = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'num_students': num_students,
        'avg_score': avg_score,
        'min_score': min_score,
        'max_score': max_score,
        'avg_attendance': avg_attendance,
        'avg_homework': avg_homework,
        'top_students': top_students
    }
    
    return analysis

def save_analysis(analysis, filename='analysis_results.csv'):
    """Save analysis results to a CSV file."""
    if not analysis:
        print("No analysis results to save.")
        return
    
    try:
        # Save overall statistics
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['Timestamp', analysis['timestamp']])
            writer.writerow(['Number of Students', analysis['num_students']])
            writer.writerow(['Average Score', f"{analysis['avg_score']:.2f}"])
            writer.writerow(['Minimum Score', analysis['min_score']])
            writer.writerow(['Maximum Score', analysis['max_score']])
            writer.writerow(['Average Attendance', f"{analysis['avg_attendance']:.2f}"])
            writer.writerow(['Average Homework', f"{analysis['avg_homework']:.2f}"])
            writer.writerow([])
            
            # Add top students section
            writer.writerow(['Top Performers'])
            writer.writerow(['Name', 'Score', 'Attendance', 'Homework'])
            for student in analysis['top_students']:
                writer.writerow([
                    student['Name'], 
                    student['Score'],
                    student['Attendance'],
                    student['Homework']
                ])
        
        print(f"Analysis results saved to {filename}")
    except Exception as e:
        print(f"Error saving analysis: {e}")

def main():
    # Sample data file
    data_file = 'student_data.csv'
    
    # Check if sample data exists, create if not
    if not os.path.exists(data_file):
        print(f"Creating sample data file: {data_file}")
        with open(data_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Score', 'Attendance', 'Homework'])
            writer.writerow(['Alice', 92, 95, 90])
            writer.writerow(['Bob', 85, 88, 82])
            writer.writerow(['Charlie', 78, 92, 80])
            writer.writerow(['David', 95, 98, 97])
            writer.writerow(['Eve', 67, 75, 70])
    
    # Load and analyze data
    students = load_student_data(data_file)
    analysis = analyze_student_data(students)
    
    # Save analysis results
    save_analysis(analysis)

if __name__ == "__main__":
    main()
```

## Take-Home Exercise

1. Complete the Student Performance Analyzer by adding:
   - A function to calculate grade distributions (A, B, C, D, F)
   - Identification of students who need improvement (e.g., below average)
   - A final weighted grade calculation (e.g., 60% score + 20% attendance + 20% homework)
   - A function to save detailed individual student reports

2. Create a Jupyter Notebook that demonstrates:
   - Reading and writing CSV files
   - Working with directories and file paths
   - Error handling for file operations
   - Basic data analysis on the student data

## Additional Resources

* [Working with Markdown](https://www.markdownguide.org/)
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
* [Jupyter Notebook Installation](https://www.youtube.com/watch?v=WOK9HeB-OmY)
* [Anaconda Installer](https://www.anaconda.com/download/success)
* [Anaconda Documentation](https://docs.anaconda.com/)