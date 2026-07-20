sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("Original Dictionary:", sample_dict)
 
# popitem() Removes & Returns The Last Inserted (Key, Value) Pair
removed_1 = sample_dict.popitem()
print("First popitem() Removed:", removed_1)
 
removed_2 = sample_dict.popitem()
print("Second popitem() Removed:", removed_2)
 
print("Dictionary After Two popitem() Calls:", sample_dict)
 
# clear() Empties The Dictionary Completely
sample_dict.clear()
print("Dictionary After clear():", sample_dict)
 
# Difference Between pop() & popitem():
# - pop(key) Removes A Specific Key You Name, & Returns Its Value.
#   It Raises A KeyError If The Key Doesn't Exist (Unless A Default Is Given).
# - popitem() Removes & Returns The Last Inserted (Key, Value) Pair As A Tuple.
#   You Don't Choose Which Item Is Removed; Python Picks The Most Recently Added One.