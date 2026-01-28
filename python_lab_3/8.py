marks = [70, 80, 90, 60, 50]
total = sum(marks)
percentage = total / 5
cgpa = percentage / 10
if cgpa <= 3.4:
 grade = "F"
elif cgpa <= 5.0:
 grade = "C+"
elif cgpa <= 6.0:
 grade = "B"
elif cgpa <= 7.0:
 grade = "B+"
elif cgpa <= 8.0:
 grade = "A"
elif cgpa <= 9.0:
 grade = "A+"
else:
 grade = "O"
print("Percentage:", percentage)
print("CGPA:", cgpa)
print("Grade:", grade)