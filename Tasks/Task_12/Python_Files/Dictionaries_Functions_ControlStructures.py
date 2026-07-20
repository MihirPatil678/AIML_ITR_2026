def student_database():
    records = {}  # dictionary: roll_no -> {name, age, city}

    while True:
        print("\n***** Student Database Menu *****")
        print("1. Add Student")
        print("2. Search Student By Roll Number")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter Your Choice (1-4):"))
        except ValueError:
            print("Invalid Input! Please Enter A Number Between 1 & 4.")
            continue

        if choice == 1:
            try:
                roll_no = int(input("Enter Roll Number:"))
                name = input("Enter Name:")
                age = int(input("Enter Age:"))
                city = input("Enter City:")

                # update() Is Used To Add/Overwrite The Record For This roll_no
                records.update({roll_no: {"name": name, "age": age, "city": city}})
                print(f"Student With Roll Number {roll_no} Added Successfully.")
            except ValueError:
                print("Invalid Age Entered! Student Not Added.")

        elif choice == 2:
            roll_no = int(input("Enter Roll Number To Search:"))
            # get() Returns None If The Key Doesn't Exist, Avoiding A KeyError
            student = records.get(roll_no)
            if student:
                print(f"Roll No: {roll_no} -> {student}")
            else:
                print("No Student Found With That Roll Number.")

        elif choice == 3:
            if not records:
                print("No Student Records Found.")
            else:
                print("\nAll Student Records:")
                for roll_no, info in records.items():
                    print(f"Roll No: {roll_no} -> {info}")

        elif choice == 4:
            print("Exiting Student Database. Goodbye!")
            break

        else:
            print("Invalid Choice! Please Select An Option Between 1 & 4.")


if __name__ == "__main__":
    student_database()