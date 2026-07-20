# A Set With 5 Integers
int_set = {10, 20, 30, 40, 50}
print("Integer Set:", int_set)
print("Type:", type(int_set))

# A Set With Mixed Data Types
mixed_set = {42, "hello", 3.14, True, "world"}
print("Mixed Set:", mixed_set)
print("Type:", type(mixed_set))

# An Empty Set Must Use set(), Not {} (That Creates An Empty Dict)
empty_set = set()
print("Empty Set:", empty_set)
print("Type:", type(empty_set))

# A Set From The String "hello" Using set() Constructor
# Sets Store Only Unique Elements, So Duplicate Letters Are Removed
string_set = set("hello")
print("Set From 'hello':", string_set)
print("Type:", type(string_set))

# Why Sets Remove Duplicates:
# Sets Are Implemented Using Hash Tables.
# Each Element Is Hashed & Stored At A Unique Position.
# If Two Elements Have The Same Hash (i.e., They Are Equal), Only One Is Kept.