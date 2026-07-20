person = {"name": "Priya", "age": 21, "profession": "Engineer"}
 
# Safely Access A Key; Second Argument Is The Default If Key Is Missing
print("Age (Via get()):", person.get("age"))
print("Salary (Via get(), Default Used):", person.get("salary", "Not Available"))
 
# All Keys
print("Keys:", person.keys())
 
# All Values
print("Values:", person.values())
 
# All Key-Value Pairs
print("Items:", person.items())