# Project 5 - Inventory Management System

inventory = {}  # Stores All Product Data

def add_product():
    product_id = input("Enter Product ID:")

    if product_id in inventory:
        print("Product ID Already Exists!")
        return

    name = input("Enter Product Name:")
    category = input("Enter Category:")
    price = float(input("Enter Price:"))
    quantity = int(input("Enter Quantity:"))

    inventory[product_id] = {
        "product_id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    print("Product Added!")
    print(f"Product ID: {product_id} | Name: {name} | Category: {category} | Price: Rs.{price} | Quantity: {quantity}")

def view_all():
    if len(inventory) == 0:
        print("No Products Found.")
        return

    for product_id in inventory:
        p = inventory[product_id]
        print(f"Product ID: {p['product_id']} | Name: {p['name']} | Category: {p['category']} | Price: Rs.{p['price']} | Quantity: {p['quantity']}")

def search_product():
    product_id = input("Enter Product ID To Search:")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    p = inventory[product_id]

    print("Product ID:", p['product_id'])
    print("Name:", p['name'])
    print("Category:", p['category'])
    print("Price:", p['price'])
    print("Quantity:", p['quantity'])

def stock_in():
    product_id = input("Enter Product ID:")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    qty = int(input("Enter Quantity To Add:"))

    inventory[product_id]["quantity"] += qty

    print("Stock Updated Successfully!")
    print("New Quantity:", inventory[product_id]["quantity"])

def stock_out():
    product_id = input("Enter Product ID:")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    qty = int(input("Enter Quantity To Remove:"))

    if qty > inventory[product_id]["quantity"]:
        print("Not Enough Stock.")
        return

    inventory[product_id]["quantity"] -= qty

    print("Stock Updated Successfully!")
    print("Remaining Quantity:", inventory[product_id]["quantity"])

def delete_product():
    product_id = input("Enter Product ID To Delete:")

    if product_id not in inventory:
        print("Product Not Found.")
        return

    confirm = input(f"Delete {inventory[product_id]['name']}? (y/n):")

    if confirm == "y":
        del inventory[product_id]
        print("Product Deleted.")
    else:
        print("Cancelled.")

# Main Menu Loop
while True:
    print("\n*** INVENTORY MANAGEMENT SYSTEM ***")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Stock In")
    print("5. Stock Out")
    print("6. Delete Product")
    print("7. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_product()
    elif choice == "4":
        stock_in()
    elif choice == "5":
        stock_out()
    elif choice == "6":
        delete_product()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice.")