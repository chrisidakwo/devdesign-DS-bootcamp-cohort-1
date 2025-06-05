import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

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
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)

    # Make predictions
    dt_pred = dt_model.predict(X_test)

    # Evaluate performance
    dt_accuracy = accuracy_score(y_test, dt_pred)
    print(f"Decision Tree Accuracy: {dt_accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, dt_pred))

    # Visualize the tree (for small trees only)
    plt.figure(figsize=(20, 10))
    tree.plot_tree(dt_model, feature_names=X.columns, filled=True,
                   class_names=['No Default', 'Default'], rounded=True)
    plt.title("Decision Tree for Loan Default Prediction")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
