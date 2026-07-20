# Defining Functions
def square(num):
    return num ** 2 # Returns The Square Of The Number
 
def cube(num):
    return num ** 3 # Returns The Cube Of The Number
 
number = int(input("Enter A Number : "))
print("Square Of", number, ":",square(number))
print("Cube Of", number, ":",cube(number))