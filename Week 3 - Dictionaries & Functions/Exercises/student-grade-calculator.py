studentScores1 = {
    "Chris Idakwo": 89,
    "Billy White": 90,
    "John Doe": 76,
    "Christiana Billison": "51",
    "Betty Ndubuisi": "92",
    "Catherine Ekwusa": 67,
}

print('')
print('STUDENT SCORES', studentScores1)

# Add a new student score to the dictionary (1st option)
studentScores1["Ayo Towolawi"] = 58
studentScores1['Grace Chukwu'] = 82

print('')
print('STUDENTS 1 SCORES UPDATED', studentScores1)
print('')

# Chris Idakwo scored 80 out of 100
for name, score in studentScores1.items():
    print(f"{name} scored {score} out of 100")

print('')

studentScores2 = [
    { 'name': "Chris Idakwo", 'score': 89 },
    { 'name': "Billy White", 'score': 90 },
    { 'name': "John Doe", 'score': 76 },
    { 'name': "Christiana Bilison", 'score': 51 },
    { 'name': "Betty Ndubuisi", 'score': 92 },
    { 'name': "Catherine Ekwusa", 'score': 67 },
]

# Add a new student score to the dictionary (2nd option)
studentScores2.append({ 'name': "Ayo Towolawi", 'score': 58 })

print('')
print('STUDENTS 2 SCORES UPDATED', studentScores2)
print('')

# Chris Idakwo scored 80 out of 100
for item in studentScores2:
    studentName = item['name']
    studentScore = item['score']

    if studentScore >= 90:
        grade = "A"
    elif studentScore >= 80:
        grade = "B"
    elif studentScore >= 70:
        grade = "C"
    elif studentScore >= 60:
        grade = "D"
    elif studentScore >= 50:
        grade = "E"
    else:
        grade = "F"

    print(f"{studentName} scored {studentScore} out of 100")
    print(f"{studentName}: {grade}")
    print('')

print('')
