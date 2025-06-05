import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, recall_score, precision_score

def load_dataset(path):
    """Load dataset from file path into Pandas DataFrame"""
    return pd.read_csv(path)

def main():
    """Run logistic regression on loan dataset"""

    # Load dataset
    loan_data = load_dataset('../data/loan_data.csv')

    # Fill NaN columns - Approach 1
    loan_data['income'] = loan_data['income'].fillna(loan_data['income'].mode())
    loan_data['loan_amount'] = loan_data['loan_amount'].fillna(loan_data['loan_amount'].mean())
    loan_data['interest_rate'] = loan_data['interest_rate'].fillna(loan_data['interest_rate'].mean())

    # Fill NaN columns - Approach 2
    # loan_data.fillna({ 'income': loan_data['income'].mode() }, inplace=True)
    # loan_data.fillna({ 'loan_amount': loan_data['loan_amount'].mean() }, inplace=True)
    # loan_data.fillna({ 'interest_rate': loan_data['interest_rate'].mean() }, inplace=True)

    # Prepare data (assume preprocessing has been done)
    X = loan_data.drop([
        'customer_id', 'occupation', 'education', 'marital_status', 'has_mortgage', 'default'
    ], axis=1)  # Features
    y = loan_data['default'] # Target variable

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nPrecision Score:")
    # print(precision_score(y_test, y_pred))

    print("\nRecall Score:")
    # print(recall_score(y_test, y_pred))


if __name__ == '__main__':
    main()
