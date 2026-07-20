colors = set()
print("Enter 5 Colors:")
for i in range(5):
    color = input(" Color:")
    colors.add(color)

print("Your Color Set:", colors)
search = input("Enter A Color To Search For:")

if search in colors:
    print(search, "IS In The Set.")
else:
    print(search, "Is NOT In The Set.")

if search not in colors:
    print("Confirmed:", search, "Is Not Present.")