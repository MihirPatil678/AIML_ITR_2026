# Project 1 - Student Management System

students = {}  # Stores All Student Data

def calculate_grade(percentage):
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"

def add_student():
    name = input("Enter Name:")
    roll = int(input("Enter Roll No:"))

    if roll in students:
        print("Roll Number Already Exists!")
        return

    marks = []
    for i in range(1, 6):
        m = float(input(f"Marks Of Subject {i}:"))
        marks.append(m)

    percentage = sum(marks) / 5
    grade = calculate_grade(percentage)

    students[roll] = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "percentage": round(percentage, 2),
        "grade": grade
    }

    print("Student Added!")
    print(f"Name: {name} | Roll: {roll} | Percentage: {percentage:.2f}% | Grade: {grade}")

def view_all():
    if len(students) == 0:
        print("No Students Found.")
        return

    for roll in students:
        s = students[roll]
        print(f"Name: {s['name']} | Roll: {s['roll']} | Percentage: {s['percentage']}% | Grade: {s['grade']}")

def search_student():
    roll = int(input("Enter Roll No To Search:"))

    if roll not in students:
        print("Student Not Found.")
        return

    s = students[roll]
    print("Name:", s['name'])
    print("Roll:", s['roll'])
    print("Marks:", s['marks'])
    print("Percentage:", s['percentage'], "%")
    print("Grade:", s['grade'])

def update_student():
    roll = int(input("Enter Roll No To Update:"))

    if roll not in students:
        print("Student Not Found.")
        return

    name = input("Enter New Name (Press Enter To Skip):")
    if name != "":
        students[roll]["name"] = name

    choice = input("Update Marks? (y/n): ")
    if choice == "y":
        marks = []
        for i in range(1, 6):
            m = float(input(f"Marks of Subject {i}:"))
            marks.append(m)
        percentage = sum(marks) / 5
        students[roll]["marks"] = marks
        students[roll]["percentage"] = round(percentage, 2)
        students[roll]["grade"] = calculate_grade(percentage)

    print("Record Updated!")

def delete_student():
    roll = int(input("Enter Roll No To Delete:"))

    if roll not in students:
        print("Student Not Found.")
        return

    confirm = input(f"Delete {students[roll]['name']}? (y/n):")
    if confirm == "y":
        del students[roll]
        print("Student Deleted.")
    else:
        print("Cancelled.")

# Main Menu Loop
while True:
    print("\n*** STUDENT MANAGEMENT SYSTEM ***")
    print("1. Add Student")
    print("2. View All")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice.")