scores = [85, 92, 78, 92, 65, 92, 88]
print("Scores:", scores)

# index() Returns The Position Of The First Occurrence
first_index = scores.index(92)
print("First Index Of 92:", first_index)

# count() Returns How Many Times The Value Appears
count_92 = scores.count(92)
print("Count Of 92:", count_92)

# User Input Check
num = int(input("Enter A Number To Search In Scores: "))
if num in scores:
    print(num, "Found At Index", scores.index(num), "Appears", scores.count(num), "Times.")
else:
    print(num, "Not Found In The List.")