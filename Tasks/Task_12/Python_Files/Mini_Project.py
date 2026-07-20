import math
import random
from datetime import datetime
 
# Dictionary To Store Results: {timestamp_string: result_description}
history = {}
 
 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input! Please Enter A Numeric Value.")
 
 
def basic_arithmetic():
    print("\n*** Basic Arithmetic ***")
    print("Operations: +  -  *  /")
    op = input("Choose An Operation (+, -, *, /):").strip()
 
    num1 = get_number("Enter First Number:")
    num2 = get_number("Enter Second Number:")
 
    try:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2  # May Raise ZeroDivisionError
        else:
            print("Invalid Operation Selected.")
            return None
 
        print(f"Result: {num1} {op} {num2} = {result}")
        return f"{num1} {op} {num2} = {result}"
 
    except ZeroDivisionError:
        print("Error: Division By Zero Is Not Allowed.")
        return None
 
 
def scientific_calculations():
    print("\n*** Scientific Calculations ***")
    print("Options: 1) Square Root  2) Power  3) Factorial")
    choice = input("Choose An Option (1-3):").strip()
 
    try:
        if choice == "1":
            num = get_number("Enter A Number:")
            if num < 0:
                print("Cannot Calculate Square Root Of A Negative Number.")
                return None
            result = math.sqrt(num)
            print(f"Square Root Of {num} = {result}")
            return f"sqrt({num}) = {result}"
 
        elif choice == "2":
            base = get_number("Enter Base:")
            exponent = get_number("Enter Exponent:")
            result = math.pow(base, exponent)
            print(f"{base} ^ {exponent} = {result}")
            return f"{base}^{exponent} = {result}"
 
        elif choice == "3":
            num = int(get_number("Enter A Whole Number:"))
            if num < 0:
                print("Factorial Is Not Defined For Negative Numbers.")
                return None
            result = math.factorial(num)
            print(f"Factorial Of {num} = {result}")
            return f"{num}! = {result}"
 
        else:
            print("Invalid Option Selected.")
            return None
 
    except Exception as e:
        print(f"An Error Occurred During Calculation: {e}")
        return None
 
 
def generate_random_numbers():
    print("\n*** Generate Random Numbers ***")
    try:
        count = int(get_number("How Many Random Numbers Do You Want?"))
        low = int(get_number("Enter The Lower Bound:"))
        high = int(get_number("Enter The Upper Bound:"))
 
        if count <= 0 or low > high:
            print("Invalid Range Or Count Provided.")
            return None
 
        random_numbers = []
        for _ in range(count):
            random_numbers.append(random.randint(low, high))

        print(f"Generated random numbers: {random_numbers}")
        return f"Random numbers {random_numbers}"
 
    except Exception as e:
        print(f"An Error Occurred:{e}")
        return None
 
 
def store_result(description):
    if description is None:
        print("Nothing To Store.")
        return
 
    # Create A Timestamp String As The Dictionary Key
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history[timestamp] = description
    print(f"Result Stored Under Timestamp: {timestamp}")
 
 
def view_history():
    print("\n*** History ***")
    if not history:
        print("No Results Have Been Stored Yet.")
        return
 
    for timestamp, description in history.items():
        print(f"[{timestamp}] {description}")
 
 
def main():
    last_result = None  # Keeps Track Of The Most Recent Result For Storing
 
    while True:
        print("\n***** Smart Calculator & Data Manager *****")
        print("1. Basic Arithmetic")
        print("2. Scientific Calculations")
        print("3. Generate Random Numbers")
        print("4. Store Last Result In Dictionary")
        print("5. View History")
        print("6. Exit")
 
        try:
            choice = int(input("Enter Your Choice (1-6):"))
        except ValueError:
            print("Invalid Input! Please Enter A Number Between 1 & 6.")
            continue
 
        if choice == 1:
            last_result = basic_arithmetic()
        elif choice == 2:
            last_result = scientific_calculations()
        elif choice == 3:
            last_result = generate_random_numbers()
        elif choice == 4:
            store_result(last_result)
        elif choice == 5:
            view_history()
        elif choice == 6:
            print("Exiting Smart Calculator & Data Manager. Goodbye!")
            break
        else:
            print("Invalid Choice! Please Select An Option Between 1 & 6.")
 
 
if __name__ == "__main__":
    main()
 