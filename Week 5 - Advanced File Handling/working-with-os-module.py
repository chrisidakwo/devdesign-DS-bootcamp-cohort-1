import os # Import statement
import pprint

# File and directory operations
# Process management
# Environment variables
# Path manipulation

# `os.getcwd()` returns the current working directory for the project
currentWorkingDirectory = os.getcwd()
print("\n******************* WORKING WITH OS MODULE *******************\n")
print('\n', currentWorkingDirectory)

# `os.listdir()` returns a list of the content within the provided path/directory
# Can either be a relative or absolute path

cwdContent = os.listdir(currentWorkingDirectory)
# cwdContent = os.listdir('Week 1 - Introduction to Python')

cwdContent.sort()

pprint.pprint(cwdContent)

# `os.mkdir()` creates a new directory 
# The FileExistsError exception will be thrown when you attempt to create a directory that already exists
if os.path.exists('Week 6 - Introduction to Python Modules') is False:
    os.mkdir('Week 6 - Introduction to Python Modules')

pathExists = os.path.exists('Week 6 - Introduction to Python Modules')
print('\nDoes path exist?', pathExists)

fileExists = os.path.exists('Week 4 - Functions/Exercises/student-grade-calculator.py')
print('\nDoes file exist?', fileExists)

# Get absolute path from relative path
absPath = os.path.abspath('Week 6 - Introduction to Python Modules')
print('\n', absPath)

# Create nested directories
os.makedirs('Week 6 - Introduction to Python Modules/files/examples', exist_ok=True)

# Join paths safely (handles different OS path separators)
dataFile = os.path.join('data', 'students', 'grades.txt')
print('\n', dataFile)  # 'data/students/grades.txt' or 'data\students\grades.txt'