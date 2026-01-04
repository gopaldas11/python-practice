student_scores = {
     "Gopal": 81,
     "Nayon": 88,
     "Sojib": 89,
     "Monjoy": 82,
     "Pranto": 65,
}
student_greads = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_greads[student] = "Outstanding"
    elif  score > 80:
        student_greads[student] = "Exceed Expectation"
    elif  score > 70:
        student_greads[student] = "Acceptable"
    else:
        student_greads[student] = "fail"
print(student_greads)