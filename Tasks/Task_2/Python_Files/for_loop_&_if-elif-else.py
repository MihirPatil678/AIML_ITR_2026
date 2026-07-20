# Starts At 1, Stops Before 41
for number in range(1, 41):

    # Check Divisibility By Both 3 & 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")        # If Divisible By Both 3 & 5

    # Check Divisibility By 3 Only
    elif number % 3 == 0:
        print("Fizz")            # If Divisible By 3 Only

    # Check Divisibility By 5 Only
    elif number % 5 == 0:
        print("Buzz")            # If Divisible By 5 Only

    else:
        print(number)            # Or Else Just Print The Number