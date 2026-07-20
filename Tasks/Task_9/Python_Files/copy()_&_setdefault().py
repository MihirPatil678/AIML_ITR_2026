d = {"a": 1, "b": 2}
 
# copy() Creates A Separate (Shallow) Copy; Changes To One Don't Affect The Other
d_copy = d.copy()
 
# setdefault() Adds The Key With The Given Value ONLY If It Doesn't Already Exist
d_copy.setdefault("c", 3)          # "c" Doesn't Exist -> Gets Added With Value 3
d_copy.setdefault("a", 100)        # "a" Already Exists -> Value Stays Unchanged
 
print("Original Dictionary:", d)
print("Copied Dictionary:", d_copy)