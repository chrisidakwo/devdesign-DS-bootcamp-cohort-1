import math
import time

def normalize_score(score, max_score = 100, target_max = 10):
    """Convert scores to a 0-10 scale and round to nearest 0.5"""
    rawNormalized = (score / max_score) * target_max

    # Round to nearest 0.5
    return round(rawNormalized * 2) / 2

student_scores = [87, 92, 65, 100, 74]
normalized_scores = []

exam_years = [2021, 2022, 2023, 2024, 2025]

for score in student_scores:
    start_time = time.time()
    calculation = normalize_score(score)
    end_time = time.time()

    print(f'\nIt took {end_time - start_time} seconds to run')
    
    normalized_scores.append(calculation)

# List comprehension
# normalized_scores = [normalize_score(score) for score in student_scores]

print(f"\nOriginal scores: {student_scores}")

print(f"\nNormalized scores: {normalized_scores}")





