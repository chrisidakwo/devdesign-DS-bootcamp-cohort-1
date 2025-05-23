# Week 6, Lesson 1: Introduction to Machine Learning & Data Preparation

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand the differences between AI, ML, and Deep Learning
2. Learn about datasets, features, and target variables
3. Master data preparation techniques for ML models
4. Gain hands-on experience with real-world datasets
5. Build a foundation for more advanced ML concepts

## 1. Introduction to Machine Learning

### What is Machine Learning?

Machine learning is a way for computers to learn from examples rather than being explicitly programmed.

**The Child Learning Analogy**:
Think about how a child learns to recognize animals. You don't give the child specific rules like "if it has four legs, fur, and barks, it's a dog." Instead, you show the child many examples of dogs, cats, and other animals, and eventually, they learn to recognize them.
Machine learning works similarly - we show the computer many examples, and it learns patterns from these examples.

### The Machine Learning Spectrum/Subsets

**AI vs. ML vs. Deep Learning**:
- **Artificial Intelligence (AI)**: The broad goal of creating machines that can perform tasks requiring human intelligence
- **Machine Learning (ML)**: A subset of AI that focuses on learning from data
- **Deep Learning**: A specialized subset of ML using neural networks with multiple layers


**The Vehicle Analogy**:
- AI is like transportation (the broad concept of moving from A to B)
- ML is like vehicles (a specific approach to transportation)
- Deep Learning is like self-driving cars (a specialized type of vehicle)

### How Machine Learning Differs from Traditional Programming

**Traditional Programming**:
```
INPUT (Data) + PROGRAM (Rules) = OUTPUT (Answers)
```

**Machine Learning**:
```
30,3 = 10
INPUT (Data) + OUTPUT (Answers) = PROGRAM (Rules)
```

**The Cooking Analogy**:
- Traditional Programming: You give detailed cooking instructions (program) and ingredients (data) to get a meal (output)
- Machine Learning: You give examples of ingredients (data) and final meals (outputs), and the computer learns the cooking instructions (program)

## 2. Key Machine Learning Concepts

### Types of Machine Learning

1. **Supervised Learning**:
    - Training with labeled examples
    - Like learning with a teacher who provides correct answers
    - Examples: Predicting house prices, classifying emails as spam

2. **Unsupervised Learning**:
    - Finding patterns in unlabeled data
    - Like exploring a new city without a map
    - Examples: Customer segmentation, anomaly detection

3. **Reinforcement Learning**:
    - Learning through trial and error with rewards/penalties
    - Like training a dog with treats and scolding
    - Examples: Game playing, robot navigation


**The ML Workflow (Supervised Learning)**
Data -> Features -> Model -> Predictions -> Evaluation -> Iteration


### Key Elements of a Machine Learning Problem

1. **Datasets**:
    - Collections of examples the model learns from
    - Divided into training, validation, and test sets

   **The School Analogy**:
    - Training set: The material you study during the semester
    - Validation set: Practice exams to check your understanding
    - Test set: The final exam that tests what you've learned

2. **Features**:
    - The input variables or attributes
    - The information we use to make predictions

   **The Doctor Analogy**:
    - Features are like symptoms and test results a doctor examines
    - More informative features lead to better diagnoses

3. **Target Variable**:
    - What we're trying to predict
    - Also called the label, outcome, or dependent variable

   **The Map Analogy**:
    - Features are your current location and route
    - Target is your destination

## 3. Data Preparation for Machine Learning

### Why Data Preparation is Important

- cleaning, transforming, organizing

**The Cooking Preparation Analogy**:
Before cooking a meal, you wash, peel, and chop ingredients. Similarly, before applying machine learning, you need to clean and prepare your data. No matter how good your cooking skills (algorithm) are, if your ingredients (data) are poor quality, your meal (model) will be disappointing.

### Common Data Preparation Steps

1. **Handling Missing Values**:
    - Detection: Check for nulls and NaNs
    - Strategies: Remove, impute (mean, median, mode), or predict

   ```python
   # Check for missing values
   print(data.isnull().sum())
   
   # Fill missing values with mean
   data['age_years'].fillna(data['age_years'].mean(), inplace=True)
   ```

2. **Scaling Numerical Features**:
    - Standardization: (x - mean) / std_dev
    - Normalization: (x - min) / (max - min)

   ```python
   from sklearn.preprocessing import StandardScaler
   
   # Select numerical features
   numerical_features = ['area_sqm', 'bedrooms', 'age_years']
   
   # Create a scaler
   scaler = StandardScaler()
   
   # Fit and transform the data
   data[numerical_features] = scaler.fit_transform(data[numerical_features])
   ```

3. **Encoding Categorical Variables**:
    - One-hot encoding: Create binary columns for each category
    - Label encoding: Convert categories to numbers

   ```python
   # One-hot encoding
   data_encoded = pd.get_dummies(data, columns=['location', 'house_type'])
   ```

4. **Feature Selection**:
    - Removing irrelevant or redundant features
    - Focusing on the most informative variables

   ```python
   # Calculate correlations with the target
   correlations = data.corr()['price'].sort_values(ascending=False)
   print(correlations)
   ```

## 4. Building Your First Simple ML Model

