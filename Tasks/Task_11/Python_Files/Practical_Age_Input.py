try:
    age = int(input("Please Enter Your Age:"))
    if age < 0:
    # Manually Raising A ValueError With A Descriptive Message
        raise ValueError("Age Cannot Be Negative.")
    print("Your Age Is:", age)
except ValueError as e:
        # As e Captures The Exception Object So We Can Print Its Message
    print("Error:", e)