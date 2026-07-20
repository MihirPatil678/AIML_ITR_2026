total = 0   # Global Variable
 
def add_value(x):
    global total          # Declare We Want To Modify The Global 'total'
    total = total + x
 
add_value(5)
print("Total After Adding 5:", total)
 
add_value(10)
print("Total After Adding 10:", total)
 
add_value(3)
print("Total After Adding 3:", total)
 
# Demonstrating That A Local Variable Cannot Be Accessed Outside Its Function:
def demo_local():
    local_var = "I Am Local"
    print("Inside Function:", local_var)
 
demo_local()
 
print("Outside Function:", local_var) # Local Variable 'local_var' Is Not Accessible