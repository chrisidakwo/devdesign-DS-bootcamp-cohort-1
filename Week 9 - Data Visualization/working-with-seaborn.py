import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set the Seaborn style
# sns.set_style("whitegrid")  # Options: "darkgrid", "whitegrid", "dark", "white", "ticks"

def load_data(path):
    # Let's continue using our Nigerian students dataset
    return pd.read_csv(path)


def histogram_and_kde(df):
    # Create a figure
    plt.figure(figsize=(12, 6))

    # Create a histogram with KDE using Seaborn
    sns.histplot(df['Mathematics'], kde=True, color='skyblue')

    # Add labels and title
    plt.title('Distribution of Mathematics Scores', fontsize=15)
    plt.xlabel('Score', fontsize=12)
    plt.ylabel('Count', fontsize=12)

    # Display the plot
    plt.show()


def box_plot(df):
    # Create a figure
    plt.figure(figsize=(12, 6))

    # Create a box plot for core subjects by class level
    sns.boxplot(x='class_level', y='value', hue='variable',
        data=pd.melt(
            df,
            id_vars=['student_id', 'class_level'],
            value_vars=['Mathematics', 'English Language', 'Agriculture'],
            var_name='variable'
        )
    )

    # Add labels and title
    plt.title('Score Distribution by Subject and Class Level', fontsize=15)
    plt.xlabel('Class Level', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    # TODO: Hide the label
    plt.legend(title='Subject')

    # Display the plot
    plt.show()


def violin_plot(df):
    # Create a figure
    plt.figure(figsize=(14, 7))

    # Create a violin plot for Mathematics scores by gender and class level
    sns.violinplot(
        x='class_level',
        y='Mathematics',
        hue='gender',
        data=df,
        split=True,
        inner='quart',
        palette='Set2'
    )

    # Add labels and title
    plt.title('Mathematics Score Distribution by Class Level and Gender', fontsize=15)
    plt.xlabel('Class Level', fontsize=12)
    plt.ylabel('Mathematics Score', fontsize=12)
    plt.legend(title='Gender')

    # Display the plot
    plt.show()


def bar_plot(df):
    # Create a figure
    plt.figure(figsize=(14, 7))

    # Create a bar plot for average scores by family income level
    sns.barplot(
        x='family_income_level',
        y='Mathematics',
        data=df[df['class_level'] == 'SS1'],
        palette='Blues',
        hue="family_income_level",
        legend=False,
        order=['Low', 'Lower Middle', 'Upper Middle', 'High']
    )

    # Add labels and title
    plt.title('Average Mathematics Score by Family Income Level', fontsize=15)
    plt.xlabel('Family Income Level', fontsize=12)
    plt.ylabel('Average Mathematics Score', fontsize=12)

    # Add value labels on top of bars
    for i, p in enumerate(plt.gca().patches):
        plt.gca().annotate(
            f'{p.get_height():.1f}',
            (p.get_x() + p.get_width() / 2., p.get_height() + 10),
            ha='center',
            va='bottom',
            fontsize=11
        )

    # plt.grid(axis="y", alpha=0.3)

    # Display the plot
    plt.tight_layout()
    plt.show()


def count_plot(df):
    # Create a figure
    plt.figure(figsize=(12, 6))

    # Create a count plot for class level by gender
    sns.countplot(x='class_level', hue='gender', data=df, palette='Set1')

    # Add labels and title
    plt.title('Number of Students by Class Level and Gender', fontsize=15)
    plt.xlabel('', fontsize=12)
    plt.ylabel('Number of students', fontsize=12)
    plt.legend(title='Gender')

    # Add count labels on top of bars
    for p in plt.gca().patches:
        plt.gca().annotate(f'{int(p.get_height())}',
                           (p.get_x() + p.get_width() / 2., p.get_height()),
                           ha='center', va='bottom', fontsize=11)

    plt.tight_layout()

    # Display the plot
    plt.show()


def scatter_plot(df):
    # Create a figure
    plt.figure(figsize=(10, 8))

    # Create a scatter plot with regression line for Mathematics vs. attendance
    sns.regplot(x='attendance', y='Mathematics', data=df,
                scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

    # Add labels and title
    plt.title('Relationship Between Attendance and Mathematics Score', fontsize=15)
    plt.xlabel('Attendance Rate (%)', fontsize=12)
    plt.ylabel('Mathematics Score', fontsize=12)

    # Display the plot
    plt.tight_layout()
    plt.show()


def pair_plot(df):
    # Create a subset of the data with just core subjects and attendance
    core_data = df[['Mathematics', 'English Language', 'Agriculture', 'attendance', 'gender']].dropna()

    # Create a pair plot
    sns.pairplot(
        core_data,
        hue='gender',
        palette='Set1',
        diag_kind='hist',
        plot_kws={'alpha': 0.6},
        height=2.5
    )

    # Add a title
    plt.suptitle('Pairwise Relationships Among Core Subjects and Attendance', y=1.02, fontsize=16)

    # Display the plot
    plt.show()


def main():
    students_df = load_data('../data/students-old.csv')
    pair_plot(students_df)


if __name__ == '__main__':
    main()