items = [10, 20, 30, 20, 40, 50]
print("Original:", items)

# remove(value) -> Removes The First Occurrence Of The Given Value
items.remove(20)
print("After Remove(20):", items)

# pop(index) -> Removes & Returns The Item At The Given Index
removed = items.pop(3)
print("After pop(3) Removed Value:", removed, "List Now:", items)

# pop() With No Argument Removes & Returns The Last Item    
items.pop()
print("After pop():", items)

# clear() -> Removes All Items, Leaving An Empty List
items.clear()
print("After clear():", items)

# Difference:
#   remove() -> You Specify The Value To Delete (First Match Only)
#   pop() -> You Specify The Index To Delete