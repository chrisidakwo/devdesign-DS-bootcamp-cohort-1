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
    ax.grid(axis='y', linestyle='--', alpha=0.4)

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

    # TODO: Add padding at the top, before annotation

    # Add a text annotation
    avg_math = students_df['Mathematics'].mean()
    ax.annotate(f'Overall Mathematics Average: {avg_math:.1f}',
        xy=(0.5, 0.95), xycoords='axes fraction',
        fontsize=12, ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.3", fc='yellow', alpha=0.3)
    )

    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()