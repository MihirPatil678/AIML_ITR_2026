user_string = input("Enter A String:")
 
# len() Returns The Total Number Of Characters In The String
string_length = len(user_string)
print("Length Of String:", string_length)
 
print("Last Character (Using len-1):", user_string[string_length - 1])
 
# Middle Character Is Only Possible When Length Is Odd
if string_length % 2 != 0:
    print("Middle Character:", user_string[string_length // 2])
else:
    print("String Has Even Length (No Middle Character)")