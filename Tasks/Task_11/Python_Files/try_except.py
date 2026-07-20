try:
    num1 = float(input("Enter The First Number:"))
    num2 = float(input("Enter The Second Number:"))
    result = num1 / num2
    print("Result Of Division:", result)
except ValueError:
    print("Oops! That Doesn't Look Like A Valid Number. Please Enter Numeric Values.")