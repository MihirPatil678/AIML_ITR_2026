fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

# First Occurrence Of 'banana'
print("First Index Of 'banana':", fruits.index('banana'))

# First 'banana' Starting From Index 2
print("Index Of 'banana' From Index 2:", fruits.index('banana', 2))

# Safe Search For 'kiwi'
try:
    print("Index Of 'kiwi':", fruits.index('kiwi'))
except ValueError:
    print("Not Found")