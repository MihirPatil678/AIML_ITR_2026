try:
    num = float(input("Enter A Number To Divide 100 By:"))
    result = 100 / num
    print("Result:", result)
except (ValueError, ZeroDivisionError):
    # A Single except Block Handling Two Exception Types Via A Tuple
    print("Error: Please Enter A Valid Non-Zero Number."
          "(Invalid Input Or Division By Zero Detected.)")