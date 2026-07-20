students = {
    "s1": {"name": "Rahul", "age": 20, "marks": 88},
    "s2": {"name": "Sneha", "age": 21, "marks": 95}
}
 
# Details Of The First Student (Entire Inner Dictionary)
print("Student 1 Details:", students["s1"])
 
# Marks Of The Second Student (Specific Value From Inner Dictionary)
print("Student 2 Marks:", students["s2"]["marks"])
 
# Adding A New Subject For The First Student
students["s1"]["math"] = 90
print("Student 1 After Adding Math Marks:", students["s1"])