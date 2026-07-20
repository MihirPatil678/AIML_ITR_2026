# Negative Step Counts Down (Start Must Be Greater Than Stop)
# range(start, stop, step) Where step < 0 Goes From start Down To stop+1
 
print("Numbers From 20 Down To 10:")
for num in range(20, 9, -1):    # stop=9 so 10 is included
    print(num, end=" ")
 
print("\nNumbers From 15 Down To 1 In Steps Of 2:")
for num in range(15, 0, -2):    # stop=0 so 1 is included
    print(num, end=" ")
 