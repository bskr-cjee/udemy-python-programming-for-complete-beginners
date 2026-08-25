student_score = int(input("Enter the student's score: "))

# Write your if block here:
if student_score < 60:
    grade = "F"
elif student_score > 60 and student_score <= 69:
    grade = "D"
elif student_score > 70 and student_score <= 79:
    grade = "C"
elif student_score > 80 and student_score <= 89:
    grade = "B"
elif student_score > 90:
    grade = "A"


print('The grade is:', grade)
