import matplotlib.pyplot as plt
import pandas as pd


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

def math_score_distribution(df):
    # Extract Mathematics scores for different class levels
    ss1_math = df[df['class_level'] == 'SS1']['Mathematics']
    ss2_math = df[df['class_level'] == 'SS2']['Mathematics']
    ss3_math = df[df['class_level'] == 'SS3']['Mathematics']

    print(ss3_math)

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(20, 12))

    # Create a line representing the distribution of math scores

    ax.plot(range(len(ss1_math)), sorted(ss1_math), label='SS1', color='blue')
    ax.plot(range(len(ss2_math)), sorted(ss2_math), label='SS2', color='green')
    ax.plot(range(len(ss3_math)), sorted(ss3_math), label='SS3', color='red')

    # Add labels and title
    ax.set_title('Distribution of Mathematics Scores by Class Level')
    ax.set_xlabel('Student Rank')
    ax.set_ylabel('Mathematics Score')
    ax.legend()  # Display the legend

    # Display the plot
    plt.show()


def main():
    # 1. Load the student dataframe
    students_df = load_student_data('../../data/students.csv')
    print(f"Loaded dataset with {students_df.shape[0]} students")

    math_score_distribution(students_df)


if __name__ == '__main__':
    main()