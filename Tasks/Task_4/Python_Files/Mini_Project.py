import math
import random
 
# Lambda Function
square = lambda x: x ** 2
 
# Normal Functions
def calculate_power(base, exp):
    return math.pow(base, exp)
 
def display_menu():
    print("\n***** Math Utility Menu *****")
    print("  1. Square Of A Number")
    print("  2. Power Of A Number")
    print("  3. Generate A Random Number (1–100)")
    print("  4. Exit")
 
print("Simple Math Utility Program")
 
while True:
    display_menu()
    choice = input("Enter Your Choice (1/2/3/4):")
 
    if choice == "1":
        num = float(input("Enter A Number:"))
        print("Square Of", num,"=", square(num))
 
    elif choice == "2":
        base = float(input("Enter Base:"))
        exp  = float(input("Enter Exponent:"))
        print(base, "^", exp, "=", calculate_power(base, exp))
 
    elif choice == "3":
        rand_num = random.randint(1, 100)
        print("Random Number Generated:", rand_num)
 
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
 
    else:
        print("Invalid Choice. Please Enter 1, 2, 3, Or 4.")
 

