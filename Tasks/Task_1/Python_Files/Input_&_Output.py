# Input From User
name = input("Enter Your Name:")
birth_year = int(input("Enter Your Birth Year:"))

#input() Always Returns String, Even If The User Types A Number
#To Do Arithmetic Operations, We Convert The String To An Integer Using int()

# Assume The Current Year Is 2026
current_year = 2026

# Calculate Age
age = current_year - birth_year

# Print The Result With Proper Formatting
print(name,"Is",age,"Years Old.")