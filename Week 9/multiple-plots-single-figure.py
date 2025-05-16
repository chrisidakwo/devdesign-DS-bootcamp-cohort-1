import matplotlib.pyplot as plt
import pandas as pd

def load_student_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)

def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../data/students.csv')
    print(f"Loaded dataset with {students_df.shape[0]} students")
    print('')

    # Create a figure with multiple subplots (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    print('Axes', axes)

    # Flatten the axes array for easier indexing
    axes = axes.flatten()

    print('Axes', axes)

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
    scatter = axes[3].scatter(
        students_df['Mathematics'],
        students_df['English Language'],
        c=students_df['attendance'],
        cmap='viridis'
    )
    axes[3].set_title('Math vs. English Scores')
    axes[3].set_xlabel('Mathematics Score')
    axes[3].set_ylabel('English Language Score')
    plt.colorbar(scatter, ax=axes[3], label='Attendance')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    plt.savefig('testing.png', format='png', dpi=300)
    plt.savefig('testing.svg', format='svg', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()