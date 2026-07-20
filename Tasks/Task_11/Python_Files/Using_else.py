try:
    num1 = float(input("Enter The Numerator:"))
    num2 = float(input("Enter The Denominator:"))
    result = num1 / num2
except ValueError:
    print("Error: Please Enter Valid Numeric Values.")
except ZeroDivisionError:
    print("Error: Division By Zero Is Not Allowed.")
else:
    # The else block runs ONLY when no exception was raised in the try block
    print("Result:", result)
    print("Division Performed Successfully!")