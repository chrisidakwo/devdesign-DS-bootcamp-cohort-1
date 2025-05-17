# Week 8, Lesson 3: Data Visualization with Matplotlib and Seaborn

## Learning Objectives
By the end of this lesson, you will be able to:
1. Create and customize various types of plots using Matplotlib
2. Understand the difference between Matplotlib's figure, axes, and plots
3. Enhance visualizations with proper titles, labels, legends, and color schemes
4. Use Seaborn to create more sophisticated statistical visualizations
5. Select appropriate visualization types for different kinds of data
6. Interpret visualizations to extract meaningful insights about student performance

## Introduction

So far, we've learned how to manipulate and analyze data using NumPy and Pandas. Today, we'll explore how to transform that data into visual representations that make patterns and insights immediately apparent.

Data visualization is a critical skill for any data scientist. As the saying goes, "a picture is worth a thousand words." Effective visualizations can communicate complex findings to stakeholders in ways that tables of numbers simply cannot. In this lesson, we'll focus on using Matplotlib and Seaborn, two of the most popular visualization libraries in Python.

## Part 1: Introduction to Matplotlib

### What is Matplotlib?

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It provides an object-oriented API for embedding plots into applications.

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load our dataset
students_df = pd.read_csv('nigerian_students_full.csv')
print(f"Loaded dataset with {students_df.shape[0]} students")
```

### The Anatomy of a Matplotlib Plot

In Matplotlib, a plot consists of several components:
- **Figure**: The overall window or page where everything is drawn
- **Axes**: The actual plot area where data is displayed
- **Axis**: The number lines along the edges of the plot
- **Other elements**: Titles, legends, labels, etc.

```python
# Create a simple figure and axes
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axes with specified size

# The fig is the entire canvas, and ax is the plot area
ax.set_title('My First Plot')  # Set the title of the plot
ax.set_xlabel('X Axis Label')  # Set the label for the x-axis
ax.set_ylabel('Y Axis Label')  # Set the label for the y-axis

# Display the plot
plt.show()
```

### Creating Basic Plots

#### Line Plots
Line plots show trends over time or relationships between continuous variables.

```python
# Extract Mathematics scores for different class levels
ss1_math = students_df[students_df['class_level'] == 'SS1']['Mathematics']
ss2_math = students_df[students_df['class_level'] == 'SS2']['Mathematics']
ss3_math = students_df[students_df['class_level'] == 'SS3']['Mathematics']

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a line representing the distribution of math scores
ax.plot(range(len(ss1_math)), sorted(ss1_math), label='SS1', color='blue', marker='o')
ax.plot(range(len(ss2_math)), sorted(ss2_math), label='SS2', color='green', marker='s')
ax.plot(range(len(ss3_math)), sorted(ss3_math), label='SS3', color='red', marker='^')

# Add labels and title
ax.set_title('Distribution of Mathematics Scores by Class Level')
ax.set_xlabel('Student Rank')
ax.set_ylabel('Mathematics Score')
ax.legend()  # Display the legend

# Display the plot
plt.show()
```

The `plt.plot()` function creates a line plot. Parameters:
- First argument: X-coordinates
- Second argument: Y-coordinates
- `label`: Text for the legend
- `color`: Color of the line
- `marker`: Shape to mark each data point (e.g., 'o' for circles, 's' for squares)


## Additional Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Python Graph Gallery](https://python-graph-gallery.com/) - Examples of various plot types
- [Data Visualization Catalogue](https://datavizcatalogue.com/) - Guide to choosing the right visualization
- [Data Visualization Checklist](https://depictdatastudio.com/checklist/) - Best practices for visualization
