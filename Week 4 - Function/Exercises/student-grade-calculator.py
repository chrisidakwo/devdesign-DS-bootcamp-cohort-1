# TODO: Include a validation for numbers greater than 100. Convert to a while loop

def mapScoreToGradeLetter(score):
    grade = "F"

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"

    return grade

def scoreConverter():
    score = input("Please enter a score, between 0 and 100: ")

    if score.isnumeric():
        score = float(score)
        gradeLetter = mapScoreToGradeLetter(score)

        print("The student's grade is: ", gradeLetter)
        print("")
    else:
        print('Please enter a number or decimal')

print('')
scoreConverter()
