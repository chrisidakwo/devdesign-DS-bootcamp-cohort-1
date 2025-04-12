# Python File Handling and OS Module
## Week 4, Lesson 3

---

# Agenda

1. Introduction to File Handling (45 min)
2. Practical File Handling (45 min)
3. The OS Module (45 min)
4. Applying File Handling to Student Report Generator (30 min)
5. Case Studies (30 min)
6. Wrap-up and Take-Home Exercise (10 min)

---

# Section 1: Introduction to File Handling
## Why File Handling in Data Science?

- **Data persistence** - Save results and analysis for later use
- **Data sources** - Most data comes from files (CSV, JSON, TXT)
- **Automation** - Process multiple files without manual intervention
- **Reporting** - Save outputs and visualizations to files
- **Logging** - Track program execution and errors

---

# Basic File Operations

- **Read**: Retrieve data from files
- **Write**: Create new files or overwrite existing files
- **Append**: Add data to existing files
- **Close**: Safely finish working with a file

---

# File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - open for reading |
| `'w'` | Write - create new file or overwrite existing |
| `'a'` | Append - add to end of file |
| `'r+'` | Read and write |
| `'b'` | Binary mode (add to other modes, e.g., `'rb'`) |
| `'t'` | Text mode (default) |

---

# Opening and Closing Files

```python
# Traditional way
file = open('example.txt', 'r')  # Open for reading
content = file.read()            # Read the entire file
file.close()                     # Always close files!

# Better way using context manager
with open('example.txt', 'r') as file:
    content = file.read()        # File automatically closes after block
```

---

# Reading Files

```python
# Read entire file as a string
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # List of strings, one per line
```

---

# Writing Files

```python
# Write a string to a file (creates or overwrites)
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

# Write multiple lines at once
lines = ["Line 1", "Line 2", "Line 3"]
with open('output.txt', 'w') as file:
    file.writelines([line + '\n' for line in lines])
```

---

# Appending to Files

```python
# Add content to the end of an existing file
with open('log.txt', 'a') as file:
    file.write("New entry: " + str(datetime.now()) + "\n")

# If file doesn't exist, it will be created
with open('new_file.txt', 'a') as file:
    file.write("This file was just created!")
```

---

# File Paths

```python
# Relative path (relative to current working directory)
with open('data/students.txt', 'r') as file:
    # ...

# Absolute path
with open('/home/user/data/students.txt', 'r') as file:
    # ...

# Windows paths (use raw strings to avoid escape issues)
with open(r'C:\Users\name\Documents\data.txt', 'r') as file:
    # ...
```

---

# Demo: Simple File Operations

```python
# Creating a new file with some content
with open('students.txt', 'w') as file:
    file.write("Alice, 92\n")
    file.write("Bob, 85\n")
    file.write("Charlie, 78\n")

# Reading the file we just created
with open('students.txt', 'r') as file:
    content = file.read()
    print("File contents:")
    print(content)

# Appending more data
with open('students.txt', 'a') as file:
    file.write("David, 95\n")
```
