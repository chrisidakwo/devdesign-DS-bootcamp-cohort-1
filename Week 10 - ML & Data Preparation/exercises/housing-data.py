import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

# In this tutorial, we used the linear regression model for our prediction, and that's because
# linear regression finds the straight line that best fits through your data points.
# It considers how input variables (like house size, age) relate to an outcome (like price)
# and uses that pattern to make predictions.

# Here are some best scenarios to use it:
#
# 1. When you expect roughly straight-line relationships between inputs and outputs
# (like in the case of the housing dataset, where we expect that each feature contributes a positive correction with the target variable - being the property price)
# 2. When you need to understand which factors matter most (it tells you the importance of each variable)
# 3. When you want a simple, fast model that's easy to interpret and explain
# 4. For baseline predictions before trying more complex methods
#
# Examples: Predicting sales based on advertising spend, estimating delivery times based on distance and traffic,
# or forecasting energy usage based on temperature and building size.

# Linear regression works best when your relationships are reasonably straight-forward,
# and you value simplicity and interpretability over perfect accuracy.

def load_data(path):
    """Loads student data from a CSV file specified in the path argument"""

    return pd.read_csv(path)


def explore_data(df):
    """Perform initial data exploration"""
    print("="*50)
    print("DATASET OVERVIEW")
    print("="*50)
    print(f"Dataset Shape: {df.shape}")
    print(f"Number of properties: {len(df)}")

    print('\nDataset Highlight Information:')
    print(df.info())

    print("\nColumn Information:")
    for col in df.columns:
        print(f"- {col}: {df[col].dtype}")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing Values:")
    missing_values = df.isnull().sum()
    if missing_values.sum() == 0:
        print("No missing values found!")
    else:
        print(missing_values[missing_values > 0])

    print("\nPrice Statistics (Target Variable):")
    print(f"Min Price: ₦{df['price'].min():,}")
    print(f"Max Price: ₦{df['price'].max():,}")
    print(f"Average Price: ₦{df['price'].mean():,.0f}")
    print(f"Median Price: ₦{df['price'].median():,}")

    return df


def one_hot_encoding_categorical_variables(df):
    """One-hot encode nominal categorical variables (location and house_type)"""

    print("One-hot encoding nominal categorical variables:")
    print(f"- location: {df['location'].unique()}")
    print(f"- house_type: {df['house_type'].unique()}")

    return pd.get_dummies(df, columns=['location', 'house_type'], prefix=['location', 'house_type'])


def preprocess_data(df):
    """Clean and preprocess the housing data"""

    print("\n" + "="*50)
    print("DATA PREPROCESSING")
    print("="*50)

    # Make a copy to avoid modifying original data
    df_processed = df.copy()

    # Remove property_id as it's just an identifier
    df_processed = df_processed.drop('property_id', axis=1)

    # One-hot encoding for nominal categories
    df_processed = one_hot_encoding_categorical_variables(df_processed)

    # Label encode binary categorical variables
    label_encoders = {}
    binary_columns = ['has_garage', 'has_pool']

    print("\nLabel encoding binary categorical variables:")
    for col in binary_columns:
        print(f"- {col}: {df_processed[col].unique()}")
        le = LabelEncoder()
        df_processed[col + '_encoded'] = le.fit_transform(df_processed[col])
        label_encoders[col] = le

        # Show encoding mapping
        unique_values = df_processed[col].unique()
        encoded_values = le.transform(unique_values)
        mapping = dict(zip(unique_values, encoded_values))
        print(f"  Encoding: {mapping}")

    # Drop original binary categorical columns
    df_processed = df_processed.drop(binary_columns, axis=1)

    print(f"\nProcessed dataset shape: {df_processed.shape}")
    print("Final columns:", df_processed.columns.tolist())

    return df_processed, label_encoders


def perform_cross_validation(model, X_train_scaled, y_train):
    """Retrieve multiple second opinions on our model's performance"""

    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='r2')
    print('\nList of 5 CV Scores')
    print(cv_scores)
    print(f"\n5-Fold Cross-Validation R² Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")


def make_predictions(model, X_train_scaled, X_test_scaled, y_train, y_test):
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)

    # Calculate metrics to validate model performance
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)

    print("\n" + "="*30)
    print("MODEL PERFORMANCE")
    print("="*30)
    print(f"Training R² Score: {train_r2:.4f}")
    print(f"Testing R² Score: {test_r2:.4f}")
    print(f"Training RMSE: ₦{train_rmse:,.0f}")
    print(f"Testing RMSE: ₦{test_rmse:,.0f}")
    print(f"Training MAE: ₦{train_mae:,.0f}")
    print(f"Testing MAE: ₦{test_mae:,.0f}")

    return y_test_pred


