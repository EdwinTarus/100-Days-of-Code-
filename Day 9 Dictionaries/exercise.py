students_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Draco" : 74,
    "Hermione" : 99,
    "Neville" : 62,

}
student_grade = {}
for student in students_scores:
    if students_scores[student] <= 70:
        student_grade[student] = "fail"
        
    elif students_scores[student] <= 80:
        student_grade[student] = "Acceptable"
    
    elif students_scores[student] <= 90:
        student_grade[student] = "exceeds expectations"
    
    else:
        student_grade[student] = "Outstanding"
print(student_grade)