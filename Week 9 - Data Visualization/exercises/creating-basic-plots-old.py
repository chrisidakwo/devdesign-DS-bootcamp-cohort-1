import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the student data from CSV file"""
    return pd.read_csv(file_path)

def set_plot_style():
    """Set a consistent style for all plots"""
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['figure.figsize'] = [10, 6]

    # Define a consistent color palette
    colors = {
        'SS1': '#1f77b4',
        'SS2': '#ff7f0e',
        'SS3': '#2ca02c',

        'M': '#d62728',
        'F': '#9467bd',

        'Science': '#8c564b',
        'Arts': '#e377c2'
    }

    return colors

def create_subject_averages_bar_chart(df, colors, save_path=None):
    """
    Create a bar chart showing average scores for different subjects by class level

    Args:
        df: DataFrame containing student data
        colors: Dictionary of colors for consistent styling
        save_path: Optional path to save the figure
    """
    # Define the core subjects to analyze
    core_subjects = [
        'Mathematics', 'English Language', 'Physics', 'Chemistry', 'Biology', 'Further Mathematics',
        'Computer Science', 'Literature in English', 'Government', 'Economics'
    ]

    # Filter to subjects that have enough data
    subjects_to_plot = []
    for subject in core_subjects:
        if subject in df.columns and df[subject].notna().sum() > 10:
            subjects_to_plot.append(subject)

    # Calculate the mean scores by class level for each subject
    class_subject_means = df.groupby('class_level')[subjects_to_plot].mean().reset_index()

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(14, 8))

    # Set the width of a single bar and the positions for the groups
    bar_width = 0.25
    class_levels = class_subject_means['class_level'].unique()
    num_subjects = len(subjects_to_plot)
    x = np.arange(num_subjects)

    # Plot bars for each class level
    for i, class_level in enumerate(class_levels):
        class_data = class_subject_means[class_subject_means['class_level'] == class_level]
        scores = [class_data[subject].values[0] for subject in subjects_to_plot]
        bars = ax.bar(x + i*bar_width, scores, bar_width,
                      label=class_level, color=colors[class_level], alpha=0.8)

        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=8)

    # Add labels and title
    plt.title('Average Subject Scores by Class Level', fontsize=16, fontweight='bold')
    plt.xlabel('Subject', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.xticks(x + bar_width, subjects_to_plot, rotation=45, ha='right')
    plt.legend(title='Class Level')
    plt.grid(axis='y', alpha=0.3)

    # Adjust layout
    plt.tight_layout()

    # Save figure if requested
    if save_path:
        plt.savefig(save_path)

    plt.show()

def create_attendance_histogram(df, colors, save_path=None):
    """
    Create a histogram of attendance rates with different colors for male and female students

    Args:
        df: DataFrame containing student data
        colors: Dictionary of colors for consistent styling
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    # Extract attendance data by gender
    male_attendance = df[df['gender'] == 'M']['attendance']
    female_attendance = df[df['gender'] == 'F']['attendance']

    # Create histograms
    bins = np.linspace(75, 100, 11)  # Create 10 bins from 75% to 100%
    ax.hist(male_attendance, bins=bins, color=colors['M'], alpha=0.5, label='Male')
    ax.hist(female_attendance, bins=bins, color=colors['F'], alpha=0.5, label='Female')

    plt.title('Distribution of Student Attendance Rates by Gender', fontsize=16, fontweight='bold')
    plt.xlabel('Attendance Rate (%)', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)

    # Add annotations for the mean attendance by gender
    male_mean = male_attendance.mean()
    female_mean = female_attendance.mean()

    plt.axvline(male_mean, color=colors['M'], linestyle='--')
    plt.axvline(female_mean, color=colors['F'], linestyle='--')

    plt.text(male_mean+0.5, plt.gca().get_ylim()[1]*0.9,
             f'Male Mean: {male_mean:.1f}%', color=colors['M'], fontweight='bold')
    plt.text(female_mean+0.5, plt.gca().get_ylim()[1]*0.8,
             f'Female Mean: {female_mean:.1f}%', color=colors['F'], fontweight='bold')

    plt.tight_layout()

    # Save figure if requested
    if save_path:
        plt.savefig(save_path)

    plt.show()

