name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
marks1 = int(input("Enter Marks For Subject 1: "))
marks2 = int(input("Enter Marks For Subject 2: "))
marks3 = int(input("Enter Marks For Subject 3: "))

# Store Using Tuple Packing
record = name, roll, marks1, marks2, marks3

# Print Complete Record
print("\nComplete Record:", record)

# Unpack & Display
s_name, s_roll, s_m1, s_m2, s_m3 = record
print("\nName:", s_name)
print("Roll No.:", s_roll)
print("Subject 1:", s_m1)
print("Subject 2:", s_m2)
print("Subject 3:", s_m3)

# count() Usage
marks_only = (s_m1, s_m2, s_m3)
check_mark = int(input("\nEnter A Mark To Check Frequency: "))
print("Mark", check_mark, "Appears", marks_only.count(check_mark), "Time.")

# Nested Tuple With Multiple Students
all_students = (("Mihir", "R01", 85, 90, 78),("Kunal", "R02", 92, 88, 95))

print("\nAll Student Records")
for s in all_students:
    print(s)

# Accessing Specific Values
print("\nSecond Student's Name:", all_students[1][0])
print("First Student's Subject 2 Marks:", all_students[0][3])