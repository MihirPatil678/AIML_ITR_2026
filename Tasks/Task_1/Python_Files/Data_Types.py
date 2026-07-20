# Creates One Variable Of Each Core Data Type
day = "Monday"          # String
date = 1                # Integer
temperature = 25.5      # Float
prediction = False      # Boolean

# Prints Each Variable Along With Its Data Type Using type()
print("Day Is", day, "& Its Data Type Is", type(day))
print("Date Is", date, "& Its Data Type Is", type(date))
print("Temperature Is", temperature, "& Its Data Type Is", type(temperature))
print("Prediction Is", prediction, "& Its Data Type Is", type(prediction))

# Converting The Integer To Float & Float To Integer
date= float(date)              # Converts Integer To Float
temperature= int(temperature)  # Converts Float To Integer

# Print The Results
print("\nDate After Conversion:", date, "& Its Data Type Is", type(date))
print("Temperature After Conversion:", temperature, "& Its Data Type Is", type(temperature))

# After Converting The Integer To Float, The Value Of Date Becomes 1.0
# After Converting The Float To Integer, The Value Of Temperature Becomes 25 (The Decimal Part Is Removed)