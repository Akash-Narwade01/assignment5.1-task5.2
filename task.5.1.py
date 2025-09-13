# Create a dictionary of student names and marks
student_marks = {
    "Akash": 85,
    "Kalash": 92,
    "Manoj": 78,
    "Mangesh": 95,
    "jayesh": 88
}

student_name = input("Enter a student's name to check their marks: ")

if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"The marks for {student_name} are: {marks}")
else:
    print(f"Sorry, {student_name} was not found in the records.")