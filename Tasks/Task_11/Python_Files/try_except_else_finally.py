try:
    num1 = float(input("Enter The Numerator:"))
    num2 = float(input("Enter The Denominator:"))
    result = num1 / num2
except ValueError:
    # Handles Non-Numeric Input
    print("Error: Please Enter Valid Numeric Values.")
except ZeroDivisionError:
    # Handles Division By Zero
    print("Error: Division By Zero Is Not Allowed.")
else:
    # Runs Only When The try Block Succeeds Without Any Exception
    print("Result:", result)
    print("Division Performed Successfully!")
finally:
    # Always Runs - Good Place To Thank The User Or Clean Up Resources
    print("Thank You For Using This Program!")