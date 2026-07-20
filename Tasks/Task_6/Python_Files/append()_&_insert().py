# Empty List
cities = []

# append() Adds The Item To The End Of The List
cities.append("Mumbai")
cities.append("Delhi")
cities.append("Bangalore")

# Take User Input For Two More Cities And Append Them To The List
city1 = input("Enter A City Name:")
city2 = input("Enter Another City Name:")

cities.append(city1)
cities.append(city2)

print("After 5 Appends:\n", cities)

# insert(index, value) Places The Item At The Given Index
cities.insert(2, "Hyderabad")
print("After Inserting 'Hyderabad' At Position 2:\n", cities)