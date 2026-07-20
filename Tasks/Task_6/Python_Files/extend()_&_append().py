list1 = [1, 2, 3]
list2 = [4, 5, 6]

# extend() Unpacks list2 & Adds Each Element Individually To list1
list1.extend(list2)
print("After extend():", list1)

# append() Adds list2 As A Single Nested Element
list1_copy = [1, 2, 3]
list1_copy.append(list2)
print("After append():", list1_copy)

# Difference:
#   extend() -> Merges The Second List Into The First (Flat)
#   append() -> Adds The Second List As One Element (Nested)