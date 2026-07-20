# Defining A Function
def calculate_sum(a, b):
    return a + b   # return Sends The Value Back To The Caller
 
result = calculate_sum(10, 25)
print("Sum:", result)
 
# Difference Between print() Inside A Function & return:
# print(): Displays The Value But Gives Nothing Back To The Caller.
# return: Sends The Value Back To The Caller So They Can Store/Use It Further.
 
# Defining A Function
def calculate_sum_with_print(a, b):
    print("Sum (From Inside):", a + b)   # Prints But Returns None
 
val = calculate_sum_with_print(10, 25)
print("Value Returned:", val)            # None, Because No Return Statement