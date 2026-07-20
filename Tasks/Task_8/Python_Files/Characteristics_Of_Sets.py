numbers = {10, 20, 30, 20, 40, 10, 50}

print("Set (Duplicates Removed Automatically):", numbers)
print("Printing Again (Order May Vary):", numbers)
print("Printing Again (Order May Vary):", numbers)

# Python Does Not Guarantee Any Apecific Order When Iterating Or Printing A Set.
print(numbers[0])
# Trying Indexing - This Will Raise A TypeError:
# Error: 'set' Object Is Not Subscriptable
# Sets Do Not Support Indexing Or Slicing Because They Are Unordered.
# There Is No Concept Of A "first" Element In A Set.
print("Indexing (numbers[0]) Is Not Supported On Sets - Sets Are Unordered.")