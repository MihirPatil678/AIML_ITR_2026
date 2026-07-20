try:
    num1 = float(input("Enter The Numerator:"))
    num2 = float(input("Enter The Denominator:"))
    result = num1 / num2             # May Raise ZeroDivisionError
 
    text = input("Enter A String To Convert To Integer:")
    converted = int(text)            # May Raise ValueError
    print("Division Result:", result, "Converted Integer:", converted)
 
except ValueError:
    # Triggered When Input Cannot Be Converted To The Expected Numeric Type
    print("Error: Invalid Input! Could Not Convert The Given Value To A Number.")
except ZeroDivisionError:
    # Triggered When The Denominator Is Zero
    print("Error: You Cannot Divide A Number By Zero!")