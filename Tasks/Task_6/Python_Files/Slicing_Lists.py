numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Numbers List:", numbers)

# Syntax: list[start:stop:step] (stop Is Exclusive)

# First 4 Elements -> start=0 (default), stop=4
print("First 4 Elements:", numbers[:4])

# Last 3 Elements -> start=-3, stop=end (default)
print("Last 3 Elements:", numbers[-3:])

# Elements From Index 2 To 7 -> start=2, stop=7
print("Index 2 To 6:", numbers[2:7])

# Every Second Element -> step=2
print("Every Second Element:", numbers[::2])

# Reverse The List -> step=-1
print("Reverse The List:", numbers[::-1])