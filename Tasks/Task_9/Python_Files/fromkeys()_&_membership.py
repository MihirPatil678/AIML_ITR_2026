# Create A Dictionary With Given Keys, All Set To None Initially
user_info = dict.fromkeys(["name", "age", "city"], None)
print("Initial Dictionary:", user_info)
 
# Take User Input To Fill In The Keys
for key in user_info:
    user_info[key] = input("Enter Your " + key + ":")   
 
print("Filled Dictionary:", user_info)
 
# Membership Check Using The 'in' Operator
check_key = input("Enter A Key To Check If It Exists: ")
if check_key in user_info:
    print(check_key, "Exists In The Dictionary.")
else:
    print(check_key, "Does Not Exist In The Dictionary.")