# Week 6, Lesson 2: Building and Improving Machine Learning Models

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand key machine learning models for classification and regression
2. Learn how to train and test ML models properly
3. Implement techniques to evaluate and compare model performance
4. Apply cross-validation for better model generalization
5. Improve model performance through hyperparameter tuning
6. Practice building end-to-end ML solutions for real-world problems

## 1. Introduction to Machine Learning Models

### Choosing the Right Model for Your Problem

**The Tool Selection Analogy**:
Just as a craftsperson chooses specific tools for different jobs (a hammer for nails, a screwdriver for screws), data scientists must select appropriate models for different problems. Using the wrong model is like trying to hammer in a screw - you might make progress, but the results won't be ideal.

Why model selection matters: efficiency, quality, right/better use of resources, reliability (consistent and dependable)

#### Model Selection Framework:
1. **Task Type**: Classification (which category?) vs. Regression (how much?)
2. **Data Characteristics**: Size (how much?), dimensionality (how many? - low dimensions for few features, high dimensions for many features), linearity (is the relationship straightforward?), etc.
3. **Model Complexity**: Simpler models are easier to interpret but might not capture complex patterns
4. **Performance Requirements**: Speed vs. accuracy tradeoffs

### Common Classification Models

#### 1. Logistic Regression

**The Threshold Decision Analogy**:
Think of logistic regression like deciding whether to carry an umbrella. You look at various factors (dark clouds, weather forecast, time of year) and mentally calculate a probability of rain. If that probability exceeds your threshold (say, 50%), you take the umbrella.

dark clouds - 40% weight (high probability)
weather forecast - 30% weight
season - 20% weight
other considerations - 10% weight

weight is learned from historical data

How Logistic Regression Works:
1. Input features
2. Weights
3. Probability Calculation
4. Decision Threshold

**Key Characteristics**:
- Used for binary or multi-class classification
- Outputs probabilities between 0 and 1
- Easy to interpret
- Works well for linearly separable data
- Fast to train and deploy

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
import pandas as pd
loan_data = pd.read_csv('loan_data.csv')

# Prepare data (assume preprocessing has been done)
X = loan_data.drop(['customer_id', 'default'], axis=1)  # Features
y = loan_data['default']               # Target

# Split data
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
```

#### 2. Decision Trees

**The Questionnaire Analogy**:
A decision tree is like a questionnaire or flowchart. At each step, there's a yes/no question that narrows down the possibilities. "Is income > ₦100,000?" If yes, go down one path; if no, go down another. Eventually, you reach a conclusion about the classification.

Level 1 - monthly income >= N100,000 (Yes ->  2A, No -> 2B)
Level 2A - Credit score > 700 (Yes -> 3A, No -> 3B)
Level 2B - Debt-to-income ratio < 30% 
Level 3A - employment >= 5 years
Level 4A - Existing Loans

**Key Characteristics**:
- Intuitive and easy to visualize
- Can model non-linear relationships
- Prone to overfitting
- No need for feature scaling
- Can handle numerical and categorical data

```python
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree

# Create and train the model
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)
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
plt.show()
```

### Common Regression Models

#### 1. Linear Regression (Brief Review)

**The Line of Best Fit Analogy**:
Linear regression is like drawing a straight line through scattered points on a graph to show the general trend. If you're trying to relate study hours to exam scores, the line might show that each additional hour of study is associated with an extra 5 points on the exam.

#TODO: Include a note on the difference between logistic regression and linear regression

#### 2. Decision Tree Regression

**The Step Function Analogy**:
While a linear regression gives you a smooth line, a decision tree regression gives you a stair-step pattern. It breaks the data into chunks based on feature values and predicts the average outcome within each chunk.

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Create and train the model
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_train, y_train)

# Make predictions
dt_reg_pred = dt_reg.predict(X_test)

# Evaluate performance
dt_reg_mse = mean_squared_error(y_test, dt_reg_pred)
dt_reg_r2 = r2_score(y_test, dt_reg_pred)
print(f"Decision Tree MSE: {dt_reg_mse:.2f}")
print(f"Decision Tree R²: {dt_reg_r2:.2f}")
```

## 2. Evaluating Machine Learning Models

### Classification Metrics


90 non-spam emails
50 spam emails


