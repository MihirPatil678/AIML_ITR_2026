class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []  # Start With An Empty List of marks
 
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                # Basic Check For A Mark Range
                print("Invalid Mark! Marks Must Be Between 0 & 100.")
                return
            self.marks_list.append(mark)
            print(f"Mark {mark} Added Successfully.")
        except ValueError:
            print("Invalid Mark! Please Enter A Numeric Value.")
 
    def get_average(self):
        if not self.marks_list:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
 
    def display_info(self):
        print("\n*** Student Information ***")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks_list}")
        print(f"Average: {self.get_average():.2f}")
 
 
def main():
    # Create One Student Object
    name = input("Enter Student Name:")
    roll_no = input("Enter Roll Number:")
    student = Student(name, roll_no)
 
    # Add Marks Using User Input, Demonstrating Exception Handling
    num_marks = 3
    for i in range(num_marks):
        mark_input = input(f"Enter Mark #{i + 1}:")
        student.add_mark(mark_input)
 
    # Demonstrate All Methods
    print(f"\nAverage Marks: {student.get_average():.2f}")
    student.display_info()
 
 
if __name__ == "__main__":
    main()
 