### Preparing Data for a Basic Model

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Select features and target
X = data_encoded.drop('price', axis=1)  # All columns except price
y = data_encoded['price']               # Just the price column

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
```

### Training a Simple Linear Regression Model

```python
# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
```

### Visualizing Model Performance

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted House Prices')
plt.show()
```

## 5. Practical Code Examples

### Loading and Exploring a Dataset

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a dataset
housing_data = pd.read_csv('housing_data.csv')

# Explore the data
print(housing_data.head())
print(housing_data.info())
print(housing_data.describe())

# Visualize some relationships
plt.figure(figsize=(10, 6))
sns.scatterplot(x='area_sqm', y='price', data=housing_data)
plt.title('House Price vs. Area')
plt.xlabel('Area (square meters)')
plt.ylabel('Price (Naira)')
plt.show()
```

### Making Predictions with a Trained Model

```python
# Predict price for a new property
# First, set up the features for the new property
new_property = {
    'area_sqm': 150,
    'bedrooms': 3,
    'bathrooms': 2,
    'age_years': 10,
    'location': 'Lagos-Mainland',
    'house_type': 'Apartment',
    'has_garage': 'Yes',
    'has_pool': 'No'
}

# Convert to DataFrame and preprocess
new_property_df = pd.DataFrame([new_property])

# Apply the same preprocessing (one-hot encoding, scaling, etc.)
# ... (preprocessing code here)

# Make a prediction
predicted_price = model.predict(new_property_processed)[0]
print(f"Predicted price for the new property: ₦{predicted_price:,.2f}")
```

## Hands-on Exercise 1: Understanding Machine Learning Concepts

**Real-world Context**:
As a data scientist at a Nigerian real estate company, your first task is to explain machine learning concepts to stakeholders who have limited technical knowledge. You need to help them understand how ML can improve their business decisions regarding property pricing.

**Tasks**:
1. Identify and explain 3 potential use cases for machine learning in the real estate industry
2. For each use case, specify:
    - What would be the features (inputs)
    - What would be the target (output)
    - What type of ML problem this is (classification, regression, etc.)
3. Create a simple diagram showing the machine learning workflow for one of these use cases

**Why This Matters**:
Data scientists regularly need to explain complex concepts to non-technical stakeholders. The ability to translate technical concepts into business language is crucial for getting buy-in on data science projects. Before building any models, you'll often need to help business teams understand what machine learning can and cannot do, setting realistic expectations for projects.

## Hands-on Exercise 2: Data Preparation Challenge

**Real-world Context**:
You're working as a data scientist for a Nigerian bank looking to predict which customers are likely to default on loans. You've been given a dataset with customer information, but it contains several issues that need to be addressed before building a model.

**Tasks**:
1. Load the provided `loan_data.csv` file
2. Identify and handle missing values appropriately
3. Scale numerical features like income, loan amount, and credit score
4. Encode categorical variables like occupation and education level
5. Select the top 5 features most correlated with loan default
6. Prepare the data for a classification model by creating proper X (features) and y (target) datasets

**Why This Matters**:
In real-world data science roles, particularly in finance, you'll rarely receive clean, model-ready datasets. Data preparation often consumes 60-80% of a data scientist's time. Financial institutions rely on well-prepared data to make accurate lending decisions, and even small improvements in default prediction can save millions of naira. This exercise mirrors the critical data preparation stage that precedes any machine learning model implementation in industry.

## Take-Home Exercise: Full Data Science Pipeline

**Real-world Context**:
You've been hired as a data scientist by a Nigerian telecom company to help predict customer churn (customers leaving for competitors). This is your first major project, and you need to demonstrate your ability to handle the entire data science pipeline from data preparation to model evaluation.

**Tasks**:
1. Download the provided `telecom_churn.csv` dataset
2. Perform exploratory data analysis:
    - Check for missing values and outliers
    - Analyze distributions of key variables
    - Identify relationships between features and churn
3. Prepare the data for machine learning:
    - Handle missing values and outliers
    - Scale numerical features
    - Encode categorical variables
    - Select relevant features
4. Split the data into training and testing sets
5. Train a simple logistic regression model to predict churn
6. Evaluate the model's performance using accuracy, precision, recall, and F1-score
7. Write a brief report (1-2 pages) summarizing your findings and recommendations for the company

**Submission Requirement**:
- Submit your Python script or Jupyter notebook with well-documented code
- Include visualizations that support your analysis
- Provide your written report with business recommendations
- Be prepared to present your approach in the next class

## Key Takeaways

- Machine learning is about learning patterns from data, not explicit programming
- AI, ML, and Deep Learning form a hierarchy of approaches
- Features are the inputs, and the target is what we're predicting
- Data preparation is crucial for model success
- The basic ML workflow: prepare data, split into train/test, train model, evaluate

## Additional Resources

1. [Python Machine Learning (Book) by Sebastian Raschka](https://www.packtpub.com/product/python-machine-learning-third-edition/9781789955750)
2. [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)
3. [DataCamp: Introduction to Machine Learning with Python](https://www.datacamp.com/courses/introduction-to-machine-learning-with-python)
4. [Towards Data Science: Data Preparation for Machine Learning](https://towardsdatascience.com/data-preparation-for-machine-learning-cleansing-preprocessing-and-feature-engineering-bc10673a9e7c)
5. [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)