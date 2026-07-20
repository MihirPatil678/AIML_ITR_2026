import math  # Built-In Module With Mathematical Functions & Constants

num = float(input("Enter A Number:"))
 
print("Square Root : math.sqrt(num) =", math.sqrt(num))
 
if num >= 0 and num == int(num):    # Factorial Only Works On Non-Negative Integers
    print("Factorial : math.factorial(int(num)) =", math.factorial(int(num)))
else:
    print("Factorial : Only Defined For Non-Negative Integers")
 
print("Ceiling Value : math.ceil(num) =", math.ceil(num))
print("Floor Value : math.floor(num) =", math.floor(num))