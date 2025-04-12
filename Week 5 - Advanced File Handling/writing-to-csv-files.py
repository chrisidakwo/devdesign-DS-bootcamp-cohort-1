import csv

# Sample data
data = [
    ['Name', 'Score', 'Grade'],
    ['Alice', 92, 'A'],
    ['Bob', 85, 'B'],
    ['Charlie', 78, 'C']
]

# Using csv.writer
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once

students = [
    {'Name': 'David', 'Score': 95, 'Grade': 'A'},
    {'Name': 'Eve', 'Score': 88, 'Grade': 'B'},
    {'Name': 'Alice', 'Score': 92, 'Grade': 'A'},
    {'Name': 'Bob', 'Score': 85, 'Grade': 'B'},
    {'Name': 'Charlie', 'Score': 78, 'Grade': 'C'},
]

with open('output_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Score', 'Grade']

    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(students)  # Write all rows at once