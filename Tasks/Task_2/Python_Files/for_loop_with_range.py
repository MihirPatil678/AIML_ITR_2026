# Print All Numbers From 1 To 30
print("Numbers From 1 To 30:")
for number in range(1, 31):      # Starts At 1, Stops Before 31
    print(number, end=" ")

# Print All Odd Numbers From 1 To 50
print("\nOdd Numbers From 1 To 50:")
for number in range(1, 51, 2):   # Starts At 1, Stops Before 51, Step Size 2 (Only Odd Numbers)
    print(number, end=" ")

# Print The Sum Of Numbers From 1 To 15
print("\nSum Of Numbers From 1 To 15:")
sum = 0                          
for number in range(1, 16):      # Starts At 1, Stops Before 16
    sum = sum + number           # Add Each Number To The Running Total
print(sum)                       # Print The Final Sum After The Loop Ends