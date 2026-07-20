main_string = input("Enter The Main String:")
sub_string  = input("Enter The Substring To Search:")
 
# 'in' Returns True If sub_string Exists Inside main_string (Case-Sensitive)
if sub_string in main_string:
    print("Using 'in': Substring Found!")
else:
    print("Using 'in': Substring Not Found!")
 
# 'not in' Returns True If sub_string Does Not Exist Inside main_string
if sub_string not in main_string:
    print("Using 'not in': Substring Not Found!")
else:
    print("Using 'not in': Substring Found!")