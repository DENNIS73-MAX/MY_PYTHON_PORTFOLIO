# MY PORTFOLIO PROJECT: Student Grade System
# Author: [FREMPONG_ODURO_DENNIS] | ANYINAM
#, Ghana
print("=== STUDENT GRADE SYSTEM ===")

# Get student info
name = input("Enter student name: ")
math = int(input("Enter Math score: "))
english = int(input("Enter English score: "))
science = int(input("Enter Science score: "))

# Calculate
total = math + english + science
average = total / 3

# Find grade
if average >= 80:
    grade = "A - Excellent!"
elif average >= 70:
    grade = "B - Very Good"
elif average >= 60:
    grade = "C - Good"
elif average >= 50:
    grade = "D - Pass"
else:
    grade = "F - Fail"

# Show result
print("\n--- RESULT ---")
print(f"Name: {name}")
print(f"Total: {total}/300")
print(f"Average: {average:.1f}%")
print(f"Grade: {grade}")

if average >= 50:
    print(f"Congrats {name}! You passed!")
else:
    print(f"Sorry {name}, try harder next time.")