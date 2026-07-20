# Project 4 - Quiz and Examination System

questions = [
    ("Which data type is immutable in Python?", "List", "Dictionary", "Tuple", "Set", "C"),
    ("What does len([1, 2, 3, 4]) return?", "3", "4", "5", "Error", "B"),
    ("Which keyword defines a function?", "func", "define", "def", "function", "C"),
    ("What is 2 ** 3 in Python?", "6", "8", "9", "5", "B"),
    ("Which method adds element to end of list?", "add()", "insert()", "append()", "push()", "C"),
    ("How do you start a comment in Python?", "//", "/*", "#", "<!--", "C"),
    ("What is index of first element in a list?", "1", "0", "-1", "None", "B"),
    ("Which converts a string to integer?", "str()", "float()", "int()", "num()", "C"),
    ("Which data structure has no duplicates?", "List", "Tuple", "Dictionary", "Set", "D"),
    ("What does 'break' do in a loop?", "Skip iteration", "Exit loop", "Restart loop", "Pause", "B"),
]

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

# Get student details
print("*** PYTHON QUIZ SYSTEM ***")
name = input("Enter Your Name: ")
roll = input("Enter Roll No: ")

score = 0
wrong_answers = []

# Loop Through All Questions
for i in range(len(questions)):
    q = questions[i]

    print(f"\nQ{i+1}: {q[0]}")
    print(f"  A. {q[1]}")
    print(f"  B. {q[2]}")
    print(f"  C. {q[3]}")
    print(f"  D. {q[4]}")

    answer = input("Your Answer (A/B/C/D):").upper()

    if answer == q[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct Answer Is:", q[5])
        wrong_answers.append(q)

# Calculate Result
total = len(questions)
percentage = (score / total) * 100
grade = calculate_grade(percentage)
result = "PASS" if percentage >= 50 else "FAIL"

# Show Result Report
print("\n*** RESULT REPORT ***")
print(f"Name: {name}")
print(f"Roll No: {roll}")
print(f"Score: {score} / {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")

# Show Wrong Answers Review
if len(wrong_answers) > 0:
    print("\n*** Wrong Answers Review ***")
    for q in wrong_answers:
        print("Q:", q[0])
        print("Correct Answer:", q[5])