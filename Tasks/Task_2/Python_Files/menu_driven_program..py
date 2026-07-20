# The while Loop Keeps The Menu Running Until The User Chooses To Exit
while True:

    # Display The Menu Repeatedly
    print("\n****************************")
    print("   SIMPLE CALCULATOR MENU  ")
    print("****************************")
    print("1. Add Two Numbers")
    print("2. Subtract Two Numbers")
    print("3. Multiply Two Numbers")
    print("4. Divide Two Numbers")
    print("5. Exit")

    # Take Input From User For Menu Choice
    choice = int(input("Enter Your Choice (1-5):"))

    # Exit The Program If The User Chooses 5
    if choice == 5:
        print("\nExiting calculator. Goodbye!")
        break       # break Exits The While Loop Immediately

    # For Choices 1 To 4, Take Two Numbers As Input
    elif choice in [1, 2, 3, 4]:
        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        # Perform The Operation Based On The User's Choice
        if choice == 1:
            result = num1 + num2            # Addition
            print("\nResult:", result)

        elif choice == 2:
            result = num1 - num2            # Subtraction
            print("\nResult:", result)

        elif choice == 3:
            result = num1 * num2            # Multiplication
            print("\nResult:", result)

        elif choice == 4:
            # Handle Division By Zero Before Performing The Operation
            if num2 == 0:
                print("\nError: Cannot Divide By Zero!")
            else:
                result = num1 / num2        # Division
                print("\nResult:", result)

    # Handle Any Invalid Menu Choice (Not 1 To 5)
    else:
        print("\nInvalid Choice! Please Enter A Number Between 1 And 5.")