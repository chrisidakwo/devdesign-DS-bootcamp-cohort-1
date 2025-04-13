import matplotlib.pyplot as plt
import numpy as np

def normalize_score(score, max_score = 100, target_max = 10):
    """Convert scores to a 0-10 scale and round to nearest 0.5"""
    rawNormalized = (score / max_score) * target_max

    # Round to nearest 0.5
    return round(rawNormalized * 2) / 2

student_scores = [87, 92, 65, 100, 74]
normalized_scores = []

exam_years = [2021, 2022, 2023, 2024, 2025]

for score in student_scores:
    calculation = normalize_score(score)
    normalized_scores.append(calculation)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(exam_years, normalized_scores, marker='o')

# Customize the axes
plt.yticks(np.arange(0, max(normalized_scores) + 0.5, 0.5))
plt.xlabel('Exam Year')
plt.ylabel('Student Score')
plt.grid(True, linestyle='--', alpha=0.7)

# Add title
plt.title('Student Scores by Exam Year')

# Show the plot
plt.show()