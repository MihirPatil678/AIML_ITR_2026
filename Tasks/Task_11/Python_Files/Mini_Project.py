while True:
    # Display menu
    print("\n***** Calculator Menu *****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
 
    choice = input("Enter Your Choice (1-5): ")
 
    # Exit Condition Checked Before Entering Try Block
    if choice == "5":
        print("Exiting The Calculator. Goodbye!")
        break
 
    try:
        num1 = float(input("Enter The First Number:"))
        num2 = float(input("Enter The Second Number:"))
 
        if choice == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {num1} × {num2} = {result}")
        elif choice == "4":
            result = num1 / num2           # May Raise ZeroDivisionError
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid Choice! Please Select A Number Between 1 & 5.")
 
    except ValueError:
        # Triggered When The User Enters Non-Numeric Input For A Number
        print("Error: Invalid Input! Please Enter Numeric Values.")
    except ZeroDivisionError:
        # Triggered Only For Division When The Denominator Is Zero
        print("Error: Division By Zero Is Not Allowed!")
    finally:
        # Runs After Every Iteration Regardless Of Success Or Error
        print("Operation Attempted.")