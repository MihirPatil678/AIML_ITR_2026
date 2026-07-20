grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

print("Count Of 'A':", grades.count('A'))
print("Count Of 'B':", grades.count('B'))

user_grade = input("Enter A Grade To Count:")
print("Count Of", user_grade, ":", grades.count(user_grade))