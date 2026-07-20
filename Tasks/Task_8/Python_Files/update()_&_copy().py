set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# copy() Creates A Shallow Copy - Changes To set1 Won't Affect set1_copy
set1_copy = set1.copy()

# update() Adds All Elements From set2 Into set1 (In-Place Union)
set1.update(set2)

print("Original Copy Of set1:", set1_copy)
print("set1 After update() With set2:", set1)