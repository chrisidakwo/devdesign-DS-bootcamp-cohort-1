import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import set_config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from itertools import cycle
import warnings
warnings.filterwarnings('ignore')

set_config(transform_output="pandas")
def main():
    # ================================================================
    # STEP 1: LOAD AND EXPLORE THE DATA
    # ================================================================
    print("STEP 1: Loading and exploring the dataset...")

    # Load the dataset
    df = pd.read_csv('../../data/credit_scoring.csv')

    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst few rows:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nBasic statistics:")
    print(df.describe())


    # ================================================================
    # STEP 2: DATA PREPARATION AND CLEANING
    # ================================================================
    print("\n" + "="*50)
    print("STEP 2: Preparing the data for modeling...")

    # Make a copy of the original data for safety
    df_clean = df.copy()

    # Handle missing values
    # For numerical columns: fill with median (robust to outliers)
    # For categorical columns: fill with mode (most frequent value)
    for column in df_clean.columns:
        if df_clean[column].dtype in ['int64', 'float64']:
            # Numerical column - fill with median
            df_clean[column].fillna(df_clean[column].median(), inplace=True)
            print(f"Filled missing values in {column} with median: {df_clean[column].median():.2f}")
        else:
            # Categorical column - fill with mode
            mode_value = df_clean[column].mode()[0] if not df_clean[column].mode().empty else 'Unknown'
            df_clean[column].fillna(mode_value, inplace=True)
            print(f"Filled missing values in {column} with mode: {mode_value}")

    # Our target variable is 'repayment_status' with 3 classes:
    # - 'On Time': Customer paid the loan on schedule
    # - 'Delayed': Customer was late with payments but eventually paid
    # - 'Defaulted': Customer failed to repay the loan
    target_column = 'repayment_status'

    # Encode categorical variables
    # We'll use Label Encoding for simplicity (beginners can understand this easily)
    label_encoders = {}
    categorical_columns = df_clean.select_dtypes(include=['object']).columns

    for column in categorical_columns:
        if column != target_column:  # Don't encode the target variable yet
            le = LabelEncoder()
            df_clean[column] = le.fit_transform(df_clean[column].astype(str))
            label_encoders[column] = le
            print(f"Encoded categorical column: {column}")

    print(f"\nAfter preprocessing, dataset shape: {df_clean.shape}")


    # ================================================================
    # STEP 3: PREPARE FEATURES AND TARGET
    # ================================================================
    print("\n" + "="*50)
    print("STEP 3: Separating features and target variable...")

    # Separate features (X) and target (y)
    # Remove customer_id as it's just an identifier, not a predictive feature
    X = df_clean.drop(columns=[target_column, 'customer_id'])
    y = df_clean[target_column]

    print(f"Target variable: {target_column}")
    print(f"Classes in target variable: {sorted(y.unique())}")
    print(f"This is a MULTI-CLASS classification problem with 3 classes")

    # Encode target variable
    le_target = LabelEncoder()
    y_encoded = le_target.fit_transform(y.astype(str))
    print(f"\nTarget encoding:")
    for i, class_name in enumerate(le_target.classes_):
        print(f"  {class_name} → {i}")

    print(f"\nFeatures shape: {X.shape}")
    print(f"Target distribution:")
    target_counts = pd.Series(y).value_counts()
    print(target_counts)
    print(f"Percentages:")
    for status, count in target_counts.items():
        percentage = (count / len(y)) * 100
        print(f"  {status}: {percentage:.1f}%")

    # ================================================================
    # STEP 4: SPLIT THE DATA
    # ================================================================
    print("\n" + "="*50)
    print("STEP 4: Splitting data into training and testing sets...")

    # Split data into training (80%) and testing (20%) sets
    # random_state=42 ensures reproducible results
    # stratify=y_encoded ensures balanced representation of all 3 classes in train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Testing set size: {X_test.shape[0]} samples")

    # Scale the features (important for Logistic Regression)
    # Decision Tree and Random Forest don't require scaling, but it doesn't hurt
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Features scaled using StandardScaler")


    # ================================================================
    # STEP 5: TRAIN THE MODELS
    # ================================================================
    print("\n" + "="*50)
    print("STEP 5: Training three different models...")

    # Initialize the models with beginner-friendly parameters
    # Note: For multi-class classification, all these models work naturally
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000, multi_class='ovr'),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
    }

    # Train each model and store results
    trained_models = {}
    predictions = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")

        # Logistic Regression needs scaled data, others work with original data
        if name == 'Logistic Regression':
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
            y_pred_proba = model.predict_proba(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)

        # Store results
        trained_models[name] = model
        predictions[name] = {
            'y_pred': y_pred,
            'y_pred_proba': y_pred_proba
        }

        print(f"{name} training completed!")


    # ================================================================
    # STEP 6: EVALUATE THE MODELS
    # ================================================================
    print("\n" + "="*50)
    print("STEP 6: Evaluating model performance...")

    # Create a results dataframe to store all metrics
    results = []

    for name in models.keys():
        y_pred = predictions[name]['y_pred']
        y_pred_proba = predictions[name]['y_pred_proba']

        # Calculate all evaluation metrics
        # For multi-class: use 'weighted' average which accounts for class imbalance
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        # For multi-class ROC-AUC, we'll calculate macro average
        # (Note: ROC-AUC for multi-class is more complex, we'll use macro averaging)
        try:
            # Binarize the output for multi-class ROC-AUC calculation
            y_test_binarized = label_binarize(y_test, classes=[0, 1, 2])
            n_classes = y_test_binarized.shape[1]

            print('================ Y-TEST-BINARIZED ================')
            print(y_test_binarized)
            print(n_classes)

            # Calculate ROC-AUC for each class and take macro average
            roc_auc_scores = []
            for i in range(n_classes):
                if len(np.unique(y_test_binarized[:, i])) > 1:  # Check if class exists in test set
                    fpr, tpr, _ = roc_curve(y_test_binarized[:, i], y_pred_proba[:, i])
                    roc_auc_scores.append(auc(fpr, tpr))

            roc_auc = np.mean(roc_auc_scores) if roc_auc_scores else 0.0
        except:
            roc_auc = 0.0  # If ROC-AUC calculation fails

        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1_Score': f1,
            'ROC_AUC': roc_auc
        })

        print(f"\n{name} Results:")
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  Precision: {precision:.4f} (weighted avg)")
        print(f"  Recall:    {recall:.4f} (weighted avg)")
        print(f"  F1 Score:  {f1:.4f} (weighted avg)")
        print(f"  ROC-AUC:   {roc_auc:.4f} (macro avg)")

    # Convert results to DataFrame for easy comparison
    results_df = pd.DataFrame(results)
    print("\n" + "="*50)
    print("COMPARISON OF ALL MODELS:")
    print(results_df.round(4))

    # ================================================================
    # STEP 7: CREATE VISUALIZATIONS
    # ================================================================
    print("\n" + "="*50)
    print("STEP 7: Creating visualizations...")

    # Set up the plotting style
    plt.style.use('default')
    fig = plt.figure(figsize=(20, 15))

    # 1. Model Performance Comparison (Bar Chart)
    plt.subplot(2, 3, 1)
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1_Score', 'ROC_AUC']
    x = np.arange(len(metrics))
    width = 0.25

    for i, model in enumerate(results_df['Model']):
        values = [results_df.iloc[i][metric] for metric in metrics]
        plt.bar(x + i*width, values, width, label=model, alpha=0.8)

    plt.xlabel('Metrics')
    plt.ylabel('Score')
    plt.title('Model Performance Comparison')
    plt.xticks(x + width, metrics, rotation=45)
    plt.legend()
    plt.ylim(0, 1)
    plt.grid(True, alpha=0.3)

    # 2-4. Confusion Matrices for each model
    for i, name in enumerate(models.keys()):
        plt.subplot(2, 3, i+2)
        cm = confusion_matrix(y_test, predictions[name]['y_pred'])

        # Create labels for the 3 classes
        class_labels = le_target.classes_  # ['Defaulted', 'Delayed', 'On Time'] etc.

        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=class_labels,
                    yticklabels=class_labels)
        plt.title(f'Confusion Matrix - {name}')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)

    # 5. ROC Curves (for multi-class, we'll show macro-average)
    plt.subplot(2, 3, 5)

    # For multi-class ROC curves, we plot the macro-average
    colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
    for name, color in zip(models.keys(), colors):
        y_pred_proba = predictions[name]['y_pred_proba']

        # Compute ROC curve and ROC area for each class
        fpr = dict()
        tpr = dict()
        roc_auc = dict()

        # Binarize the output
        y_test_binarized = label_binarize(y_test, classes=[0, 1, 2])
        n_classes = y_test_binarized.shape[1]

        for i in range(n_classes):
            if len(np.unique(y_test_binarized[:, i])) > 1:
                fpr[i], tpr[i], _ = roc_curve(y_test_binarized[:, i], y_pred_proba[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])

        # Compute macro-average ROC curve and ROC area
        if len(roc_auc) > 0:
            # First aggregate all false positive rates
            all_fpr = np.unique(np.concatenate([fpr[i] for i in roc_auc.keys()]))

            # Then interpolate all ROC curves at this points
            mean_tpr = np.zeros_like(all_fpr)
            for i in roc_auc.keys():
                mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])

            # Finally average it and compute AUC
            mean_tpr /= len(roc_auc)

            macro_auc = auc(all_fpr, mean_tpr)
            plt.plot(all_fpr, mean_tpr, color=color,
                     label=f'{name} (Macro AUC = {macro_auc:.3f})', linewidth=2)

    plt.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Random Classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves (Macro-Average)')
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3)

    # 6. Feature Importance (for Random Forest)
    plt.subplot(2, 3, 6)
    rf_model = trained_models['Random Forest']
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=True).tail(10)

    plt.barh(feature_importance['feature'], feature_importance['importance'])
    plt.xlabel('Feature Importance')
    plt.title('Top 10 Most Important Features (Random Forest)')
    plt.tight_layout()

    plt.tight_layout()
    plt.show()

    #================================================================
    # STEP 8: MODEL RECOMMENDATION
    # ================================================================
    print("\n" + "="*50)
    print("STEP 8: MODEL RECOMMENDATION")
    print("="*50)

    # Find the best model based on different criteria
    best_accuracy = results_df.loc[results_df['Accuracy'].idxmax()]
    best_precision = results_df.loc[results_df['Precision'].idxmax()]
    best_recall = results_df.loc[results_df['Recall'].idxmax()]
    best_f1 = results_df.loc[results_df['F1_Score'].idxmax()]
    best_roc_auc = results_df.loc[results_df['ROC_AUC'].idxmax()]

    # print("BEST MODELS BY METRIC:")
    # print(f"• Best Accuracy:  {best_accuracy['Model']} ({best_accuracy['Accuracy']:.4f})")
    # print(f"• Best Precision: {best_precision['Model']} ({best_precision['Precision']:.4f})")
    # print(f"• Best Recall:    {best_recall['Model']} ({best_recall['Recall']:.4f})")
    # print(f"• Best F1 Score:  {best_f1['Model']} ({best_f1['F1_Score']:.4f})")
    # print(f"• Best ROC-AUC:   {best_roc_auc['Model']} ({best_roc_auc['ROC_AUC']:.4f})")

    # Calculate overall ranking (simple average of all metrics)
    results_df['Overall_Score'] = results_df[['Accuracy', 'Precision', 'Recall', 'F1_Score', 'ROC_AUC']].mean(axis=1)
    best_overall = results_df.loc[results_df['Overall_Score'].idxmax()]

    print(f"\nOVERALL RECOMMENDATION:")
    print(f"Best Model: {best_overall['Model']}")
    print(f"Overall Score: {best_overall['Overall_Score']:.4f}")

    model_scores = {}

    for _index, row in results_df.iterrows():
        score = (
            0.25 * row['Accuracy'] +
            0.25 * row['Precision'] +
            0.25 * row['Recall'] +
            0.25 * row['F1_Score'] +
            0.25 * row['ROC_AUC']
        )

        model_scores[row['Model']] = score

    # Find the best model
    best_model = max(model_scores, key=model_scores.get)

    print("\nJUSTIFICATION FOR REPAYMENT STATUS PREDICTION:")

    if best_overall['Model'] == 'Logistic Regression':
        print("""
    ✅ RECOMMENDED: Logistic Regression
    REASONS FOR REPAYMENT STATUS PREDICTION:
    • High interpretability - Easy to explain to business stakeholders and customers
    • Provides probability scores for each repayment status class
    • Fast training and prediction - suitable for real-time loan approvals
    • Less prone to overfitting with small datasets
    • Regulatory compliance - Financial institutions prefer interpretable models
    • Can handle multi-class problems well with One-vs-Rest approach
    • Good baseline performance that's easy to understand and maintain
        """)
    elif best_overall['Model'] == 'Random Forest':
        print("""
    ✅ RECOMMENDED: Random Forest
    REASONS FOR REPAYMENT STATUS PREDICTION:
    • Excellent handling of mixed data types (age, income, ratios, etc.)
    • Built-in feature importance - shows which factors matter most for repayment
    • Robust to outliers in financial data (extreme incomes, debt ratios)
    • Good generalization - less likely to overfit than individual decision trees
    • Can capture complex interactions between financial variables
    • Handles multi-class prediction naturally
    • Provides confidence estimates through ensemble voting
        """)
    else:
        print("""
    ✅ RECOMMENDED: Decision Tree
    REASONS FOR REPAYMENT STATUS PREDICTION:
    • Maximum interpretability - Can create simple if-then rules
    • No need for feature scaling (works with raw financial ratios)
    • Handles categorical variables (past_default) naturally
    • Fast predictions - suitable for real-time loan processing
    • Easy to visualize and explain to loan officers and customers
    • Creates clear decision paths: "If income > X and debt_ratio < Y, then likely On Time"
    Note: Monitor for overfitting in production with more complex datasets
        """)

    print("""
    BUSINESS CONSIDERATIONS FOR REPAYMENT STATUS PREDICTION:
    
    🎯 CLASS PRIORITIES:
    • 'On Time' customers: Ideal - approve quickly, offer competitive rates
    • 'Delayed' customers: Manageable risk - approve with monitoring/higher rates  
    • 'Defaulted' customers: High risk - reject or require collateral
    
    📊 METRICS THAT MATTER MOST:
    • Overall Accuracy: How often we correctly predict repayment behavior
    • Precision for 'Defaulted': Of customers we predict will default, how many actually do?
    • Recall for 'On Time': Of customers who pay on time, how many do we correctly identify?
    
    💼 BUSINESS IMPACT:
    • Misclassifying 'On Time' as 'Defaulted': Lost revenue (rejecting good customers)
    • Misclassifying 'Defaulted' as 'On Time': Financial loss (approving bad loans)
    • Correctly identifying 'Delayed': Opportunity for targeted interventions
    
    🔄 OPERATIONAL CONSIDERATIONS:
    • Model should be retrained regularly as economic conditions change
    • Consider seasonal patterns in repayment behavior
    • Monitor for demographic bias in predictions
    • Implement model explainability for loan officer decision support
    """)

    print("\n" + "="*50)
    print("EXERCISE COMPLETED SUCCESSFULLY! 🎉")
    print("You now understand how to compare models for multi-class loan repayment prediction!")
    print("="*50)

    # Save the results for future reference
    results_df.to_csv('model_comparison_results.csv', index=False)
    print("Results saved to 'model_comparison_results.csv'")

    # ================================================================
    # BONUS: DETAILED CLASSIFICATION REPORTS
    # ================================================================
    print("\nBONUS: Detailed Classification Reports")
    print("="*50)

    for name in models.keys():
        print(f"\n{name} - Detailed Report:")
        print(classification_report(y_test, predictions[name]['y_pred']))

if __name__ == '__main__':
    print("=== CREDIT SCORING MODEL SELECTION EXERCISE ===")
    print("🎯 GOAL: Predict loan repayment status (On Time, Delayed, or Defaulted)")
    print("Comparing Logistic Regression, Decision Tree, and Random Forest\n")

    main()