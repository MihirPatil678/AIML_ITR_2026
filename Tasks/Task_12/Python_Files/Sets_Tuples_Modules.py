import random
import math
 
 
def main():
    number_set = set()  # Unique Numbers Only
 
    print("Enter 10 Numbers (Duplicates Will Be Automatically Ignored):")
    count = 0
    while count < 10:
        try:
            value = float(input(f"Number {count + 1}: "))
            number_set.add(value)
            count += 1
        except ValueError:
            print("Invalid Input! Please Enter A Numeric Value.")
 
    # Convert The Set Into A Tuple
    number_tuple = tuple(number_set)
    print(f"\nUnique Numbers Set: {number_set}")
    print(f"Converted To Tuple: {number_tuple}")
 
    # Use Random Module To Pick 3 Random Numbers From The Tuple
    try:
        sample_size = min(3, len(number_tuple))
        random_numbers = random.sample(number_tuple, sample_size)
        print(f"3 Random Numbers From The Tuple: {random_numbers}")
    except ValueError as e:
        print(f"Could Not Sample Random Numbers: {e}")
 
    # Use Math Module To Print The Square Root Of The Sum Of Tuple Elements
    try:
        total = sum(number_tuple)
        if total < 0:
            print("Cannot Compute Square Root Of A Negative Sum.")
        else:
            sqrt_value = math.sqrt(total)
            print(f"Sum Of Tuple Elements: {total}")
            print(f"Square Root Of The Sum: {sqrt_value:.2f}")
    except Exception as e:
        print(f"An Error Occurred While Calculating The Square Root: {e}")
 
 
if __name__ == "__main__":
    main()