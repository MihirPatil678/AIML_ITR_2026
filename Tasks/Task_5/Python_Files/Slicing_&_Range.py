# First 10 Even Numbers: range(start=2, stop=21, step=2)
print("First 10 Even Numbers (2 To 20):")
for num in range(2, 21, 2):
    print(num, end=" ")
 
# Numbers 1 To 30 In Steps Of 3
print("Numbers 1 To 30 In Steps Of 3:")
for num in range(1, 31, 3):
    print(num, end=" ")
 
# String Slicing On "PythonProgramming"
text = "PythonProgramming"
print("\nOriginal string:",text)
print("'Python':", text[:6])        # Index 0–5
print("'Programming':", text[6:])        # Index 6 To End
print("Reversed:", text[::-1])      # step=-1