# Introduction to PIP and Virtual Environments
## Week 6, Lesson 2

Today, we'll explore two critical tools for Python development: package management with pip and virtual environments. These tools are essential for managing external libraries and creating reproducible Python environments for your data science projects.

## 1. Understanding Package Management

### What is Package Management?

Package management is the process of installing, upgrading, configuring, and removing third-party software packages/libraries in a consistent manner. In Python, packages/libraries are collections of modules that extend Python's functionality.

As your Python projects grow more complex, you'll need to use libraries beyond what's available in Python's standard library. This is where package management becomes essential.

### The Python Package Ecosystem

The Python ecosystem is incredibly rich with thousands of libraries available for different purposes:

- **Data Analysis**: pandas, NumPy, SciPy
- **Machine Learning**: scikit-learn, TensorFlow, PyTorch
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Web Development**: Django, Flask, FastAPI
- **And many more specialized libraries**

Without a package manager, installing and managing these libraries would be a tedious manual process. That's where `pip` comes in!

## 2. What is PIP?

`pip` is Python's official package manager/installer. The name "pip" stands for "Pip Installs Packages" (a recursive acronym). It's designed to simplify the installation and management of Python packages.

### Checking if PIP is Installed

Most Python installations (version 3.4+) come with pip pre-installed. You can check if pip is installed and see its version using:

```bash
# In command prompt or terminal
pip --version
```

If pip is installed, you'll see output similar to:

```
pip 22.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)
```

