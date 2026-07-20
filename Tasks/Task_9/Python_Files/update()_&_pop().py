info = {"brand": "Samsung", "model": "A52", "price": 25000}
 
# update() Merges/Overwrites Keys From The Given Dictionary
info.update({"color": "Black", "price": 24000})
print("After Update:", info)
 
# pop() Removes A Key And Returns Its Value
removed_value = info.pop("model")
print("Removed Value (model):", removed_value)
 
print("Final Dictionary:", info)