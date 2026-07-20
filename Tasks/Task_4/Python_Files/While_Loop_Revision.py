# Initialize The Total To 0
total = 0

# Take Input From The User For The First Number Before Entering The Loop
number = float(input("Enter A Positive Number:"))

# Keep Looping Until The User Enters A Positive Number
while number > 0:

    # Add The Entered Number To The Total
    total = total + number

    # Ask The User For The Next Number
    number = float(input("Enter A Positive Number:"))

print("\nYou Entered 0 Or A Negative Number.")
print("Total:", total)