try:
    num1 = float(input("Enter The Numerator:"))
    num2 = float(input("Enter The Denominator:"))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please Enter Numbers Only.")
except ZeroDivisionError:
    print("Error: Division By Zero Is Not Allowed.")
finally:
    # The finally Block Always Executes Regardless Of Whether An Exception Occurred Or Not.
    print("Program Execution Completed.")