Confusion Matrix
                                          PREDICTION
                                   Not Spam    |     Spam
      ACTUAL DATA     Not Spam       85        |       5
                      Spam           10        |       40

1. True Positives (40): Correctly identified spam emails
2. False Positives (5): Emails marked wrongly as spam
3. True Negatives (85): Correctly identified emails
4. False Negatives (10): Spam emails that got through

**The Medical Test Analogy**:
Understanding classification metrics is like evaluating a medical diagnostic test. We need to consider both the test's ability to correctly identify sick patients (True Positives) and its tendency to raise false alarms (False Positives).

#### 1. Accuracy

**Definition**: The proportion of correct predictions among all predictions
**Limitations**: Can be misleading with imbalanced classes (categories)
**When to use**: When you have balanced classes (roughly equal number of spam and non-spam)
**When not to use**: If 95% of emails are normal and 5% are spam, a lazy model that always says "no spam" would get 95% accuracy but never catch a spam!

```python
from sklearn.metrics import accuracy_score

# Formula: Sum of Correct Predictions / Sum of Total Predictions

# (85 + 40) /  (85 + 5 + 10 + 40)
# (125 / 140)
# 0.89 -> 89%

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

#### 2. Precision and Recall

**Precision**: Out of all positive predictions, how many were actually positive?
**Recall**: Out of all actual positives, how many did we predict correctly?

**The Fishing Analogy**:
- Precision is like asking "Of all the fish I caught, what percentage were the specific type I was trying to catch?"
- Recall is like asking "Of all the specific fish in the lake, what percentage did I manage to catch?"

**Precision (Quality of Positive Prediction)**:
- **What does it mean:** When the model says "spam", how often is it actually spam?
- **Importance:** High precision means fewer normal emails are marked as spam 

**Recall (Sensitivity)**:
- **What does it mean:** Out of all actual spam, how many did we catch?
- **Importance**: High recall means that less spam reaches your inbox

TODO: Investigate issue with precision_score() and recall_score() in logistic-regression.py

```python
from sklearn.metrics import precision_score, recall_score

# Precision Formula: True Positives / (True Positives + False Positives)
# 40 / (40 + 5)
# 0.889 -> 89%

# Recall Formula: True Positives / (True Positives + False Negatives)
# 40 / (40 + 10)
# 0.8 -> 80%


precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
```

#### 3. F1 Score

**Definition**: The harmonic mean of precision and recall
**Usefulness**: Balances precision and recall, especially important with imbalanced classes

```python
from sklearn.metrics import f1_score

# Formula: 2 x (Precision x Recall) / (Precision + Recall)

f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.2f}")
```

#### 4. Confusion Matrix

**Definition**: A table showing the counts of true positives, false positives, true negatives, and false negatives
**Usefulness**: Provides a detailed breakdown of model errors

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Default', 'Default'],
            yticklabels=['No Default', 'Default'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
```

### Regression Metrics

#### 1. Mean Squared Error (MSE)

**Definition**: The average of squared differences between predicted and actual values
**Usefulness**: Heavily penalizes large errors

```python
from sklearn.metrics import mean_squared_error

# Formula: Average of (Predicted - Actual)^2

mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.2f}")
```

#### 2. Root Mean Squared Error (RMSE)

**Definition**: The square root of MSE, which brings the error back to the original unit
**Usefulness**: More interpretable than MSE

```python
# Formula: square root of MSE

rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse:.2f}")
```

#### 3. R-squared (R²)

**Definition**: The proportion of variance in the dependent variable explained by the model
**Usefulness**: Provides a relative measure of fit (0 to 1)

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(f"R²: {r2:.2f}")
```

#### 4. Mean Absolute Error (MAE)
TODO: Add a note for this

### Visual Evaluation Methods

#### 1. ROC Curve for Classification

**Definition**: A plot of True Positive Rate vs. False Positive Rate at various threshold settings
**Usefulness**: Shows the tradeoff between sensitivity and specificity

```python
from sklearn.metrics import roc_curve, auc

# Get prediction probabilities
y_scores = model.predict_proba(X_test)[:, 1]  # Probabilities for the positive class

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
```

#### 2. Residual Plots for Regression

**Definition**: A plot of prediction errors (residuals) vs. predicted values
**Usefulness**: Helps identify patterns in errors and model weaknesses

```python
# Calculate residuals
residuals = y_test - y_pred