def train_linear_regression(df_processed):
    """Train linear regression model and evaluate performance"""

    print("\n" + "="*50)
    print("LINEAR REGRESSION TRAINING")
    print("="*50)

    # Retrieve all features excluding the price column
    features = df_processed.drop('price', axis=1)

    # Retrieve only the price column because price is the target variable, i.e., what we want to predict
    target_variable = df_processed['price']

    print("Features used for prediction:")
    for i, feature in enumerate(features    .columns):
        print(f"{i+1}. {feature}")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target_variable, test_size=0.2, random_state=42)


    print(f"\nTraining set size: {X_train.shape[0]} samples")
    print(f"Testing set size: {X_test.shape[0]} samples")

    # This line creates the scaler to scale numerical features for better performance
    scaler = StandardScaler()

    # This fits the scaler on training data and transforms it
    # X_train_scaled is now a 2D array where each row is a training example and each column is a feature
    X_train_scaled = scaler.fit_transform(X_train)

    # This transforms test data using the same scaling parameters
    X_test_scaled = scaler.transform(X_test)

    # Create and train the linear regression model
    model = LinearRegression()

    # The fit() method is where the actual learning happens - it's how you train your linear regression model
    # It takes your training data (X_train_scaled and y_train) and finds the best (linear) line through it,
    # calculates the optimal coefficients (weights) for each feature, and determines the intercept (where the line crosses the y-axis)
    model.fit(X_train_scaled, y_train)

    # Make predictions
    y_test_pred = make_predictions(model, X_train_scaled, X_test_scaled, y_train, y_test)

    # Cross-validation
    perform_cross_validation(model, X_train_scaled, y_train)

    # Feature importance (coefficients)
    print("\n" + "="*30)
    print("FEATURE IMPORTANCE")
    print("="*30)
    feature_importance = pd.DataFrame({
        'Feature': features.columns,
        'Coefficient': model.coef_,
        'Abs_Coefficient': np.abs(model.coef_)
    }).sort_values('Abs_Coefficient', ascending=False)

    print(feature_importance[['Feature', 'Coefficient']])

    return model, scaler, X_test, y_test, y_test_pred, feature_importance


def predict_new_house(model, scaler, label_encoders, house_features):
    """Predict price for a new house"""

    print("\n" + "="*50)
    print("PREDICTING NEW HOUSE PRICE")
    print("="*50)

    # Create a DataFrame with the new house features
    new_house_df = pd.DataFrame([house_features])

    # One-hot encode location and house_type to match training data structure
    new_house_df = pd.get_dummies(new_house_df, columns=['location', 'house_type'], prefix=['location', 'house_type'])

    # Encode binary categorical variables using the same encoders
    binary_columns = ['has_garage', 'has_pool']
    for col in binary_columns:
        if col in new_house_df.columns:
            try:
                encoded_value = label_encoders[col].transform([new_house_df[col].iloc[0]])[0]
                new_house_df[col + '_encoded'] = encoded_value
                new_house_df = new_house_df.drop(col, axis=1)
            except ValueError as e:
                print(f"Error encoding {col}: {e}")
                print(f"Available values for {col}: {label_encoders[col].classes_}")
                return None

    # Get the feature columns from the training data (need to match exactly)
    expected_columns = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else None

    if expected_columns is None:
        # If we can't get feature names, we need to manually create all possible dummy columns
        # This is a limitation - in practice, you'd want to save the column names from training
        print("Warning: Cannot determine exact feature names from model. Using approximate matching.")

        # Add missing dummy columns with 0 values
        all_locations = ['Lagos-Mainland', 'Lagos-Island', 'Abuja-Central', 'Ibadan', 'Port Harcourt']
        all_house_types = ['Apartment', 'Duplex', 'Bungalow', 'Mansion']

        for location in all_locations:
            col_name = f'location_{location}'
            if col_name not in new_house_df.columns:
                new_house_df[col_name] = 0

        for house_type in all_house_types:
            col_name = f'house_type_{house_type}'
            if col_name not in new_house_df.columns:
                new_house_df[col_name] = 0

        # Ensure we have the basic numerical columns and encoded binary columns
        expected_order = ['area_sqm', 'bedrooms', 'bathrooms', 'age_years', 'location_Abuja-Central',
            'location_Ibadan', 'location_Lagos-Island', 'location_Lagos-Mainland', 'location_Port Harcourt',
            'house_type_Apartment', 'house_type_Bungalow', 'house_type_Duplex', 'house_type_Mansion',
            'has_garage_encoded', 'has_pool_encoded'
        ]

        # Reorder columns to match expected order and fill missing ones with 0
        for col in expected_order:
            if col not in new_house_df.columns:
                new_house_df[col] = 0

        new_house_df = new_house_df[expected_order]
    else:
        # Use the exact feature names from the trained model
        for col in expected_columns:
            if col not in new_house_df.columns:
                new_house_df[col] = 0
        new_house_df = new_house_df[expected_columns]

    # Scale the features
    new_house_scaled = scaler.transform(new_house_df)

    # Make prediction
    predicted_price = model.predict(new_house_scaled)[0]

    print("House Features:")
    for key, value in house_features.items():
        print(f"- {key}: {value}")

    print(f"\nPredicted Price: ₦{predicted_price:,.0f}")

    return predicted_price


def main():
    """Main function to run the complete pipeline"""

    # Load dataset into a dataframe
    housing_df = load_data('../../data/housing_data.csv')

    print("🏠 HOUSING PRICE PREDICTION USING LINEAR REGRESSION")
    print("="*60)

    # Preprocess data
    df_processed, label_encoders = preprocess_data(housing_df)

    # Train model using linear regression
    model, scaler, X_test, y_test, y_test_pred, feature_importance = train_linear_regression(df_processed)

    new_house = {
        'area_sqm': 160,
        'bedrooms': 3,
        'bathrooms': 2,
        'age_years': 10,
        'location': 'Lagos-Island',
        'house_type': 'Duplex',
        'has_garage': 'Yes',
        'has_pool': 'No'
    }

    predict_new_house(model, scaler, label_encoders, new_house)


if __name__ == '__main__':
    main()