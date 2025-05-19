import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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

        'Science': 'teal',
        'Arts': 'purple'
    }

    return colors

def subject_averages_bar_chart(df):
    core_subjects = [
        'Mathematics', 'English Language', 'Agriculture', 'Physics', 'Chemistry', 'Biology',
        'Further Mathematics', 'Computer Science', 'Literature in English', 'Government', 'Economics'
    ]

    subjects_to_plot = []
    for subject in core_subjects:
        if subject in df.columns and df[subject].notna().sum() > 200:
            subjects_to_plot.append(subject)

    class_subject_means = df.groupby('class_level')[subjects_to_plot].mean().reset_index()

    fig, ax = plt.subplots(figsize=(14, 8))

    # Set the width of a single bar and the positions for the groups
    bar_width = 0.25
    class_levels = class_subject_means['class_level'].unique()
    num_subjects = len(subjects_to_plot)
    x = np.arange(num_subjects)

    colors = set_plot_style()

    # Plot bars for each class level
    for i, class_level in enumerate(class_levels):
        class_data = class_subject_means[class_subject_means['class_level'] == class_level]
        scores = [class_data[subject].values[0] for subject in subjects_to_plot]
        bars = ax.bar(
            x + (i*bar_width),
            scores,
            bar_width,
            label=class_level,
            color=colors[class_level],
            alpha=0.8
        )

        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2.,
                height + 1,
                f'{height:.1f}',
                ha='center',
                va='bottom',
                fontsize=8
            )

    # Add labels and title
    plt.title('Average Subject Scores by Class Level', fontsize=16, fontweight='bold')
    plt.xlabel('Subject', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.xticks(x + bar_width, subjects_to_plot, rotation=45, ha='right')
    plt.legend(title='Class Level')
    plt.grid(axis='y', alpha=0.3)

    # Adjust layout
    plt.tight_layout()

    plt.show()

def create_attendance_histogram(df):
    fig, ax = plt.subplots(figsize=(12, 6))

    # Extract attendance data by gender
    male_attendance = df[df['gender'] == 'M']['attendance']
    female_attendance = df[df['gender'] == 'F']['attendance']

    colors = set_plot_style()

    # Create histograms
    bins = np.linspace(75, 100, 11)  # Create 10 bins from 75% to 100%
    ax.hist(male_attendance, bins=bins, color=colors['M'], alpha=0.5, label='Male')
    ax.hist(female_attendance, bins=bins, color=colors['F'], alpha=0.5, label='Female')

    plt.title('Distribution of Student Attendance Rates by Gender', fontsize=16, fontweight='bold')
    plt.xlabel('Attendance Rate (%)', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.legend()

    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    plt.show()


def create_math_english_scatter_plot(df):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter to only include rows where both subjects have values
    scatter_data = df.dropna(subset=['Mathematics', 'English Language'])

    colors = set_plot_style()

    # Plot points for each study group with different colors
    for (study_group, color) in [('Science', colors['Science']), ('Arts', colors['Arts'])]:
        group_data = scatter_data[scatter_data['study_group'] == study_group]
        ax.scatter(
            group_data['Mathematics'],
            group_data['English Language'],
            color=color,
            label=study_group,
            s=80,
            alpha=0.7
        )

    plt.title('Mathematics vs. English Language Scores by Study Group', fontsize=16, fontweight='bold')
    plt.xlabel('Mathematics Score', fontsize=12)
    plt.ylabel('English Language Score', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Study Group')

    plt.tight_layout()

    plt.show()

def prepare_boxplot_data(df, subjects):
    data_list = []
    labels = []

    for subject in subjects:
        # Get non-null scores for this subject

        scores = df[subject].dropna().values # dropping all NaN or null/empty cells (in a row)
        if len(scores) > 0:
            data_list.append(scores)
            labels.append(subject)

    return (data_list, labels)


def customize_boxplot(box_dict, color='blue'):
    """
    Customize the appearance of a boxplot

    Args:
        box_dict: Dictionary returned by plt.boxplot()
        color: Base color for styling the boxplot
    """
    for box in box_dict['boxes']:
        box.set(color="black", linewidth=1.5,)
        box.set(facecolor=f'{color}', alpha=0.5)

    for whisker in box_dict['whiskers']:
        whisker.set(color=color, linewidth=1.5, linestyle='--')

    for cap in box_dict['caps']:
        cap.set(color=color, linewidth=1.5)

    for median in box_dict['medians']:
        median.set(color='orange', linewidth=1.5)

    for flier in box_dict['fliers']:
        flier.set(marker='o', markerfacecolor=color, markersize=5, alpha=0.5)


def create_stem_arts_comparison(df):
    # Define STEM and Arts subjects
    stem_subjects = [
        'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science',
        'Further Mathematics', 'Agriculture'
    ]
    arts_subjects = [
        'Literature in English', 'Government', 'Economics', 'English Language', 'History',
        'Civic Education', 'French', 'Agriculture', 'History'
    ]

    # Filter to subjects that exist in our dataset
    stem_subjects = [subject for subject in stem_subjects if subject in df.columns]
    arts_subjects = [subject for subject in arts_subjects if subject in df.columns]

    # Create a Figure with 2 subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    # Plot 1: Distribution of scores in STEM subjects
    stem_subjects_scores, stem_subject_names = prepare_boxplot_data(df, stem_subjects)
    stem_box = axes[0].boxplot(stem_subjects_scores, patch_artist=True, labels=stem_subject_names)
    customize_boxplot(stem_box, 'teal')

    axes[0].set_title('Distribution of Scores in STEM Subjects', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Score', fontsize=12)
    axes[0].set_xticklabels(stem_subject_names, rotation=45, ha='right')
    axes[0].grid(axis='y', alpha=0.3)

    # Add mean score markers for each STEM subject
    for i, subject in enumerate(stem_subject_names):
        mean_score = df[subject].mean()
        axes[0].plot(i+1, mean_score, 'ro', markersize=8)

    # Plot 2: Distribution of scores in Art subjects
    art_subjects_scores, art_subject_names = prepare_boxplot_data(df, arts_subjects)
    art_box = axes[1].boxplot(art_subjects_scores, patch_artist=True, labels=art_subject_names)

    axes[1].set_title('Distribution of Scores in Arts Subjects', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Score', fontsize=12)
    axes[1].set_xticklabels(art_subject_names, rotation=45, ha='right')
    axes[1].grid(axis='y', alpha=0.3)

    # Add mean score markers for each Arts subject
    for i, subject in enumerate(art_subject_names):
        mean_score = df[subject].mean()
        axes[1].plot(i+1, mean_score, 'ro', markersize=8)

    # Add an overall title for the figure
    fig.suptitle('Comparison of STEM vs. Arts Subject Score Distributions',
                 fontsize=18, fontweight='bold', y=1.05)

    plt.tight_layout()
    plt.show()



def main():
    """Main function to run the analysis"""

    # Load the data
    students_df = load_data('../../data/students-old.csv')
    create_stem_arts_comparison(students_df)


if __name__ == "__main__":
    main()


# stem_subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology',
#                  'Computer Science', 'Further Mathematics']
# arts_subjects = ['Literature in English', 'Government', 'Economics',
#                  'History', 'Civic Education', 'French']