# Create residual plot
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
```

## 3. Improving Model Performance

### Cross-Validation

**The Practice Test Analogy**:
Cross-validation is like taking multiple practice tests before a final exam, each covering different parts of the material. This gives you a more reliable estimate of how well you understand the entire subject, rather than just one subset.

**Purpose**:
- Provide a more reliable estimate of model performance
- Reduce the impact of how the data is split into training and testing sets
- Help detect model overfitting

```python
from sklearn.model_selection import cross_val_score

# Perform 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean():.2f}")
print(f"Standard deviation of CV scores: {cv_scores.std():.2f}")
```

### Hyperparameter Tuning

**The Recipe Adjustment Analogy**:
Hyperparameter tuning is like adjusting ingredient quantities in a recipe to get the best taste. If a cake is too dry, you might add more butter next time. Similarly, if a model isn't performing well, we adjust its hyperparameters to improve its predictions.

**Key Techniques**:
1. **Grid Search**: Exhaustively search through a predefined set of hyperparameters
2. **Random Search**: Randomly sample from the hyperparameter space
3. **Bayesian Optimization**: Intelligently search based on previous results

```python
from sklearn.model_selection import GridSearchCV

# Define hyperparameter grid for a Decision Tree
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Create a grid search object
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1  # Use all available CPU cores
)

# Fit grid search
grid_search.fit(X_train, y_train)

# Print best parameters and score
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.2f}")

# Create model with best parameters
best_dt_model = grid_search.best_estimator_
best_dt_pred = best_dt_model.predict(X_test)
best_dt_accuracy = accuracy_score(y_test, best_dt_pred)
print(f"Test accuracy with best parameters: {best_dt_accuracy:.2f}")
```

### Ensemble Methods

**The Committee Decision Analogy**:
Ensemble methods are like getting opinions from a committee of experts rather than just one person. By combining multiple viewpoints, you often get better decisions than any single expert would provide.

#### 1. Random Forest

**Description**: Combines multiple decision trees trained on different subsets of data and features

```python
from sklearn.ensemble import RandomForestClassifier

# Create and train the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
rf_pred = rf_model.predict(X_test)

# Evaluate
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")
print(classification_report(y_test, rf_pred))
```

#### 2. Gradient Boosting

**Description**: Builds models sequentially, with each model correcting errors made by previous ones

```python
from sklearn.ensemble import GradientBoostingClassifier

# Create and train the model
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

# Make predictions
gb_pred = gb_model.predict(X_test)

# Evaluate
gb_accuracy = accuracy_score(y_test, gb_pred)
print(f"Gradient Boosting Accuracy: {gb_accuracy:.2f}")
print(classification_report(y_test, gb_pred))
```

### Handling Class Imbalance

**The Rare Disease Analogy**:
Handling class imbalance is like diagnosing a rare disease. If only 1% of patients have the disease, a model could achieve 99% accuracy by simply predicting "no disease" for everyone - but that's not useful! We need strategies to ensure our model can still identify those rare positive cases.

**Key Techniques**:
1. **Resampling**:
    - Oversampling the minority class
    - Undersampling the majority class
    - Synthetic minority oversampling (SMOTE)

2. **Class Weights**:
    - Give more importance to the minority class during training

```python
from imblearn.over_sampling import SMOTE

# Apply SMOTE to balance classes
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Check class distribution after resampling
print("Class distribution before SMOTE:")
print(pd.Series(y_train).value_counts(normalize=True))

print("Class distribution after SMOTE:")
print(pd.Series(y_train_resampled).value_counts(normalize=True))

# Train model on resampled data
model_resampled = LogisticRegression(random_state=42)
model_resampled.fit(X_train_resampled, y_train_resampled)

