fruits = {'apple', 'banana', 'mango'}
print("Initial Set:", fruits)

# Add 'orange'
fruits.add('orange')
print("After Add('orange'):", fruits)

# Add 'banana' Again - No Duplicate, No Error, Set Unchanged
fruits.add('banana')
print("After Add('banana') Again:", fruits)  # banana Already Exists

# Remove 'mango' - remove() Raises KeyError If Element Doesn't Exist
fruits.remove('mango')
print("After Remove('mango'):", fruits)

# discard 'grape' — discard() Does Not Raise An Error If Missing
fruits.discard('grape')
print("After discard('grape') (grape Wasn't There):", fruits)