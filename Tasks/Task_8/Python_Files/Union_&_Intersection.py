A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union: All Elements From Both Sets (No Duplicates)
print("Union Using .union():", A.union(B))
print("Union Using | Operator:", A | B)

# Intersection: Only Elements That Appear In Both Sets
print("Intersection Using .intersection():", A.intersection(B))
print("Intersection Using & Operator:", A & B)

# Union Gives Every Unique Element Across Both Sets.
# Intersection Gives Only The Common Elements Shared By Both Sets.