# Evaluate
pred_resampled = model_resampled.predict(X_test)
print(f"Accuracy with SMOTE: {accuracy_score(y_test, pred_resampled):.2f}")
print(classification_report(y_test, pred_resampled))
```

## Hands-on Exercise 1: Model Selection and Evaluation

**Real-world Context**:
You're working as a data scientist for a Nigerian financial services company tasked with developing a credit scoring model. Your manager wants to know which model type would work best for predicting whether customers will repay their loans on time.

**Tasks**:
1. Load the provided `credit_scoring.csv` dataset
2. Prepare the data for modeling (handle missing values, encode categorical features, etc.)
3. Train three different models on the data:
    - Logistic Regression
    - Decision Tree
    - Random Forest
4. Evaluate each model using:
    - Accuracy
    - Precision and Recall
    - F1 Score
    - ROC-AUC
5. Create visualizations to compare model performance (include confusion matrix)
6. Provide a recommendation for which model to use, justifying your choice

**Why This Matters**:
In real-world data science roles, particularly in finance, choosing the right model type is critical. Different models have different strengths and weaknesses, and the choice can significantly impact business outcomes. Financial institutions rely on accurate credit scoring models to determine lending decisions, and poor model selection can lead to either missed revenue opportunities (rejecting good customers) or financial losses (approving bad customers). This exercise mirrors the model selection process that data scientists go through at the start of many machine learning projects.

## Hands-on Exercise 2: Hyperparameter Tuning Challenge

**Real-world Context**:
You're a data scientist working for a Nigerian e-commerce company that wants to predict which customers are likely to make a purchase based on their browsing behavior. You've already built a basic model, but your team leader has challenged you to improve its performance through hyperparameter tuning.

**Tasks**:
1. Load the provided `ecommerce_purchase.csv` dataset
2. Prepare the data for modeling
3. Split the data into training, validation, and test sets
4. Train a baseline Random Forest model and record its performance
5. Use GridSearchCV to find the optimal hyperparameters for:
    - Number of trees (n_estimators)
    - Maximum depth (max_depth)
    - Minimum samples per split (min_samples_split)
6. Train an optimized model with the best hyperparameters
7. Compare the performance of the baseline and optimized models
8. Calculate the percentage improvement in your chosen metric

**Why This Matters**:
Hyperparameter tuning is a crucial skill for professional data scientists. In competitive industries like e-commerce, even small improvements in model performance can translate to significant business impact. A 1% improvement in conversion prediction could mean millions in additional revenue. This exercise reflects the iterative optimization process that data scientists use to extract maximum value from their models in commercial settings.

## Take-Home Exercise: End-to-End Machine Learning Project

**Real-world Context**:
You've been hired as a data scientist by a Nigerian health insurance company to predict medical costs for different policyholder profiles. The company wants to use these predictions to optimize their premium pricing structure and reduce financial risk.

**Tasks**:
1. Download the provided `health_insurance.csv` dataset, which contains information about policyholders including age, BMI, smoking status, and medical costs
2. Perform exploratory data analysis:
    - Analyze the distribution of medical costs
    - Identify key factors that correlate with higher costs
    - Visualize important relationships in the data
3. Prepare the data for machine learning
4. Train multiple regression models:
    - Linear Regression
    - Decision Tree
    - Random Forest
    - Gradient Boosting
5. Evaluate each model using appropriate metrics (RMSE, MAE, R²)
6. Tune the hyperparameters of the best-performing model
7. Analyze feature importance to identify the main drivers of medical costs
8. Create a final predictive model and use it to estimate costs for different customer profiles
9. Write a brief report (1-2 pages) summarizing your approach, findings, and recommendations for the company

**Submission Requirements**:
- Python script or Jupyter notebook with well-documented code
- Visualizations of data insights and model performance
- Written report with business recommendations
- A section explaining how the company could use this model to improve their pricing strategy

## Key Takeaways

- Different machine learning models serve different purposes
- Proper evaluation metrics depend on the problem type
- Cross-validation gives more reliable performance estimates
- Hyperparameter tuning can significantly improve model performance
- Ensemble methods often outperform individual models
- Class imbalance requires special handling techniques

## Additional Resources

1. [Scikit-learn Documentation - Supervised Learning](https://scikit-learn.org/stable/supervised_learning.html)
2. [Towards Data Science: Model Evaluation in Machine Learning](https://towardsdatascience.com/model-evaluation-in-machine-learning-8e71301aafab)
3. [Machine Learning Mastery: Hyperparameter Tuning](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/)
4. [Analytics Vidhya: Ensemble Methods in Machine Learning](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-for-ensemble-models/)
5. [Imbalanced-learn Documentation](https://imbalanced-learn.org/stable/)