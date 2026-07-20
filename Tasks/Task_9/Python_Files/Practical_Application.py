contacts = {}
 
num_contacts = int(input("How Many Contacts Do You Want To Add:"))
for _ in range(num_contacts):
    name = input("Enter Name:")
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")

    # Store Each Contact's Details As A Nested Dictionary, Keyed By Name
    contacts[name] = {"Phone": phone, "Email": email}
 
# Search A Contact By Name Using get() (Returns None If Not Found)
search_name = input("\nEnter A Name To Search:")
found_contact = contacts.get(search_name)
if found_contact:
    print("Contact Found:", search_name, "->", found_contact)
else:
    print("No Contact Found With The Name", search_name,)
 
# Print All Contacts Using items()
print("\nAll Contacts:")
for name, details in contacts.items():
    print(name, ":", details)
