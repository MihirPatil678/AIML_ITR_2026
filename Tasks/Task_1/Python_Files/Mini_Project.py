# Taking Input From The User For Student Profile
name = input("Enter Your Name:")           
age = int(input("Enter Your Age:"))  
city = input("Enter Your City:") 

# Taking Marks For 3 Subjects
marks_subject1 = float(input("Enter Marks For Subject 1:"))
marks_subject2 = float(input("Enter Marks For Subject 2:"))
marks_subject3 = float(input("Enter Marks For Subject 3:"))

# Calculating Total Marks
total_marks = marks_subject1 + marks_subject2 + marks_subject3

# Calculating Percentage
percentage = (total_marks / 300) * 100  # Assuming Each Subject Is Of 100 Marks

# Printing The Student Profile
print("\n***** STUDENT PROFILE *****")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Marks:")
print("  Subject 1:", marks_subject1)
print("  Subject 2:", marks_subject2)
print("  Subject 3:", marks_subject3)
print("Total Marks:", total_marks)
print("Percentage:", f"{percentage:.2f}%")