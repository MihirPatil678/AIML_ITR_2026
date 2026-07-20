# Take Marks As Input From User & Convert It To Integer
marks = int(input("Please Enter Your Marks:"))

# Assigning Grade Based On Marks
if marks >= 90:
    print("Grade A - Excellent") # If Marks Are 90 Or Above -> Grade A
elif marks >= 75:
    print("Grade B - Good")      # If Marks Are Between 75 & 89 -> Grade B
elif marks >= 60:
    print("Grade C - Average")   # If Marks Are Between 60 & 74 -> Grade C
elif marks >= 40:
    print("Grade D - Pass")      # If Marks Are Between 40 & 59 -> Grade D
else:
    print("Fail")                # Or Else Marks Are Below 40 -> Fail