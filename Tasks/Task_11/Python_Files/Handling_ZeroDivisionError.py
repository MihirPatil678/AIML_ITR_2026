try:
    num1 = float(input("Enter The Numerator:"))
    num2 = float(input("Enter the Denominator:"))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division By Zero Is Not Allowed.")
except ValueError:
    print("Error: Invalid Input. Please Enter Numeric Values Only.")