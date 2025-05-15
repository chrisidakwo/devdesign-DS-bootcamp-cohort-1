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

#### Bar Charts
Bar charts are excellent for comparing values across categories.

```python
# Calculate average scores by class level for core subjects
class_level_means = students_df.groupby('class_level')[['Mathematics', 'English Language']].mean()

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar chart
class_level_means.plot(kind='bar', ax=ax)

# Add labels and title
ax.set_title('Average Scores by Class Level')
ax.set_xlabel('Class Level')
ax.set_ylabel('Average Score')
ax.legend(title='Subject')

# Add value labels on top of bars
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', padding=3)

# Display the plot
plt.show()
```

The `plot(kind='bar')` method creates a bar chart from a DataFrame. Parameters:
- `kind='bar'`: Specifies the type of plot (bar chart)
- `ax`: The axes object where to draw the plot
- `bar_label()`: Adds numerical labels to the top of each bar

#### Histograms
Histograms show the distribution of a single numerical variable.

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(40, 42))

# Create a histogram of mathematics scores
ax.hist(students_df['Mathematics'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)

# Add labels and title
ax.set_title('Distribution of Mathematics Scores')
ax.set_xlabel('Score')
ax.set_ylabel('Number of Students')

# Add grid lines for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
```

The `hist()` function creates a histogram. Parameters:
- First argument: Array of values to plot
- `bins`: Number of bins (bars) to divide the data into
- `color`: Fill color of the bars
- `edgecolor`: Color of the bar edges
- `alpha`: Transparency level (0 to 1)

#### Scatter Plots
Scatter plots show the relationship between two numerical variables.

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a scatter plot of Mathematics vs. English Language scores
ax.scatter(students_df['Mathematics'], students_df['English Language'], 
           c=students_df['attendance'], cmap='viridis', alpha=0.7)

# Add labels and title
ax.set_title('Mathematics vs. English Language Scores (colored by attendance)')
ax.set_xlabel('Mathematics Score')
ax.set_ylabel('English Language Score')

# Add a colorbar to show what the colors represent
cbar = plt.colorbar(ax.collections[0], ax=ax)
cbar.set_label('Attendance Rate (%)')

# Display the plot
plt.show()
```

The `scatter()` function creates a scatter plot. Parameters:
- First argument: X-coordinates
- Second argument: Y-coordinates
- `c`: Values used to color the points
- `cmap`: Colormap (palette) to use
- `alpha`: Transparency level

### Multiple Plots in a Single Figure

Often, we want to compare multiple plots side by side:

```python
# Create a figure with multiple subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Flatten the axes array for easier indexing
axes = axes.flatten()

# Plot 1: Histogram of Mathematics scores
axes[0].hist(students_df['Mathematics'], bins=10, color='skyblue', edgecolor='black')
axes[0].set_title('Mathematics Scores Distribution')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Count')

# Plot 2: Histogram of English Language scores
axes[1].hist(students_df['English Language'], bins=10, color='lightgreen', edgecolor='black')
axes[1].set_title('English Language Scores Distribution')
axes[1].set_xlabel('Score')
axes[1].set_ylabel('Count')

# Plot 3: Bar chart of average scores by gender
gender_means = students_df.groupby('gender')[['Mathematics', 'English Language']].mean()
gender_means.plot(kind='bar', ax=axes[2], color=['blue', 'orange'])
axes[2].set_title('Average Scores by Gender')
axes[2].set_xlabel('Gender')
axes[2].set_ylabel('Average Score')

# Plot 4: Scatter plot of Mathematics vs. English Language
scatter = axes[3].scatter(students_df['Mathematics'], students_df['English Language'], 
                         c=students_df['attendance'], cmap='viridis', alpha=0.7)
axes[3].set_title('Math vs. English Scores')
axes[3].set_xlabel('Mathematics Score')
axes[3].set_ylabel('English Language Score')
plt.colorbar(scatter, ax=axes[3], label='Attendance')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the figure
plt.show()
```

The `plt.subplots()` function creates a figure with multiple axes. Parameters:
- First argument: Number of rows
- Second argument: Number of columns
- `figsize`: Size of the overall figure

### Customizing Plots

Matplotlib offers extensive customization options:

```python
# Create a more customized plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create bar chart with custom colors
study_groups = students_df.groupby('study_group')[['Mathematics', 'English Language']].mean()
bars = study_groups.plot(kind='bar', ax=ax, color=['#3498db', '#e74c3c'], width=0.7)

# Add labels and title with custom styling
ax.set_title('Average Scores by Study Group', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Study Group', fontsize=12)
ax.set_ylabel('Average Score', fontsize=12)

# Customize the legend
ax.legend(title='Subject', title_fontsize=12, fontsize=10, loc='upper right')

# Customize grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels with custom format
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', fontweight='bold')

# Customize the background
ax.set_facecolor('#f8f9fa')

# Customize the axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#555555')
ax.spines['bottom'].set_color('#555555')

# Add a text annotation
avg_math = students_df['Mathematics'].mean()
ax.annotate(f'Overall Mathematics Average: {avg_math:.1f}', 
            xy=(0.5, 0.95), xycoords='axes fraction',
            fontsize=12, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", fc='yellow', alpha=0.3))

# Display the plot
plt.show()
```

Key customization functions:
- `set_title()`, `set_xlabel()`, `set_ylabel()`: Add text elements with formatting
- `legend()`: Customize the legend appearance and location
- `grid()`: Add grid lines with custom style
- `set_facecolor()`: Change background color
- `spines`: Control the border lines of the plot
- `annotate()`: Add text annotations to specific locations

## Hands-on Exercise 1: Creating Basic Plots

**Real-world Context**:
As an educational data analyst for a Nigerian school, you've been asked to create a dashboard showing key performance metrics. The school board wants clear visualizations to understand student performance patterns across different subjects and demographics.

**Tasks**:
1. Create a bar chart showing the average scores for different subjects in each class level (SS1, SS2, SS3)
2. Plot a histogram of attendance rates, with different colors for male and female students
3. Create a scatter plot comparing Mathematics and English Language scores, using different colors for study groups
4. Create a figure with 2 subplots:
    - One showing the distribution of scores in STEM subjects
    - One showing the distribution of scores in Arts subjects

**Why This Matters**:
In real-world data science scenarios, stakeholders often prefer visual representations over raw numbers. A well-designed visualization can instantly convey patterns that might take paragraphs to explain in text. Educational administrators use these visualizations to identify areas needing improvement and to track the effectiveness of interventions.

## Part 2: Advanced Visualization with Seaborn

### What is Seaborn?

Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn is designed to work well with Pandas DataFrames and includes built-in themes that make plots more aesthetically pleasing.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Let's continue using our Nigerian students dataset
students_df = pd.read_csv('nigerian_students_full.csv')

# Set the Seaborn style
sns.set_style("whitegrid")  # Options: "darkgrid", "whitegrid", "dark", "white", "ticks"
```

### Basic Seaborn Plots

#### Distributional Plots

**Histograms and KDE (Kernel Density Estimation)**

```python
# Create a figure
plt.figure(figsize=(12, 6))

# Create a histogram with KDE using Seaborn
sns.histplot(students_df['Mathematics'], kde=True, color='skyblue')

# Add labels and title
plt.title('Distribution of Mathematics Scores', fontsize=15)
plt.xlabel('Score', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Display the plot
plt.show()
```

The `histplot()` function creates a histogram with an optional KDE curve. Parameters:
- First argument: Data to plot
- `kde`: Whether to include a KDE curve
- `color`: Color of the histogram

**Box Plots**

Box plots show the distribution of a numerical variable through quartiles.

```python
# Create a figure
plt.figure(figsize=(12, 6))

# Create a box plot for core subjects by class level
sns.boxplot(x='class_level', y='value', hue='variable', 
            data=pd.melt(students_df, 
                         id_vars=['student_id', 'class_level'], 
                         value_vars=['Mathematics', 'English Language', 'Physics', 'Chemistry', 'Biology'],
                         var_name='variable'))

# Add labels and title
plt.title('Score Distribution by Subject and Class Level', fontsize=15)
plt.xlabel('Class Level', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.legend(title='Subject')

# Display the plot
plt.show()
```

The `boxplot()` function creates a box plot. Parameters:
- `x`: Categorical variable for grouping on the x-axis
- `y`: Numerical variable to show distribution
- `hue`: Additional categorical variable for sub-grouping
- `data`: DataFrame containing the data

The `pd.melt()` function restructures the data from wide to long format. Parameters:
- `id_vars`: Columns to use as identifier variables
- `value_vars`: Columns to unpivot
- `var_name`: Name for the variable column
- `value_name`: Name for the value column

**Violin Plots**

Violin plots combine box plots with KDE curves.

```python
# Create a figure
plt.figure(figsize=(14, 7))

# Create a violin plot for Mathematics scores by gender and class level
sns.violinplot(x='class_level', y='Mathematics', hue='gender', 
               data=students_df, split=True, inner='quart', palette='Set2')

# Add labels and title
plt.title('Mathematics Score Distribution by Class Level and Gender', fontsize=15)
plt.xlabel('Class Level', fontsize=12)
plt.ylabel('Mathematics Score', fontsize=12)
plt.legend(title='Gender')

# Display the plot
plt.show()
```

The `violinplot()` function creates a violin plot. Parameters:
- `x`: Categorical variable for grouping on the x-axis
- `y`: Numerical variable to show distribution
- `hue`: Additional categorical variable for sub-grouping
- `data`: DataFrame containing the data
- `split`: Whether to split the violins for the hue variable
- `inner`: Type of interior representation ('box', 'quart', 'point', etc.)
- `palette`: Color palette to use

#### Categorical Plots

**Bar Plots**

```python
# Create a figure
plt.figure(figsize=(14, 7))

# Create a bar plot for average scores by family income level
sns.barplot(x='family_income_level', y='Mathematics', 
            data=students_df, palette='Blues', 
            order=['Low', 'Lower Middle', 'Upper Middle', 'High'])

# Add labels and title
plt.title('Average Mathematics Score by Family Income Level', fontsize=15)
plt.xlabel('Family Income Level', fontsize=12)
plt.ylabel('Average Mathematics Score', fontsize=12)

# Add value labels on top of bars
for i, p in enumerate(plt.gca().patches):
    plt.gca().annotate(f'{p.get_height():.1f}', 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='bottom', fontsize=11)

# Display the plot
plt.show()
```

The `barplot()` function creates a bar plot with error bars. Parameters:
- `x`: Categorical variable for grouping on the x-axis
- `y`: Numerical variable to show distribution
- `data`: DataFrame containing the data
- `palette`: Color palette to use
- `order`: Custom ordering of the categories

**Count Plots**

Count plots show the counts of observations in each categorical bin.

```python
# Create a figure
plt.figure(figsize=(12, 6))

# Create a count plot for class level by gender
sns.countplot(x='class_level', hue='gender', data=students_df, palette='Set1')

# Add labels and title
plt.title('Number of Students by Class Level and Gender', fontsize=15)
plt.xlabel('Class Level', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Gender')

# Add count labels on top of bars
for p in plt.gca().patches:
    plt.gca().annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='bottom', fontsize=11)

# Display the plot
plt.show()
```

The `countplot()` function creates a count plot. Parameters:
- `x`: Categorical variable for grouping on the x-axis
- `hue`: Additional categorical variable for sub-grouping
- `data`: DataFrame containing the data
- `palette`: Color palette to use

#### Relational Plots

**Scatter Plots with Regression Line**

```python
# Create a figure
plt.figure(figsize=(10, 8))

# Create a scatter plot with regression line for Mathematics vs. attendance
sns.regplot(x='attendance', y='Mathematics', data=students_df, 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

# Add labels and title
plt.title('Relationship Between Attendance and Mathematics Score', fontsize=15)
plt.xlabel('Attendance Rate (%)', fontsize=12)
plt.ylabel('Mathematics Score', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

The `regplot()` function creates a scatter plot with a regression line. Parameters:
- `x`: Variable for the x-axis
- `y`: Variable for the y-axis
- `data`: DataFrame containing the data
- `scatter_kws`: Dictionary of keyword arguments for scatter plot
- `line_kws`: Dictionary of keyword arguments for the regression line

**Pair Plots**

Pair plots show pairwise relationships across variables.

```python
# Create a subset of the data with just core subjects and attendance
core_data = students_df[['Mathematics', 'English Language', 'attendance', 'gender']].dropna()

# Create a pair plot
sns.pairplot(core_data, hue='gender', palette='Set1', diag_kind='kde', 
             plot_kws={'alpha': 0.6}, height=2.5)

# Add a title
plt.suptitle('Pairwise Relationships Among Core Subjects and Attendance', y=1.02, fontsize=16)

# Display the plot
plt.show()
```

The `pairplot()` function creates a grid of pairwise relationships. Parameters:
- First argument: DataFrame containing the data
- `hue`: Categorical variable for color-coding
- `palette`: Color palette to use
- `diag_kind`: Type of plot for the diagonal ('hist', 'kde')
- `plot_kws`: Dictionary of keyword arguments for the plot
- `height`: Height of each subplot in inches

**Heat Maps**

Heat maps are great for visualizing correlation matrices.

```python
# Create a correlation matrix for numerical variables
corr_columns = ['Mathematics', 'English Language', 'Physics', 'Chemistry', 
                'Biology', 'attendance', 'disciplinary_count']
corr_matrix = students_df[corr_columns].corr()

# Create a figure
plt.figure(figsize=(12, 10))

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
            linewidths=0.5, vmin=-1, vmax=1)

# Add a title
plt.title('Correlation Matrix of Academic Performance Variables', fontsize=15, pad=20)

# Display the plot
plt.tight_layout()
plt.show()
```

The `heatmap()` function creates a heat map. Parameters:
- First argument: 2D dataset (typically a correlation matrix)
- `annot`: Whether to write the data value in each cell
- `cmap`: Colormap to use
- `fmt`: String formatting code for the annotations
- `linewidths`: Width of the lines that divide each cell
- `vmin`, `vmax`: Range of data to anchor the colormap on

### Customizing Seaborn Plots

Seaborn offers several ways to customize plots:

```python
# Set a specific theme
sns.set_theme(style="darkgrid", context="notebook", palette="deep", font="sans-serif")

# Create a more customized categorical plot
plt.figure(figsize=(14, 8))

# Custom bar plot with specific styling
bar_plot = sns.barplot(x='mother_occupation', y='Mathematics', 
                      data=students_df, palette='viridis',
                      errorbar=None, edgecolor='black', linewidth=1.5)

# Add labels and title with custom styling
plt.title('Average Mathematics Score by Mother\'s Occupation', fontsize=18, fontweight='bold')
plt.xlabel('Mother\'s Occupation', fontsize=14)
plt.ylabel('Average Mathematics Score', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Add value labels on top of bars
for i, p in enumerate(bar_plot.patches):
    if not np.isnan(p.get_height()):
        bar_plot.annotate(f'{p.get_height():.1f}', 
                         (p.get_x() + p.get_width() / 2., p.get_height() + 0.5), 
                         ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize grid and add a horizontal line at the average score
plt.grid(axis='y', linestyle='--', alpha=0.7)
avg_math = students_df['Mathematics'].mean()
plt.axhline(y=avg_math, color='red', linestyle='--', label=f'Overall Average: {avg_math:.1f}')
plt.legend(fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

Seaborn customization functions:
- `set_theme()`: Set the visual theme of all plots
- `set_style()`: Control the plot background and grid
- `set_context()`: Adjust plot scaling for different contexts
- `set_palette()`: Set the default color palette

## Hands-on Exercise 2: Advanced Data Visualization

**Real-world Context**:
You're working as a data scientist for the Nigerian Ministry of Education, tasked with analyzing factors that influence student performance across various demographic and socioeconomic dimensions. You need to create sophisticated visualizations that help policymakers understand the complex relationships in the data.

**Tasks**:
1. Create violin plots showing the distribution of Mathematics and English Language scores by family income level
2. Generate a pair plot showing relationships between core subject scores, colored by gender
3. Create a heat map showing the correlation between different subjects
4. Make a bar plot showing performance differences based on:
    - Whether students have a smartphone
    - Whether students have a part-time job
    - Daily study hours category

**Why This Matters**:
In policy analysis, understanding the relationships between socioeconomic factors and educational outcomes is crucial. These visualizations can help identify systemic issues and guide resource allocation. For example, if visualization reveals that students without smartphones consistently underperform, policymakers might consider technology access initiatives.

## Part 3: Creating Effective Visualizations for Education Data

### Choosing the Right Plot Type

Different types of data and questions require different visualization approaches:

| Question Type | Recommended Plot | Example |
|---------------|-----------------|---------|
| Distribution of a single variable | Histogram, KDE, Box plot | How are Mathematics scores distributed? |
| Comparison across categories | Bar chart, Box plot, Violin plot | How do different class levels compare in scores? |
| Relationship between variables | Scatter plot, Pair plot, Heat map | Is there a correlation between attendance and scores? |
| Composition of a whole | Pie chart, Stacked bar chart | What proportion of students are in each study group? |
| Trends over time or sequence | Line plot | How do scores change from SS1 to SS3? |

### Visualization Best Practices

1. **Choose appropriate visualizations** for your data type and question
2. **Keep it simple** - avoid unnecessary complexity
3. **Use clear labels** for axes, titles, and legends
4. **Use color effectively** but don't overuse it
5. **Maintain consistency** across multiple visualizations
6. **Highlight important information** through annotations or design elements
7. **Consider your audience** when determining level of detail

### Creating Visualization Projects

Let's create a complete visualization project to analyze Nigerian student performance:

```python
# Create a visualization project with multiple plots
fig, axes = plt.subplots(2, 2, figsize=(20, 16))

# Plot 1: Performance by study group and gender (top left)
sns.barplot(x='study_group', y='value', hue='gender', 
            data=pd.melt(students_df, 
                         id_vars=['student_id', 'gender', 'study_group'], 
                         value_vars=['Mathematics', 'English Language']),
            ax=axes[0, 0])
axes[0, 0].set_title('Average Scores by Study Group and Gender', fontsize=14)
axes[0, 0].set_xlabel('Study Group', fontsize=12)
axes[0, 0].set_ylabel('Average Score', fontsize=12)
axes[0, 0].legend(title='Gender')

# Plot 2: Correlation between attendance and academic performance (top right)
sns.scatterplot(x='attendance', y='Mathematics', hue='class_level', 
                size='daily_study_hours', sizes=(50, 200),
                data=students_df, ax=axes[0, 1], alpha=0.7)
axes[0, 1].set_title('Mathematics Score vs. Attendance by Class Level', fontsize=14)
axes[0, 1].set_xlabel('Attendance Rate (%)', fontsize=12)
axes[0, 1].set_ylabel('Mathematics Score', fontsize=12)
axes[0, 1].legend(title='Class Level', fontsize=10)

# Plot 3: Subject distribution by class level (bottom left)
# First, prepare the data
subjects = ['Mathematics', 'English Language', 'Physics', 'Chemistry', 'Biology']
plot_data = []
for subject in subjects:
    for level in students_df['class_level'].unique():
        scores = students_df[students_df['class_level'] == level][subject].dropna()
        if len(scores) > 0:  # Only add if there are scores for this combination
            plot_data.append({
                'Subject': subject,
                'Class Level': level,
                'Mean Score': scores.mean(),
                'Count': len(scores)
            })
plot_df = pd.DataFrame(plot_data)

# Create the plot
sns.barplot(x='Subject', y='Mean Score', hue='Class Level', 
            data=plot_df, ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Average Scores by Subject and Class Level', fontsize=14)
axes[1, 0].set_xlabel('Subject', fontsize=12)
axes[1, 0].set_ylabel('Average Score', fontsize=12)
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45, ha='right')
axes[1, 0].legend(title='Class Level')

# Plot 4: Socioeconomic factors (bottom right)
# Calculate average scores by income level
income_scores = students_df.groupby('family_income_level')['Mathematics', 'English Language'].mean().reset_index()
income_scores = pd.melt(income_scores, 
                        id_vars=['family_income_level'], 
                        value_vars=['Mathematics', 'English Language'],
                        var_name='Subject', value_name='Average Score')
income_scores['family_income_level'] = pd.Categorical(income_scores['family_income_level'], 
                                                      categories=['Low', 'Lower Middle', 'Upper Middle', 'High'], 
                                                      ordered=True)
income_scores = income_scores.sort_values('family_income_level')

sns.barplot(x='family_income_level', y='Average Score', hue='Subject', 
            data=income_scores, ax=axes[1, 1], palette='Set2')
axes[1, 1].set_title('Average Scores by Family Income Level', fontsize=14)
axes[1, 1].set_xlabel('Family Income Level', fontsize=12)
axes[1, 1].set_ylabel('Average Score', fontsize=12)
axes[1, 1].legend(title='Subject')

# Add an overall title
fig.suptitle('Nigerian Secondary School Student Performance Analysis', fontsize=20, y=0.98)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.93)

# Display the visualization
plt.show()

# Save the visualization as a file
plt.savefig('nigerian_student_performance.png', dpi=300, bbox_inches='tight')
```

### Interactive Visualizations

While Matplotlib and Seaborn create static visualizations, libraries like Plotly allow for interactive plots. While we won't implement interactive plots in this lesson, they are worth exploring for data presentations.

## Hands-on Exercise 3: Creating a Comprehensive Dashboard

**Real-world Context**:
You've been hired by a Nigerian educational consulting firm to create a comprehensive dashboard analyzing the factors affecting student performance. The company works with schools to develop targeted intervention programs, and they need data-driven insights to guide their recommendations.

**Tasks**:
1. Create a multi-panel dashboard (using plt.subplots) with at least 4 visualizations:
   - A visualization showing performance differences across socioeconomic factors (family income, parents' occupations)
   - A visualization analyzing the relationship between study habits (daily study hours) and academic performance
   - A visualization comparing performance across different demographics (gender, class level)
   - A visualization highlighting correlations between different academic subjects
2. Make sure your visualizations use appropriate plot types for the questions being answered
3. Use clear titles, labels, and legends
4. Use a consistent color scheme across all visualizations
5. Add annotations highlighting key insights

**Why This Matters**:
In professional data science roles, you'll often need to create comprehensive dashboards that tell a complete story with data. These dashboards help stakeholders make informed decisions without having to understand the underlying code or analysis. Educational consultants use such visualizations to identify which factors have the strongest impact on student outcomes, allowing schools to design more effective intervention programs.

## Key Takeaways

1. **Matplotlib Fundamentals**
   - Matplotlib provides a flexible, object-oriented approach to creating visualizations
   - Understanding the figure and axes structure is key to creating customized plots
   - Basic plot types (line, bar, histogram, scatter) serve as building blocks for more complex visualizations

2. **Seaborn Advantages**
   - Seaborn builds on Matplotlib to provide statistical visualizations with less code
   - Default styling in Seaborn is more aesthetically pleasing and modern
   - Specialized plots (violin plots, pair plots, heat maps) help reveal patterns in complex data

3. **Choosing the Right Visualization**
   - Match your visualization type to your data and the question you're trying to answer
   - Distributional plots show how values are spread
   - Relational plots show connections between variables
   - Categorical plots compare values across groups

4. **Effective Visualization Practices**
   - Clear labeling is essential for understanding
   - Consistent styling helps create cohesive dashboards
   - Avoiding clutter keeps focus on important patterns
   - Thoughtful color choices improve accessibility and clarity

5. **Educational Data Analysis**
   - Visualizations help identify factors affecting student performance
   - Multi-panel dashboards present a comprehensive view of complex educational data
   - Proper visualization makes patterns immediately apparent that might be missed in tables of numbers

## Take-Home Exercise: Nigerian Student Performance Dashboard

**Real-world Context**:
You're preparing a presentation for the Nigerian Education Committee that examines how various factors influence student academic performance. The committee wants to use this data to inform policy decisions about resource allocation and intervention programs.

**Tasks**:

1. Using the students.csv dataset, create a comprehensive visualization dashboard that addresses the following questions:
   - How do socioeconomic factors (family income, parent occupations, computers at home) affect academic performance?
   - What is the relationship between technology access (smartphones, computers) and academic performance?
   - How do study habits and extracurricular activities (daily study hours, daily gaming hours, jobs) relate to academic performance?
   - Are there significant performance differences across gender, class levels, or study groups?
   - Which subjects show the strongest correlations with each other?

2. Your dashboard should include:
   - At least 6 different types of visualizations (e.g., bar charts, scatter plots, box plots, heat maps)
   - Clear annotations highlighting key insights
   - A consistent color scheme and styling
   - Proper handling of missing values
   - A logical organization that tells a coherent story

3. Write a brief report (1-2 pages) summarizing:
   - Your key findings and their potential policy implications
   - Your visualization choices and why they were appropriate for the data
   - Any data limitations or areas for further investigation

**Submission**:
- Submit your Python script that generates the dashboard
- Include your visualization dashboard saved as a PNG or PDF
- Include your written report
- Be prepared to present your dashboard and findings in the next class

## Additional Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Python Graph Gallery](https://python-graph-gallery.com/) - Examples of various plot types
- [Data Visualization Catalogue](https://datavizcatalogue.com/) - Guide to choosing the right visualization
- [Data Visualization Checklist](https://depictdatastudio.com/checklist/) - Best practices for visualization
