user_set = set()

print("Enter 6 Numbers (Duplicates Will Be Ignored):")
for i in range(6):
    num = int(input("Number:"))
    user_set.add(num)

print("Set After 6 Inputs:", user_set)

# Add Two More Numbers
extra1 = int(input("Add Extra Number 1:"))
user_set.add(extra1)
extra2 = int(input("Add Extra Number 2:"))
user_set.add(extra2)
print("After Adding Two More:", user_set)

# Safely Remove One Number
remove_val = int(input("Enter A Number To Remove (discard):"))
user_set.discard(remove_val)  # No Error Even If Not Present

print("Final Set:", user_set)
print("Length Of Final Set:", len(user_set))

