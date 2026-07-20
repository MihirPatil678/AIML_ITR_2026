user_string = input("Enter A String:")
str_length  = len(user_string)
 
# Print Each Character With Its Index Using range(len(string))
print("Characters With Their Indices:")
for i in range(str_length):
    print("Index", i, ":", user_string[i])
 
# Reverse Order: Range Starts From Last Index (len-1) Down To 0, step=-1
print("\nString in reverse order:")
for i in range(str_length - 1, -1, -1):  # stop=-1 So Index 0 Is Included
    print(user_string[i], end="")
