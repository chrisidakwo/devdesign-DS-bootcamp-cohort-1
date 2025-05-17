import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_student_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)


def basic_plot():
    (fig, ax) = plt.subplots(figsize=(10, 6))

    # The fig is the entire canvas, and ax is the plot area
    ax.set_title('Testing Axes Title')  # Set the title of the plot
    ax.set_xlabel('X-Axis Label')  # Set the label for the x-axis
    ax.set_ylabel('Y-Axis Label')  # Set the label for the y-axis

    plt.show()


def line_plot_sample(df):
    # Extract Mathematics scores for different class levels
    ss1_math = df[df['class_level'] == 'SS1']['Mathematics']
    ss2_math = df[df['class_level'] == 'SS2']['Mathematics']
    ss3_math = df[df['class_level'] == 'SS3']['Mathematics']

    print(ss3_math)

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(20, 12))

    # Create a line representing the distribution of math scores

    print("Number of SS1 maths students", len(ss1_math))
    print("Number of SS2 maths students", len(ss2_math))
    print("Number of SS3 maths students", len(ss3_math))

    ax.plot(range(len(ss1_math)), sorted(ss1_math), label='Secondary School 1', color='blue')
    ax.plot(range(len(ss2_math)), sorted(ss2_math), label='SS2', color='green')
    ax.plot(range(len(ss3_math)), sorted(ss3_math), label='SS3', color='red')

    # Add labels and title
    ax.set_title('Distribution of Mathematics Scores by Class Level')
    ax.set_xlabel('Student Rank')
    ax.set_ylabel('Mathematics Score')
    ax.legend()  # Display the legend

    ax.grid(True)

    plt.tight_layout()

    # Display the plot
    plt.show()


def format_bar_label(label):
    return f"{label:.1f}%"


def bar_chart_sample(df):
    class_level_means = df.groupby('class_level')[['Mathematics', 'English Language', 'Agriculture']].mean()

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
        ax.bar_label(container, fmt=format_bar_label, padding=3, label_type="center")

    # Display the plot
    plt.show()


def random_numbers_bar_chart():
    np.random.seed(28)

    data = np.random.randint(10, 550, size=7)

    print(data)

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the bar chart
    bars = ax.bar(range(len(data)), data, color='violet', edgecolor='black', alpha=1)

    for bar in bars:
        height = bar.get_height()
        half_width = bar.get_width() / 2

        ax.text(bar.get_x() + half_width, height + 1, f'{height}', ha='center', va='bottom')

    # Customize the chart
    ax.set_title('Weekly Sales Data', fontsize=16, fontweight='bold')
    # ax.set_xlabel('Week Days', fontsize=12)
    ax.set_ylabel('Sales Amount (in USD)', fontsize=12)

    # Set ticks values
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

    # TODO: Use a dynamic values (e.g: list comprehension) to build the list
    # ax.set_xticklabels(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

    ax.grid(axis='y', linestyle='dashed', alpha=0.3)

    # Improve aesthetics
    plt.tight_layout()

    plt.show()

    # Save chart
    # TODO: Generates a blank canvas
    # plt.savefig('weekly-sales-data.png', format='png', dpi=360, bbox_inches='tight')


def histogram_chart_sample(df):
    # Create a figure and axes
    (fig, ax) = plt.subplots(figsize=(40, 42))

    # Create a histogram of mathematics scores
    ax.hist(df[df['class_level'] == 'SS1']['Mathematics'], bins=10, color='skyblue', edgecolor='black')

    # Add labels and title
    ax.set_title('Distribution of Mathematics Scores')
    ax.set_xlabel('Score')
    ax.set_ylabel('Number of Students')

    # Add grid lines for readability
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot
    plt.show()


def scatter_chart_sample(df):
    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a scatter plot of Mathematics vs. English Language scores
    ax.scatter(df['Mathematics'], df['English Language'], c=df['attendance'], cmap='viridis')

    # Add labels and title
    ax.set_title('Mathematics vs. English Language Scores (colored by attendance)')
    ax.set_xlabel('Mathematics Score')
    ax.set_ylabel('English Language Score')

    # Add a colorbar to show what the colors represent
    cbar = plt.colorbar(ax.collections[0], ax=ax)
    cbar.set_label('Attendance Rate (%)')

    # Display the plot
    plt.show()


def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../data/students.csv')
    print(f"Loaded dataset with {students_df.shape[0]} students")

    line_plot_sample(students_df)


if __name__ == '__main__':
    main()
