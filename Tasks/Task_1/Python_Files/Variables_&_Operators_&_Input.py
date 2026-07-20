# BMI Calculator

# Take Weight & Height As Input From The User
weight = float(input("Enter Your Weight In kg:"))
height = float(input("Enter Your Height In m:"))

# Calculate BMI
BMI = weight / (height ** 2)

# Print The Result
print("Your BMI Is:", round(BMI, 2))