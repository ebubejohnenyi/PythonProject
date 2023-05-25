userFirstGrades = int(input("Enter the course grade: "))
userSecondGrades = int(input("Enter the course grade: "))
userThirdGrades = int(input("Enter the course grade: "))

for grades in (1,3):
    mathematics = 0
    english = 0
    commerce = 0
    if userFirstGrades > grades:
        mathematics