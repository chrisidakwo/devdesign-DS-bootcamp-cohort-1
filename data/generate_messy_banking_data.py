import random
from datetime import datetime, timedelta

import pandas as pd

def generate_messy_banking_data(n_records=150):
    """
    Generate a realistic Nigerian banking dataset with common data quality issues
    that students will need to clean and prepare for machine learning.
    """

    # Nigerian names for realistic context
    nigerian_first_names = [
        'Adebayo', 'Amara', 'Chidi', 'Emeka', 'Fatima', 'Grace', 'Ibrahim', 'Joy',
        'Kemi', 'Lawal', 'Musa', 'Ngozi', 'Olumide', 'Peace', 'Rasheed', 'Sarah',
        'Tunde', 'Uche', 'Victor', 'Yemi', 'Zainab', 'Ahmed', 'Blessing', 'Daniel',
        'Esther', 'Felix', 'Halima', 'Isaac', 'Janet', 'Kingsley', 'Lydia', 'Moses',
        'Nkem', 'Ola', 'Patricia', 'Queen', 'Raymond', 'Stella', 'Timothy', 'Uma'
    ]

    nigerian_last_names = [
        'Adebayo', 'Okafor', 'Nwachukwu', 'Abubakar', 'Williams', 'Johnson', 'Eze',
        'Adeyemi', 'Ibrahim', 'Okonkwo', 'Musa', 'Adewale', 'Nwosu', 'Hassan',
        'Ogbonna', 'Yakubu', 'Okoro', 'Bello', 'Chioma', 'Danjuma', 'Emeka',
        'Garba', 'Igwe', 'Jibril', 'Kalu', 'Lawal', 'Mahmud', 'Nnadi', 'Osei',
        'Patel', 'Qasim', 'Raji', 'Sani', 'Taiwo', 'Usman', 'Wale', 'Yusuf'
    ]

    nigerian_states = [
        'Lagos', 'Abuja', 'Rivers', 'Kano', 'Ogun', 'Kaduna', 'Oyo', 'Delta',
        'Edo', 'Anambra', 'Imo', 'Abia', 'Enugu', 'Cross River', 'Akwa Ibom',
        'Osun', 'Ondo', 'Ekiti', 'Kwara', 'Niger', 'Benue', 'Plateau', 'Taraba',
        'Adamawa', 'Borno', 'Yobe', 'Bauchi', 'Gombe', 'Jigawa', 'Katsina',
        'Kebbi', 'Sokoto', 'Zamfara', 'Nasarawa', 'Kogi', 'Bayelsa', 'Ebonyi'
    ]

    # Generate base data
    data = []

    for i in range(n_records):
        # Create customer ID (some will be missing or malformed)
        if random.random() < 0.05:  # 5% missing customer IDs
            customer_id = None
        elif random.random() < 0.03:  # 3% malformed IDs
            customer_id = f"CUS{random.randint(1, 999)}"  # Missing leading zeros
        else:
            customer_id = f"CUS{i+1:03d}"

        # Generate names (some missing, some with extra spaces)
        first_name = random.choice(nigerian_first_names)
        last_name = random.choice(nigerian_last_names)

        if random.random() < 0.03:  # 3% missing names
            full_name = ""
        elif random.random() < 0.05:  # 5% with formatting issues
            full_name = f"  {first_name.upper()} {last_name.lower()}  "
        else:
            full_name = f"{first_name} {last_name}"

        # Generate ages (with outliers and missing values)
        if random.random() < 0.04:  # 4% missing ages
            age = None
        elif random.random() < 0.02:  # 2% with impossible ages
            age = random.choice([150, 200, -5, 0, 300])
        else:
            age = random.randint(18, 80)

        # Generate states (with inconsistent formatting)
        state = random.choice(nigerian_states)
        if random.random() < 0.15:  # 15% with formatting issues
            variations = [
                state.upper(),
                state.lower(),
                state[:3] if len(state) > 3 else state,
                f"{state[:2]}.{state[2:4].upper()}." if len(state) > 4 else state,
                f"  {state}  "
            ]
            state = random.choice(variations)

        # Generate income (with missing values and wrong data types)
        base_income = random.randint(30000, 500000)
        if random.random() < 0.08:  # 8% missing income
            income = None
        elif random.random() < 0.05:  # 5% as strings with formatting
            income = f"₦{base_income:,}"
        elif random.random() < 0.03:  # 3% as strings without formatting
            income = str(base_income)
        else:
            income = base_income

        # Generate account balance (with negative outliers)
        if random.random() < 0.02:  # 2% with impossible negative balances
            balance = random.randint(-1000000, -100000)
        elif random.random() < 0.01:  # 1% with extreme positive outliers
            balance = random.randint(50000000, 100000000)
        else:
            balance = random.randint(1000, 5000000)

        # Generate phone numbers (various formats)
        base_phone = f"080{random.randint(10000000, 99999999)}"
        if random.random() < 0.05:  # 5% missing phones
            phone = None
        elif random.random() < 0.2:  # 20% with different formats
            formats = [
                f"+234{base_phone[1:]}",
                f"{base_phone[:4]}-{base_phone[4:7]}-{base_phone[7:]}",
                f"{base_phone[:4]} {base_phone[4:7]} {base_phone[7:]}",
                base_phone[1:],  # Missing leading 0
                f"0{base_phone[3:]}"  # Different provider code
            ]
            phone = random.choice(formats)
        else:
            phone = base_phone

        # Generate employment type
        employment_types = ['Government', 'Private', 'Self-employed', 'Student', 'Retired']
        # employment_types = ['Government', 'Private', 'Self-employed', 'Student', 'Retired', 'Public Servant']
        employment = random.choice(employment_types)

        # Generate account type
        account_types = ['Savings', 'Current', 'Fixed Deposit', 'Student']
        account_type = random.choice(account_types)

        # Generate loan history (some with inconsistent values)
        if random.random() < 0.7:  # 70% have loan history
            loans_taken = random.randint(0, 5)
            if random.random() < 0.05:  # 5% with text instead of numbers
                loans_taken = random.choice(['None', 'Many', 'Few', 'Several'])
        else:
            loans_taken = 0

        # Generate marital status (with inconsistent formatting)
        marital_statuses = ['Single', 'Married', 'Divorced', 'Widowed']
        marital_status = random.choice(marital_statuses)
        if random.random() < 0.1:  # 10% with formatting issues
            variations = {
                'Single': ['single', 'SINGLE', 'S', 'Not Married'],
                'Married': ['married', 'MARRIED', 'M', 'Wed'],
                'Divorced': ['divorced', 'DIVORCED', 'D', 'Separated'],
                'Widowed': ['widowed', 'WIDOWED', 'W', 'Widow']
            }
            marital_status = random.choice(variations.get(marital_status, [marital_status]))

        # Generate education level
        education_levels = ['Primary', 'Secondary', 'University', 'Masters', 'PhD']
        education = random.choice(education_levels)

        # Generate registration date (some with wrong formats)
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2024, 12, 31)
        reg_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

        if random.random() < 0.1:  # 10% with wrong date formats
            date_formats = [
                reg_date.strftime("%d/%m/%Y"),
                reg_date.strftime("%m-%d-%Y"),
                reg_date.strftime("%d-%b-%Y"),
                reg_date.strftime("%Y/%m/%d"),
                "Invalid Date",
                ""
            ]
            registration_date = random.choice(date_formats)
        else:
            registration_date = reg_date.strftime("%Y-%m-%d")

        # Generate credit score (with some outliers)
        if random.random() < 0.02:  # 2% with impossible credit scores
            credit_score = random.choice([1000, -100, 2000])
        elif random.random() < 0.05:  # 5% missing
            credit_score = None
        else:
            credit_score = random.randint(300, 850)

        data.append({
            'customer_id': customer_id,
            'full_name': full_name,
            'age': age,
            'state': state,
            'monthly_income': income,
            'account_balance': balance,
            'phone_number': phone,
            'employment_type': employment,
            'account_type': account_type,
            'previous_loans': loans_taken,
            'marital_status': marital_status,
            'education_level': education,
            'registration_date': registration_date,
            'credit_score': credit_score
        })

    # Create DataFrame
    df = pd.DataFrame(data)

    # Introduce some duplicate records (10-15 duplicates)
    duplicate_indices = random.sample(range(len(df)), 12)
    duplicate_rows = df.iloc[duplicate_indices].copy()

    # Modify duplicates slightly to make them realistic
    for idx, row in duplicate_rows.iterrows():
        # Same person, different phone or slight name variation
        if pd.notna(row['phone_number']) and random.random() < 0.5:
            # Change phone format
            phone = str(row['phone_number'])
            if phone.startswith('080'):
                duplicate_rows.at[idx, 'phone_number'] = f"+234{phone[1:]}"

        if pd.notna(row['full_name']) and random.random() < 0.3:
            # Slight name variation
            name_parts = str(row['full_name']).split()
            if len(name_parts) >= 2:
                duplicate_rows.at[idx, 'full_name'] = f"{name_parts[0]} {name_parts[1][:3]}."

    # Add duplicates to main dataframe
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    # Shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)

    return df


def main():
    banking_df = generate_messy_banking_data(250)

    # Save to CSV
    banking_df.to_csv('banking_data.csv', index=False)

if __name__ == '__main__':
    main()