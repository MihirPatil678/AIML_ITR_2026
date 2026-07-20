print("Numbers From 1 To 25:")
for i in range(1, 26):          # Starts At 1, Stops Before 26
    print(i, end=" ")

total = 0
for i in range(1, 21):          # Starts At 1, Stops Before 21
    total += i
print("\n\nSum Of 1 To 20:", total)
 
print("\nMultiplication Table Of 5:")
for i in range(1, 11):          # Starts At 1, Stops Before 11
    print("5 x", i, "=", 5 * i)

# When To Use A For Loop:
# - You Know In Advance How Many Iterations Are Needed.
# - You Want To Iterate Over A Sequence (List, Range, String, etc.).
# - Cleaner & Safer Than While When The Count Is Fixed.