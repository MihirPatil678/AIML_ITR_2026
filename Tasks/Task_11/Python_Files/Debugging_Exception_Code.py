try:                                          # Fix 1: Added ':'
    num = int(input("Enter A Number:"))
    result = 100 / num
    print("Result:", result)
except ValueError:                            # Fix 2: Added ':'
    print("Please Enter A Valid Number")
except ZeroDivisionError:                     # Fix 3: Added specific handler
    print("Error: Cannot Divide By Zero!")
except Exception as e:                        # Generic Catch-All
    print("Some Error Occurred:", e)
