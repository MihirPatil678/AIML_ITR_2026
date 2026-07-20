items = set()  # Main Collection

while True:
    print("\n*** Menu ***")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Unique Items")
    print("4. Check If An Item Exists")
    print("5. Clear All Items")
    print("6. Exit")

    choice = int(input("Choose An Option (1-6):"))

    if choice == 1:
        item = input("Enter Item To Add:")
        items.add(item)  # add() Ignores The Item If It Already Exists
        print(item, "added. Current items:", items)

    elif choice == 2:
        item = input("Enter Item To Remove:")
        items.discard(item)  # discard() Won't Raise Error If Item Is Missing
        print(item, "Removed (If It Existed). Current Items:",items)

    elif choice == 3:
        if items:
            print("All Unique Items:", items)
        else:
            print("The Collection Is Empty.")

    elif choice == 4:
        item = input("Enter Item To Check:")
        if item in items:
            print(item, "Exists In The Collection.")
        else:
            print(item, "Does Not Exist In The Collection.")

    elif choice == 5:
        items.clear()  # Removes All Elements; Set Becomes Empty
        print("All Items Cleared.", items)

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice. Please Enter A Number Between 1 & 6.")