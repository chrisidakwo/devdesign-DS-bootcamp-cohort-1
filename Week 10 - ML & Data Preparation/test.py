# Understanding the accuracy calculation
from sklearn.metrics import accuracy_score, precision_score, recall_score

def xys():
    pass

if __name__ == '__main__':
    # Example with imbalanced data
    y_true = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 90% negative, 10% positive
    y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Model always predicts negative

    accuracy = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {accuracy:.2f}")  # Will show 90% accuracy

    print("But the model never detects positive cases!")
    print('')

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
