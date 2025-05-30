import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_student_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)

# Explore your data
# df.shape, df.describe(), df.head(), df.types

# 1. Missing Data
# customer_data = {
#     'customer_id': ['CUS001', 'CUS002', 'CUS003'],
#     'age': [28, None, 35],                    # Missing age
#     'income': [120000, 250000, None],         # Missing income
#     'account_balance': [50000, None, 80000],  # Missing balance
#     'state': ['Lagos', 'Abuja', '']          # Empty string
# }

print('============= HANDLING MISSING DATA =============')
def handle_missing_data(df):
    """Find and handle missing data"""

    # Check for missing data
    print('Missing values per column:')
    print(df.isnull().sum())
    print('\n')

    # Visualize missing data pattern
    plt.figure(figsize=(8, 10))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False)
    plt.title('Missing Data Patterns')
    plt.tight_layout()
    plt.show()

    # Option 1: Remove rows with missing values (if row count is few or not significant)
    df_cleaned = df.dropna()

    # Option 2: Remove columns with too many missing values
    df_cleaned = df.dropna(axis=1, thresh=0.7*len(df)) # Keep columns with less than 30% missing data

    # Option 3: Fill with appropriate values

    # For numerical data
    # df['math_score'].fillna(df['math_score'].mean(), inplace=True)
    df['math_score'].fillna(0, inplace=True)

    # For categorical data
    df['gender'].fillna(df['gender'].mode(), inplace=True) # Fill with the most common/occurring value
    df['gender'].fillna('Unknown', inplace=True) # Fill with a default/placeholder

    df['gender'].fillna(method='ffill', inplace=True) # Use previous value. Hint: because of the ffill method

    # df['temperature'].fillna(method='ffill', inplace=True)


# # 2. Outliers and Impossible Values
# student_scores = {
#     'age': [16, 17, 16, 150, 18],        # 150 years old? Impossible!
#     'score': [85, 92, 78, 450, 88],      # 450 out of 100? Error!
#     'height': [1.65, 1.72, 15.2, 1.80], # 15.2 meters tall? Wrong unit!
#     'attendance': [0.95, 0.87, 1.5, 0.92] # 150% attendance? Impossible!
# }

def handle_outliers(df):
    """Find and handle outliers in data"""

    # z-score
    # IQR
    pass


# 2. Inconsistent Formatting
product_data = {
    'location': ['Lagos', 'LAGOS', 'lagos', 'Lag', 'L.A.G.O.S'],  # Same city, different formats
    'phone': ['+2348012345678', '08012345678', '8012345678'],      # Different phone formats
    'date': ['15/03/2024', '2024-03-15', '15-Mar-2024'],          # Different date formats
    'gender': ['M', 'Male', 'male', 'MAN', 'Boy', 'Mr'],             # Same gender, different values
}


#4. Duplicate Records
customers = {
    'name': ['John Adebayo', 'John Adebayo', 'Mary Okafor', 'Mary Okafor'],
    'phone': ['08012345678', '08012345678', '08087654321', '08087654321'],
    'email': ['john@email.com', 'john@gmail.com', 'mary@email.com', 'mary@email.com']
}

#5. Wrong data types
loan_data = {
    'amount': ['500000', '1000000', '750000'],    # Should be numbers, not text
    'approved': ['Yes', 'No', 'Maybe'],          # Should be True/False/True
    'date': ['20240315', '15/03/2024'],          # Should be datetime objects
    'interest_rate': ['15%', '12.5%', '18%']     # Should be decimal numbers
}


def main():
    students_df = load_student_data('../../data/students_record.csv')

    handle_missing_data(students_df)


from sklearn.preprocessing import StandardScaler, MinMaxScaler


if __name__ == '__main__':
    main()