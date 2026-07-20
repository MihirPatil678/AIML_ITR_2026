# String Analyzer Program

# Take String Input From The User
user_string = input("Enter A String:")

# Print Length Of The String
print("\n1.Length Of The String:")
print(len(user_string))

# Print First Half & Second Half Using Slicing
middle_index = len(user_string) // 2

first_half = user_string[:middle_index]
second_half = user_string[middle_index:]

print("\n2.String Halves:")
print("First Half:", first_half)
print("Second Hal:", second_half)

# Check If The Word "python" Is Present (Case-Insensitive)
print("\n3.Checking For The Word 'python':")

if "python" in user_string.lower():
    print("'python' Is Present In The String.")
else:
    print("'python' Is Not Present In The String.")

# Print All Characters With Their Positive And Negative Indices
print("\n4.Characters With Positive & Negative Indices:")

string_length = len(user_string)

for positive_index in range(string_length):
    negative_index = positive_index - string_length
    print(
        "Character:" ,user_string[positive_index],"| "
        "Positive Index:", positive_index,"| "
        "Negative Index:",negative_index
    )

# Print The String In Reverse
print("\n5.Reversed String:")
print(user_string[::-1])