def create_math_english_scatter_plot(df, colors, save_path=None):
    """
    Create a scatter plot comparing Mathematics and English Language scores by study group

    Args:
        df: DataFrame containing student data
        colors: Dictionary of colors for consistent styling
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter to only include rows where both subjects have values
    scatter_data = df.dropna(subset=['Mathematics', 'English Language'])

    # Plot points for each study group with different colors
    for study_group, color in [('Science', colors['Science']), ('Arts', colors['Arts'])]:
        group_data = scatter_data[scatter_data['study_group'] == study_group]
        ax.scatter(group_data['Mathematics'], group_data['English Language'],
                   color=color, label=study_group, s=80, alpha=0.7)

    plt.title('Mathematics vs. English Language Scores by Study Group', fontsize=16, fontweight='bold')
    plt.xlabel('Mathematics Score', fontsize=12)
    plt.ylabel('English Language Score', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Study Group')

    # Add a diagonal line representing equal scores in both subjects
    max_score = max(scatter_data['Mathematics'].max(), scatter_data['English Language'].max())
    plt.plot([0, max_score], [0, max_score], 'k--', alpha=0.3)

    # Add correlation annotation
    corr = scatter_data['Mathematics'].corr(scatter_data['English Language'])
    plt.annotate(f'Correlation: {corr:.2f}',
                 xy=(0.05, 0.95), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", fc='yellow', alpha=0.3),
                 fontsize=12, ha='left', va='top')

    plt.tight_layout()

    # Save figure if requested
    if save_path:
        plt.savefig(save_path)

    plt.show()

def prepare_boxplot_data(df, subjects):
    """
    Prepare data for boxplots

    Args:
        df: DataFrame containing student data
        subjects: List of subject names to include

    Returns:
        data_list: List of score arrays for each subject
        labels: List of subject names with valid data
    """
    data_list = []
    labels = []

    for subject in subjects:
        # Get non-null scores for this subject
        scores = df[subject].dropna().values
        if len(scores) > 0:
            data_list.append(scores)
            labels.append(subject)

    return data_list, labels

def customize_boxplot(box_dict, color='teal'):
    """
    Customize the appearance of a boxplot

    Args:
        box_dict: Dictionary returned by plt.boxplot()
        color: Base color for styling the boxplot
    """
    for box in box_dict['boxes']:
        box.set(color=color, linewidth=1.5)
        box.set(facecolor=f'light{color}' if color in ['blue', 'green'] else 'lavender', alpha=0.8)
    for whisker in box_dict['whiskers']:
        whisker.set(color=color, linewidth=1.5, linestyle='--')
    for cap in box_dict['caps']:
        cap.set(color=color, linewidth=1.5)
    for median in box_dict['medians']:
        median.set(color='red', linewidth=2)
    for flier in box_dict['fliers']:
        flier.set(marker='o', markerfacecolor=color, markersize=5, alpha=0.5)

def create_stem_arts_comparison(df, colors, save_path=None):
    """
    Create a figure with 2 subplots comparing STEM and Arts subject distributions

    Args:
        df: DataFrame containing student data
        colors: Dictionary of colors for consistent styling
        save_path: Optional path to save the figure
    """
    # Define STEM and Arts subjects
    stem_subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology',
                     'Computer Science', 'Further Mathematics']
    arts_subjects = ['Literature in English', 'Government', 'Economics',
                     'History', 'Civic Education', 'French']

    # Filter to subjects that exist in our dataset
    stem_subjects = [subject for subject in stem_subjects if subject in df.columns]
    arts_subjects = [subject for subject in arts_subjects if subject in df.columns]

    # Create a Figure with 2 subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    # Plot 1: Distribution of scores in STEM subjects
    stem_data, stem_labels = prepare_boxplot_data(df, stem_subjects)
    stem_box = axes[0].boxplot(stem_data, patch_artist=True, labels=stem_labels)
    customize_boxplot(stem_box, 'teal')

    axes[0].set_title('Distribution of Scores in STEM Subjects', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Subject', fontsize=12)
    axes[0].set_ylabel('Score', fontsize=12)
    axes[0].set_xticklabels(stem_labels, rotation=45, ha='right')
    axes[0].grid(axis='y', alpha=0.3)

    # Add mean score markers for each STEM subject
    for i, subject in enumerate(stem_labels):
        mean_score = df[subject].mean()
        axes[0].plot(i+1, mean_score, 'ro', markersize=8)

    # Plot 2: Distribution of scores in Arts subjects
    arts_data, arts_labels = prepare_boxplot_data(df, arts_subjects)
    arts_box = axes[1].boxplot(arts_data, patch_artist=True, labels=arts_labels)
    customize_boxplot(arts_box, 'purple')

    axes[1].set_title('Distribution of Scores in Arts Subjects', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Subject', fontsize=12)
    axes[1].set_ylabel('Score', fontsize=12)
    axes[1].set_xticklabels(arts_labels, rotation=45, ha='right')
    axes[1].grid(axis='y', alpha=0.3)

    # Add mean score markers for each Arts subject
    for i, subject in enumerate(arts_labels):
        mean_score = df[subject].mean()
        axes[1].plot(i+1, mean_score, 'ro', markersize=8)

    # Add an overall title for the figure
    fig.suptitle('Comparison of STEM vs. Arts Subject Score Distributions',
                 fontsize=18, fontweight='bold', y=1.05)

    plt.tight_layout()

    # Save figure if requested
    if save_path:
        plt.savefig(save_path)

    plt.show()

def print_data_summary(df):
    """Print a summary of the dataset"""
    print("Data Visualization Complete!")
    print(f"Total number of students analyzed: {len(df)}")
    print(f"Class levels: {', '.join(df['class_level'].unique())}")
    print(f"Study groups: {', '.join(df['study_group'].unique())}")


def main():
    """Main function to run the analysis"""
    # Load the data
    students_df = load_data('../../data/students.csv')

    # Set plot style and get colors
    colors = set_plot_style()

    # Task 1: Bar chart of average scores by subject and class level
    create_subject_averages_bar_chart(students_df, colors, 'subject_scores_by_class.png')

    # Task 2: Histogram of attendance rates by gender
    create_attendance_histogram(students_df, colors, 'attendance_by_gender.png')

    # Task 3: Scatter plot comparing Mathematics and English Language scores by study group
    create_math_english_scatter_plot(students_df, colors, 'math_vs_english.png')

    # Task 4: Create a figure with 2 subplots comparing STEM and Arts subject distributions
    create_stem_arts_comparison(students_df, colors, 'stem_vs_arts_distributions.png')

    # Print summary
    print_data_summary(students_df)


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()