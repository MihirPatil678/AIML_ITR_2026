# Define A Recursive Function To Print A Countdown From A Given Number
def countdown(n):
    # Base Case: Stop Recursion When n Reaches 0
    if n <= 0:
        return
    print(n)
    countdown(n - 1)   # Recursive Call With n Reduced By 1
 
print("Countdown From 10:")
countdown(10)