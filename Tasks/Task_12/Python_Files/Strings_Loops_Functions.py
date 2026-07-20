def analyze_string(s):
    # Handle Empty String Case First
    if s == "":
        print("Error: The String Is Empty.Please Provide A Non-Empty String.")
        return
 
    # Length Of The String
    length = len(s)
    print(f"\nLength Of The String: {length}")
 
    # Reverse The String Using Slicing
    reversed_s = s[::-1]
    print(f"Reversed String: {reversed_s}")
 
    # Count Vowels (Case Insensitive)
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for j in s:
        if j in vowels:
            vowel_count += 1
    print(f"Number Of Vowels: {vowel_count}")
 
    # Print Each Character With Its Positive & Negative Index
    print("Character Indices (Positive & Negative):")
    for i in range(length):
        neg_index = i - length  # equivalent negative index
        print(f"  Char: '{s[i]}' : Positive Index: {i}, Negative Index: {neg_index}")
 
 
def main():
    user_input = input("Enter A String To Analyze: ")
    analyze_string(user_input)
 
 
if __name__ == "__main__":
    main()