# Develop a modular Python program for a Student Performance Analysis System using 
# user-defined functions and lambda expressions. The program should accept marks of 
# students, compute the total, average, highest, and lowest marks using user-defined 
# functions, determine the grade, and use lambda expressions to sort students based on 
# their total marks. 


# Student Performance Analysis System

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to find highest mark
def find_highest(marks):
    return max(marks)

# Function to find lowest mark
def find_lowest(marks):
    return min(marks)

# Function to determine grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Main program
students = []

n = int(input("Enter number of students: "))
k = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = []

    for j in range(k):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = calculate_grade(average)

    students.append({
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    })

# Sort students using lambda expression
students.sort(key=lambda x: x["total"], reverse=True)

# Display student performance
print("\n----- STUDENT PERFORMANCE REPORT -----")

for student in students:
    print("\nName:", student["name"])
    print("Total Marks:", student["total"])
    print("Average Marks:", round(student["average"], 2))
    print("Highest Mark:", student["highest"])
    print("Lowest Mark:", student["lowest"])
    print("Grade:", student["grade"])
