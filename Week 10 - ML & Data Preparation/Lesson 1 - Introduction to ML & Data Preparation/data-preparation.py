import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_banking_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)


def visualize_missing_data(df):
    plt.figure(figsize=(8, 10))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False)
    plt.title('Missing Data Patterns')
    plt.tight_layout()
    plt.show()


def data_exploration(df):
    print('Banking data rows and columns: ', df.shape)

    print('\nWhat are the data types for the columns')
    print(df.dtypes)

    print('\nColumn names', df.columns.tolist())

    print('\nBasic summary statistics')
    print(df.describe())

    print('\nFirst 20 rows')
    print(df.head(20))

    print('\nDataset info:')
    print(df.info())


def handle_missing_data(df):
    """Find and handle missing data"""

    print('\n\nHandle Missing Customer IDs')

    missing_ids = df['customer_id'].isnull().sum()
    new_df = df.dropna(subset=['customer_id'])

    print(f'Removed {missing_ids} customer rows missing a customer ID')

    return new_df


def remove_duplicate_records(df):
    print('\n\nRemove duplicate records')

    duplicated_records = df.duplicated(subset=['customer_id']).sum()
    df = df.drop_duplicates(subset=['customer_id'], keep='first')

    print(f'Removed {duplicated_records} duplicate records')

    return df


def clean_customers_names(df):
    print('\n\nClean customers\' names')

    # Use a heatmap to visualize the number of cells with missing data, for each column
    visualize_missing_data(df)

    # Remove empty names
    empty_name_count = ((df['full_name'].isnull()) | (df['full_name'].str.strip() == '')).sum()

    df = df[df['full_name'].notna() & (df['full_name'].str.strip() != '')]

    def standardize_name(name):
        if pd.isna(name):
            return name

        # Remove extra spaces
        name = str(name).strip()

        # Remove multiple spaces
        name = ' '.join(name.split())

        # Standardize capitalization
        name = name.title()

        return name


    df['full_name'] = df['full_name'].apply(standardize_name)

    print(f'Removed {empty_name_count} rows with empty customer names')

    return df


def handle_outliers(df):
    print('\n\nHandle outliers and missing data in age')

    outliers_count = (
            (df['age'] < 18) |
            (df['age'] > 120)
    ).sum()

    missing_ages_count = df['age'].isnull().sum()

    # Remove impossible ages (outliers). Only retain rows that pass the filter condition
    df = df[
        (df['age'] >= 18) &
        (df['age'] <= 120)
    ]

    # Fill missing age with median
    median_age = df['age'].median()
    df.fillna({'age': median_age}, inplace=True)

    print(f'Removed {outliers_count} rows with empty with invalid ages')
    print(f'Filled {missing_ages_count} missing ages with the median age: {median_age}')

    return df


def standardize_state_names(df):
    print('\n\nStandardize state names')

    # State mapping
    states_map = {
        'ab.uj': 'Abuja',
        'an.am.': 'Anambra',
        'ji.ga.': 'Jigawa',
        'so.ko.': 'Sokoto',
        'Na.sa.': 'Nasarawa',
        'go.mb.': 'Gombe',
        'cr.os.': 'Cross River',
        'za.mf.': 'Zamfara',
    }

    def standardize_state(state):
        if pd.isna(state):
            return state

        state = str(state).lower().strip()

        if state in states_map:
            return states_map[state]

        return state.title()


    df['state'] = df['state'].apply(standardize_state)

    return df


def clean_income_data(df):
    print('\n\nClean income data')

    def clean_income_value(income):
        if pd.isna(income):
            return np.nan

        # Method chaining

        # wrap in string object and clean
        # NOTE: Can also be done with a regex
        income_str = (str(income).replace('₦', '')
                      .replace(',', '')
                      .replace( ' ', '')
                      .strip())

        try:
            return float(income_str)
        except ValueError:
            return np.nan

    #
    df['monthly_income'] = df['monthly_income'].apply(clean_income_value)


    # Fill missing incomes with median
    missing_income_count = df['monthly_income'].isnull().sum()

    median_income = df['monthly_income'].median()
    df.fillna({'monthly_income': median_income}, inplace=True)

    print('Fixed income formatting issues')
    print(f'Filled {missing_income_count} missing income columns with median (₦{median_income:,.0f})')

    return df


def handle_account_balance_outliers(df):
    print('\n\nHandle account balance outliers')

    # Remove impossible/negative balances (likely data errors)

    negative_balances_count = (df['account_balance'] < 0).sum()

    # Only keep rows with account balance greater than zero(0)
    df = df[df['account_balance'] >= 0]

    # Cap extremely high balances (potential outliers)
    q99 = df['account_balance'].quantile(0.99)

    extreme_balances_count = df[df['account_balance'] > q99 * 10].sum()

    df.loc[df['account_balance'] > q99 * 10, 'account_balance'] = q99

    print(f'Removed {negative_balances_count} rows with negative account balance')
    print(f'Capped {extreme_balances_count} extremely high account balance')

    return df