If pip is not installed, you can install it following the instructions at [pip.pypa.io](https://pip.pypa.io/en/stable/installation/).

### The Python Package Index (PyPI)

PyPI (pronounced "pie-pee-eye") is the official repository for Python packages. It hosts over 400,000 projects and is where pip looks for packages by default.

You can browse PyPI at [pypi.org](https://pypi.org/) to search for packages, read documentation, and check version history.

## 3. Basic PIP Commands

Let's look at the essential pip commands you'll use most frequently:

### Installing Packages

```bash
# Install a package
pip install package_name

# Install a specific version
pip install package_name==1.0.0

# Install with version constraints
pip install package_name>=1.0.0,<2.0.0
```

Example: Installing NumPy

```bash
pip install numpy
```

### Listing Installed Packages

```bash
# List all installed packages
pip list

# Show detailed information about a package
pip show package_name
```

### Upgrading Packages

```bash
# Upgrade a package
pip install --upgrade package_name

# or
pip install -U package_name
```

### Uninstalling Packages

```bash
# Uninstall a package
pip uninstall package_name
```

### Freezing Dependencies

This command outputs all installed packages and their versions, which is useful for creating requirements files:

```bash
pip freeze
```

Example output:
```
numpy==1.24.2
pandas==1.5.3
matplotlib==3.7.1
```

## 4. Working with Requirements Files

Requirements files allow you to specify the exact packages and versions your project needs. This is essential for reproducibility and collaboration.

### Creating a Requirements File

```bash
# Save all installed packages to requirements.txt
pip freeze > requirements.txt
```

You can also create or edit requirements.txt manually:

```
# requirements.txt
numpy==1.24.2
pandas>=1.5.0,<2.0.0
matplotlib==3.7.1
```

### Installing from a Requirements File

```bash
pip install -r requirements.txt
```

This will install all packages listed in the requirements file with the specified versions.

### Best Practices for Requirements Files

1. Always specify versions to ensure reproducibility
2. Use version constraints when appropriate
3. Keep separate requirements files for development and production
4. Include comments for clarity
5. Consider organizing requirements into groups

Example of a well-structured requirements file:

```
# Core libraries
numpy==1.24.2
pandas==1.5.3
scipy==1.10.1

# Visualization
matplotlib==3.7.1
seaborn==0.12.2

# Development tools
pytest==7.3.1
black==23.3.0  # Code formatter
```

## 5. What are Virtual Environments?

### The Problem: Global Package Installation

By default, pip installs packages to a global location shared by all Python projects on your system. This can lead to several problems:

1. **Version conflicts**: Different projects might require different versions of the same package
2. **Dependency hell**: Complex dependency chains can become difficult to manage
3. **Project isolation**: It's hard to know exactly which packages a specific project needs
4. **System pollution**: Installing many packages globally can clutter your system

### The Solution: Virtual Environments

A virtual environment is an isolated Python environment that has its own installation directories and doesn't share packages with other virtual environments or the global environment.

Virtual environments solve all the problems mentioned above by:

1. Isolating dependencies for each project
2. Making it easy to track what packages a project needs
3. Allowing different projects to use different versions of the same package
4. Keeping your global Python installation clean

### How Virtual Environments Work

A virtual environment contains:
- A copy of the Python interpreter
- A copy of the standard library
- A separate directory for installing packages
- Activation scripts to switch between environments

When you activate a virtual environment, your system temporarily uses the Python interpreter and packages from that environment instead of the global installation.

## 6. Creating and Using Virtual Environments

Python comes with a built-in module called `venv` for creating virtual environments.

### Creating a Virtual Environment

```bash
# Basic syntax
python -m venv environment_name

# Example: Create a virtual environment named 'myenv'
python -m venv myenv
```

This creates a directory named `myenv` that contains the virtual environment.

### Activating a Virtual Environment

The activation process depends on your operating system:

**On Windows:**
```bash
myenv\Scripts\activate
```

**On macOS and Linux:**
```bash
source myenv/bin/activate
```

When activated, you'll see the environment name in your command prompt or terminal:

```
(myenv) $
```

### Installing Packages in a Virtual Environment

Once activated, you can use pip normally, but packages will be installed only in this environment:

```bash
(myenv) $ pip install numpy pandas matplotlib
```

### Deactivating a Virtual Environment

To return to your global Python environment:

```bash
(myenv) $ deactivate
```

### Listing Packages in a Virtual Environment

To see what packages are installed in your active virtual environment:

```bash
(myenv) $ pip list
```

### Deleting a Virtual Environment

To delete a virtual environment, simply delete its directory:

```bash
# Windows
rmdir /s /q myenv

# macOS/Linux
rm -rf myenv
```

## 7. Best Practices for Virtual Environments

### Naming Conventions

Use descriptive names for your virtual environments that indicate their purpose:

- Project-specific: `myproject-env`
- Python version-specific: `py310-env`
- Purpose-specific: `datasci-env`, `web-env`

### Location

You can create virtual environments:

1. **Inside your project directory** (common for project-specific environments):
   ```
   myproject/
   ├── myenv/
   ├── src/
   ├── README.md
   └── requirements.txt
   ```

2. **In a central location** (useful for environments shared across projects):
   ```
   ~/.virtualenvs/
   ├── project1-env/
   ├── project2-env/
   └── datasci-env/
   ```

### Using .gitignore with Virtual Environments

Virtual environments shouldn't be committed to version control. Add them to your `.gitignore` file:

```
# .gitignore
myenv/
venv/
env/
.env/
```

### Documenting Environment Setup

Always include instructions for recreating your environment:

```markdown
# Project Setup

1. Create a virtual environment:
   ```
   python -m venv myenv
   ```

2. Activate the environment:
   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
```

## 8. Hands-on Exercises

### Exercise 1: Package Installer

Let's practice installing packages with pip:

1. Open your terminal or command prompt
2. Install NumPy:
   ```bash
   pip install numpy
   ```
3. Verify the installation:
   ```bash
   pip show numpy
   ```
4. Try using NumPy in Python:
   ```python
   import numpy as np
   arr = np.array([1, 2, 3, 4, 5])
   print(f"Mean: {np.mean(arr)}")
   print(f"Sum: {np.sum(arr)}")
   ```

### Exercise 2: Virtual Environment Setup

Let's create and use a virtual environment:

1. Create a new directory for a project:
   ```bash
   mkdir student_analysis
   cd student_analysis
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the environment:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`

4. Install some packages:
   ```bash
   pip install pandas matplotlib
   ```

5. Create a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

6. Create a simple script `analyze.py`:
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   
   # Create sample data
   data = {
       'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
       'Score': [92, 85, 78, 95, 67]
   }
   
   # Create DataFrame
   df = pd.DataFrame(data)
   
   # Calculate statistics
   avg_score = df['Score'].mean()
   print(f"Average score: {avg_score:.2f}")
   
   # Create a simple bar chart
   plt.figure(figsize=(10, 6))
   plt.bar(df['Name'], df['Score'])
   plt.title('Student Scores')
   plt.xlabel('Student')
   plt.ylabel('Score')
   plt.savefig('student_scores.png')
   print("Chart saved as student_scores.png")
   ```

7. Run the script:
   ```bash
   python analyze.py
   ```

8. Deactivate the environment:
   ```bash
   deactivate
   ```

## 9. Mini-Project: Student Performance Data with External Libraries

Let's enhance our Student Performance Data Analyzer by setting up a proper environment and using external libraries. We'll build on the project from previous lessons.

### Project Setup

1. Create a dedicated directory for the project:
   ```bash
   mkdir student_performance_analyzer
   cd student_performance_analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # Activate as shown previously
   ```

3. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn emoji
   ```

4. Create a requirements.txt file:
   ```bash
   pip freeze > requirements.txt
   ```

### Implementation

Create a file named `analyzer.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import emoji
import os
from datetime import datetime

def create_sample_data(filename='student_data.csv'):
    """Create a sample CSV file if it doesn't exist."""
    if os.path.exists(filename):
        return
    
    # Create sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 
                'Grace', 'Hannah', 'Ian', 'Julia'],
        'Score': [92, 85, 78, 95, 67, 73, 88, 79, 91, 84],
        'Attendance': [95, 88, 92, 98, 75, 80, 85, 90, 87, 94],
        'Homework': [90, 82, 80, 97, 70, 75, 92, 85, 88, 79]
    }
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Sample data created and saved to {filename}")

def load_data(filename='student_data.csv'):
    """Load data from CSV file into a pandas DataFrame."""
    try:
        df = pd.DataFrame(pd.read_csv(filename))
        print(f"Successfully loaded data for {len(df)} students.")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def analyze_data(df):
    """Perform analysis on the student data."""
    if df is None or df.empty:
        print("No data to analyze.")
        return None
    
    # Basic statistics
    stats = df.describe()
    
    # Calculate weighted scores (60% score, 20% attendance, 20% homework)
    df['Weighted_Score'] = df['Score'] * 0.6 + df['Attendance'] * 0.2 + df['Homework'] * 0.2
    
    # Assign letter grades
    grade_bins = [0, 60, 70, 80, 90, 100]
    grade_labels = ['F', 'D', 'C', 'B', 'A']
    df['Grade'] = pd.cut(df['Weighted_Score'], bins=grade_bins, labels=grade_labels)
    
    # Grade distribution
    grade_counts = df['Grade'].value_counts().sort_index()
    
    # Identify top performers and struggling students
    top_students = df.nlargest(3, 'Weighted_Score')
    struggling_students = df[df['Weighted_Score'] < df['Weighted_Score'].mean()]
    
    # Compile results
    results = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'statistics': stats,
        'grade_distribution': grade_counts,
        'top_students': top_students,
        'struggling_students': struggling_students,
        'data_with_grades': df
    }
    
    return results

def visualize_results(results, output_dir='output'):
    """Create visualizations of the analysis results."""
    if results is None:
        print("No results to visualize.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    df = results['data_with_grades']
    
    # Set the Seaborn style
    sns.set(style="whitegrid")
    
    # 1. Score Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Weighted_Score'], bins=10, kde=True)
    plt.title('Distribution of Weighted Scores')
    plt.xlabel('Weighted Score')
    plt.ylabel('Count')
    plt.savefig(f"{output_dir}/score_distribution.png")
    plt.close()
    
    # 2. Grade Distribution
    plt.figure(figsize=(8, 6))
    grade_counts = results['grade_distribution']
    sns.barplot(x=grade_counts.index, y=grade_counts.values)
    plt.title('Grade Distribution')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.savefig(f"{output_dir}/grade_distribution.png")
    plt.close()
    
    # 3. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    corr_matrix = df[['Score', 'Attendance', 'Homework', 'Weighted_Score']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Between Metrics')
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.close()
    
    # 4. Top Students Comparison
    top_students = results['top_students']
    plt.figure(figsize=(12, 6))
    top_students_melted = pd.melt(top_students, 
                                 id_vars=['Name'], 
                                 value_vars=['Score', 'Attendance', 'Homework'],
                                 var_name='Metric', value_name='Value')
    sns.barplot(x='Name', y='Value', hue='Metric', data=top_students_melted)
    plt.title('Top Students Performance Comparison')
    plt.ylabel('Score')
    plt.savefig(f"{output_dir}/top_students.png")
    plt.close()
    
    print(f"Visualizations saved to {output_dir} directory")

def generate_report(results, filename='student_report.txt'):
    """Generate a text report of the analysis results."""
    if results is None:
        print("No results to report.")
        return
    
    with open(filename, 'w') as f:
        f.write(emoji.emojize(":bar_chart: STUDENT PERFORMANCE ANALYSIS :bar_chart:\n"))
        f.write(f"Generated on: {results['timestamp']}\n\n")
        
        f.write(emoji.emojize(":memo: SUMMARY STATISTICS :memo:\n"))
        f.write(f"Number of students: {len(results['data_with_grades'])}\n")
        f.write(f"Average weighted score: {results['data_with_grades']['Weighted_Score'].mean():.2f}\n")
        f.write(f"Highest weighted score: {results['data_with_grades']['Weighted_Score'].max():.2f}\n")
        f.write(f"Lowest weighted score: {results['data_with_grades']['Weighted_Score'].min():.2f}\n\n")
        
        f.write(emoji.emojize(":1st_place_medal: TOP STUDENTS :1st_place_medal:\n"))
        for i, (idx, student) in enumerate(results['top_students'].iterrows(), 1):
            f.write(f"{i}. {student['Name']}: {student['Weighted_Score']:.2f} (Grade: {student['Grade']})\n")
        f.write("\n")
        
        f.write(emoji.emojize(":chart_increasing: GRADE DISTRIBUTION :chart_increasing:\n"))
        for grade, count in results['grade_distribution'].items():
            f.write(f"Grade {grade}: {count} students\n")
        
        f.write("\nRefer to the output directory for detailed visualizations.\n")
    
    print(f"Report saved to {filename}")

def main():
    # Create sample data if needed
    create_sample_data()
    
    # Load and analyze data
    data = load_data()
    results = analyze_data(data)
    
    # Generate visualizations and report
    if results:
        visualize_results(results)
        generate_report(results)

if __name__ == "__main__":
    main()
```

### Running the Project

With the virtual environment activated, run:

```bash
python analyzer.py
```

This will:
1. Create or use the sample data
2. Perform analysis on student performance
3. Generate visualizations using matplotlib and seaborn
4. Create a report with emoji enhancements

### Project Structure

Your final project structure should look like:

```
student_performance_analyzer/
├── env/                  # Virtual environment (not committed to version control)
├── output/               # Generated visualizations
│   ├── score_distribution.png
│   ├── grade_distribution.png
│   ├── correlation_heatmap.png
│   └── top_students.png
├── analyzer.py           # Main analysis script
├── student_data.csv      # Input data
├── student_report.txt    # Generated report
└── requirements.txt      # Dependencies
```

## 10. Alternative Package Management Tools

While pip and venv are Python's built-in tools, there are other popular alternatives worth mentioning:

### Conda

Conda is a package, dependency, and environment manager particularly popular in data science:

- Manages both Python and non-Python libraries
- Handles binary dependencies better than pip
- Comes with Anaconda and Miniconda distributions
- Uses its own package repository (Anaconda repository)

### Pipenv

Pipenv combines pip and virtualenv into a single tool:

- Automatically creates and manages virtualenv
- Generates a `Pipfile` and `Pipfile.lock` for dependencies
- Provides deterministic builds with the lock file
- Simplifies development workflow

### Poetry

Poetry is a modern dependency management and packaging tool:

- Manages dependencies with precise versioning
- Handles package building and publishing
- Provides a lockfile for deterministic builds
- Offers an intuitive command-line interface

## 11. Take-Home Exercise

Create a "Python Environment Explorer" project:

1. Create a new virtual environment
2. Install three external packages of your choice (consider pandas, matplotlib, and a fun one like emoji or art)
3. Create a Jupyter Notebook that demonstrates features of each package
4. Generate a requirements.txt file for your project
5. Include documentation explaining how to set up the environment
6. Create a simple script that uses the external packages for data processing or visualization

Requirements for submission:
- Complete project directory (excluding virtual environment folder)
- Clear README with setup instructions
- Sample output demonstrating the packages in action

## 12. Conclusion and Key Takeaways

In today's lesson, we've learned:

1. **Package Management**:
   - What Python packages are and why they're important
   - How to use pip to install, update, and remove packages
   - How to create and use requirements files

2. **Virtual Environments**:
   - What virtual environments are and why they're essential
   - How to create, activate, and use virtual environments
   - Best practices for managing project environments

3. **Practical Application**:
   - How to enhance projects with external libraries
   - Setting up proper project structures
   - Creating reproducible environments

These skills form the foundation for more advanced data science work, where you'll rely on specialized libraries and need to ensure your environments are properly managed and reproducible.

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [venv documentation](https://docs.python.org/3/library/venv.html)
- [Real Python: Python Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [The Hitchhiker's Guide to Python: Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)