number = int(input("Enter A Number:"))
 
if number in range(1, 51):
    print(number, "IS present in range(1, 51)  [1 to 50]")
else:
    print(number, "is NOT present in range(1, 51)  [1 to 50]")
 
if number in range(10, 100, 5):
    print(number, "IS present in range(10, 100, 5)  [10, 15, 20, ..., 95]")
else:
    print(number, "is NOT present in range(10, 100, 5)  [10, 15, 20, ..., 95]")