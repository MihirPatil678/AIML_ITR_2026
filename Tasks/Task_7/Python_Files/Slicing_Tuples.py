numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Syntax: tuple[start:stop:step]
# stop Index Is Excluded

# Index 2 To 7 (stop=8 To Include 7)
print(numbers[2:8])

# First 5 Elements (Index 0 To 4)
print(numbers[:5])

# Last 4 Elements
print(numbers[-4:])

# Every Second Element (step=2)
print(numbers[::2])

# Reverse (step=-1)
print(numbers[::-1])