def standardize_phone_numbers(df):
    print('\n\nStandardize phone numbers')

    def clean_phone_number(phone):
        if pd.isna(phone):
            return np.nan

        # Remove all non-digits
        phone = (str(phone).replace('+', '')
                 .replace(' ', '')
                 .replace('-', ''))

        # Using regex
        # phone = re.sub(r'\\D', '', str(phone))

        # Handle different formats
        if phone.startswith('234') and len(phone) == 13:
            phone = '0' + phone[3:]
        elif len(phone) == 10 and phone.startswith(('70', '80', '81', '90', '91')):
            phone = '0' + phone
        elif len(phone) == 11 and phone.startswith('0'):
            pass
        else:
            return np.nan

        # Validate the final format
        if len(phone) == 11 and phone.startswith('0'):
            return phone
        else:
            return np.nan

    df['phone_number'] = df['phone_number'].apply(clean_phone_number)

    # Drop columns with null values

    return df


def standardize_categorical_variables(df):
    print('\n\nStandardize categorical variables')

    employment_map = {
        'public servant': 'Government',
        'public': 'Government',
    }

    #
    df['employment_type'] = df['employment_type'].str.lower.map(employment_map).fillna(df['employment_type'])


    marital_status_map = {
        'd': 'Divorced',
        'w': 'Widowed',
        'wed': 'Married',
        'm': 'Married',
    }

    #
    df['marital_status'] = df['marital_status_map'].str.lower.map(marital_status_map).fillna(df['marital_status'])

    return df


def clean_loan_history(df):

    def clean_loan_value(loan_value):
        if pd.isna(loan_value):
            return 0

        # Handle text values
        loan_str = str(loan_value).lower()
        if loan_str in ['none', 'zero', 'nil']:
            return 0
        elif loan_str in ['many', 'several']:
            return 3 # Safe/reasonable assumption
        elif loan_str in ['few', 'some']:
            return 1

        try:
            return int(float(loan_value))
        except ValueError:
            return 0

    df['previous_loans'] = df['previous_loans'].apply(clean_loan_value)

    return df


# TODO: Provide links to resources to read up on working with datetime in Python
# https://docs.python.org/3/library/datetime.html
# https://www.programiz.com/python-programming/datetime
# https://www.geeksforgeeks.org/python-datetime-module/

def clean_date_formats(df):

    def clean_date(date):
        if pd.isna(date) or str(date).strip == '':
            return np.nan

        # Try different date formats
        date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y', '%d-%b-%Y', '%Y/%m/%d', '%d-%m-%Y']

        for fmt in date_formats:
            try:
                return pd.to_datetime(str(date), format=fmt)
            except ValueError:
                continue

        return np.nan

    df['registration_date'] = df['registration_date'].apply(clean_date)

    # Drop rows/cells with nan value
    df = df.dropna(subset=['registration_date'])

    return df


def handle_credit_scores(df):
    # Remove outliers/impossible values
    df =  df[
        (df['credit_score'].isnull()) |
        (df['credit_score'] >= 300 & (df['credit_score'] <= 850))
    ]

    # Fill missing credit scores with median
    median_credit_score = df['credit_score'].median()
    df.fillna({'credit_score': median_credit_score}, inplace=True)

    return df


def main():
    banking_df = load_banking_data('../../data/banking_data.csv')

    # Change the column name for employment type using any one of the approaches below

    # Option 1
    # banking_df = banking_df.rename(columns={
    #     'employment-type': 'employment_type',
    # })

    # Option 2
    banking_df.rename(columns={'employment-type': 'employment_type'}, inplace=True)

    # Rename registration date column
    banking_df.rename(columns={'registration date': 'registration_date'}, inplace=True)

    new_df = banking_df.copy()

    # Handle missing data
    new_df = handle_missing_data(new_df)

    # Remove all duplicated customer ID rows, while retaining the first/initial occurrence
    new_df = remove_duplicate_records(new_df)

    # Properly formats the presentation of the full names of customers
    new_df = clean_customers_names(new_df)

    # Removed impossible age values and fill rows with missing values with the median age of customers
    new_df = handle_outliers(new_df)

    new_df = standardize_state_names(new_df)

    new_df = clean_income_data(new_df)

    new_df = handle_account_balance_outliers(new_df)

    new_df = standardize_phone_numbers(new_df)

    # new_df = standardize_categorical_variables(new_df)

    new_df = clean_date_formats(new_df)

    new_df = clean_loan_history(new_df)

    new_df = handle_credit_scores(new_df)

    new_df.to_csv('../../data/banking_data_formatted.csv', index=False)


if __name__ == '__main__':
    main()