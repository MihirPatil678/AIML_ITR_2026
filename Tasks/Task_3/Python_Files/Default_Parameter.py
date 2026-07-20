# Default Parameter Allows Function To Use Predefined Values If No Argument Is Passed

# Defining A Function
def show_message(message="Hello"):
    print(message)
 
show_message()                  # Uses Default Value "Hello"
show_message("Good Morning!")   # Overrides Default With Passed Argument "Good Morning!"