# Take Inputs From The User
temperature = int(input("Enter The Temperature: "))
is_raining  = input("Is it raining? (yes/no):")

# Outer if: Check If Temperature Is Above 30 (Hot)
if temperature > 30:

    # Inner if: Check Rain Condition When It Is Hot
    if is_raining == "no":
        # If Hot & No Rain
        print("Hot day, wear light clothes.")
    else:
        # Or Else Hot & Raining
        print("Hot and rainy, carry an umbrella.")

# Outer elif: Check If Temperature Is Below 15 (Cold)
elif temperature < 15:

    # Inner if: Check Rain Condition When It Is Cold
    if is_raining == "yes":
        # If Cold & Raining
        print("Cold and rainy, wear a jacket and take an umbrella.")
    else:
        # Or Else Cold But No Rain
        print("Cold day, wear a warm jacket.")

# Outer else: Temperature Is Between 15 & 30
else:
    # Inner if: Check Rain Condition For Mild Weather
    if is_raining == "yes":
        # If Mild Temperature But Raining
        print("Mild but rainy, a light raincoat will do.")
    else:
        # Or Else Mild Temperature But No Rain
        print("Nice weather, enjoy your day!")