# Lambda Function With Multiple Arguments
add_three = lambda a, b, c: a + b + c
 
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
print("Sum Of Three Numbers:", add_three(a, b, c))