import pandas as pd
import matplotlib.pyplot as plt

# Sammple data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [92, 85, 78, 95, 67],
}

 # Create DataFrame
df = pd.DataFrame(data)

# Calculate statistics
avg_score = df['Score'].mean()
print(f"Average score: {avg_score:.2f}")

# Create a simple bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Score'])
plt.title('Student Scores')
plt.xlabel('Student')
plt.ylabel('Score')
plt.savefig('student_scores.png')
print("Chart saved as student_scores.png")