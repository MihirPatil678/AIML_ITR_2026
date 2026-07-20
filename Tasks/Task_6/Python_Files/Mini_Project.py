print("*** Student Marks Manager ***")

subject_marks = []

# Collect Marks For 5 Subjects From The User
for i in range(1, 6):
    mark = int(input("Enter Marks For Subjects:"))
    subject_marks.append(mark)

print("\nInitial Marks List:", subject_marks)

# Add A 6th Subject Mark
extra_mark = int(input("\nEnter Marks For The Extra Subject:"))
subject_marks.append(extra_mark)
print("\nAfter Adding Extra Subject:", subject_marks)

# Built-in max() & min() To Find Highest & Lowest Marks
print("\nHighest Marks:", max(subject_marks))
print("Lowest Marks:", min(subject_marks))

# Sort In Descending Order
subject_marks.sort(reverse=True)
print("\nMarks In Descending Order:", subject_marks)

# Average = Total / Number Of Subjects
average = sum(subject_marks) / len(subject_marks)
print("\nAverage Marks:", average)

# len() Gives The Total Count
print("\nTotal Number Of Subjects:", len(subject_marks))