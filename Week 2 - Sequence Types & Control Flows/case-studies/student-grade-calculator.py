# A school wants to automate its grading system. 
# Students receive a numerical score between 0 and 100, 
# and the system assigns a letter grade based on the score.

# 90+ -> A
# 80 - 89 -> B
# 70 - 79 -> C
# 60 - 69 -> D
# 50 - 59 -> E
# < 50 -> F

print("")
score = input("Please enter a score, between 0 and 100: ")

if score.isnumeric():
    score = float(score)
    grade = ""

    # TODO: Include a validation for numbers greater than 100

    if score >= 90:
        grade = "A"
    elif score >= 80 and score <= 89:
        grade = "B"
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 69:
        grade = "D"
    elif score >= 50 and score <= 59:
        grade = "E"
    else:
        grade = "F"

    print("The student's grade is: ", grade)
    print("")

    # Alternative Solution
    # if score >= 90:
    #     grade = "A"
    # elif score >= 80:
    #     grade = "B"
    # elif score >= 70:
    #     grade = "C"
    # elif score >= 60:
    #     grade = "D"
    # elif score >= 50:
    #     grade = "E"
    # else:
    #     grade = "F"

    # print("The student's grade is: ", grade)
    # print("")
else:
    print('Please enter a number or decimal')
