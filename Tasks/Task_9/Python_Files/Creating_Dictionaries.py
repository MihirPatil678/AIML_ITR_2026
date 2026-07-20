# Empty Dictionary - Two Different Ways
empty_dict_1 = {}              # Method 1: Using Curly Braces
empty_dict_2 = dict()          # Method 2: Using The dict() Constructor
print("Empty Dict (Curly Braces):", empty_dict_1) 
print("Type:", type(empty_dict_1))
print("Empty Dict (dict()):", empty_dict_2)
print("Type:", type(empty_dict_2))
 
# Dictionary With String Keys
string_key_dict = {
    "name": "Mihir",
    "city": "Pune",
    "course": "AIML"
}

print("\nString-Key Dict:", string_key_dict)
print("Type:", type(string_key_dict))
 
# Dictionary With Integer Keys
int_key_dict = {
    1: "One",
    2: "Two",
    3: "Three"
}
print("\nInteger-Key Dict:", int_key_dict)
print("Type:", type(int_key_dict))
 
# Mixed Data Type Dictionary (Keys/Values Can Mix tr, int, float)
mixed_dict = {
    "id": 101,          # Int Value
    "price": 499.99,    # Float Value
    "label": "Laptop"   # String Value
}
print("\nMixed-Data-Type Dict:", mixed_dict)
print("Type:", type(mixed_dict))