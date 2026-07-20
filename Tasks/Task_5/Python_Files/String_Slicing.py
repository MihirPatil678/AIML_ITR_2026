user_string = input("Enter A String:")
 
# Slicing Syntax: string[start:end:step]
#   start -> Index To Begin (Inclusive), Default 0
#   end   -> Index To Stop  (Exclusive), Default len(string)
#   step  -> How Many Positions To Jump, Default 1
 
# start=0 (default), end=5
print("First 5 Characters:", user_string[:5])
 
# start=-4 (4th From end),
print("Last 4 Characters:", user_string[-4:])
 
# step=-1 Traverses From Right To Left
print("Reversed String:", user_string[::-1])
 
# step=2 Skips One Character Each Time
print("Every 2nd Character:", user_string[::2])