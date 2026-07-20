class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks
 
    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
 
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:",self.calculate_grade())
 
s1 = Student("Kunal",75)
s1.display()
s2 = Student("Shubham",95)
s2.display()
s3 = Student("Mihir",40)
s3.display()
