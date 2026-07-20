students_db = {}  # roll (key) -> {"name", "age", "marks"} (Nested Dictionary)
 
 
def add_student():
    roll = input("Enter Roll Number:")
    if roll in students_db:
        print("A Student With This Roll Number Already Exists.")
        return
    name = input("Enter Name:")
    age = input("Enter Age:")
    marks = input("Enter Marks:")
    students_db[roll] = {"name": name, "age": age, "marks": marks}
    print("Student Added Successfully.")
 
 
def update_marks():
    roll = input("Enter Roll Number To Update Marks:")
    if roll in students_db:
        new_marks = input("Enter New Marks:")
        students_db[roll]["marks"] = new_marks
        print("Marks Updated Successfully.")
    else:
        print("Student Not Found.")
 
 
def search_student():
    roll = input("Enter Roll Number To Search:")
    # get() Avoids A KeyError If The Roll Number Doesn't Exist
    student_record = students_db.get(roll)
    if student_record:
        print("Student Found -> Roll Number", roll, ":", student_record)
    else:
        print("Student Not Found.")
 
 
def display_all():
    if not students_db:
        print("No Students In The System Yet.")
        return
    for roll, details in students_db.items():
        print("Roll Number", roll, ":", details)
 
 
def remove_student():
    roll = input("Enter Roll Number To Remove: ")
    removed = students_db.pop(roll, None)  # Default None Avoids KeyError
    if removed:
        print("Removed Student:", removed)
    else:
        print("Student Not Found.")
 
 
def show_menu():
    print("\n*** Student Management System ***")
    print("1. Add New Student")
    print("2. Update Marks Of A Student")
    print("3. Search Student by Roll Number")
    print("4. Display All Students")
    print("5. Remove A Student")
    print("6. Exit")
 
 
while True:
    show_menu()
    choice = input("Enter Your Choice (1-6):")
 
    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_all()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid Choice. Please Enter A Number Between 1 & 6.")