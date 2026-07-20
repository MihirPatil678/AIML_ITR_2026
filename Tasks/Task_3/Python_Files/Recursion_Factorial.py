def factorial(n):
    # Base Case: Factorial Of 0 Or 1 Is 1
    if n <= 1:
        return 1
    return n * factorial(n - 1)   # Recursive Call
 
n = int(input("Enter A Number For Factorial : "))
print("Factorial of", n, ":", factorial(n))