coordinates = (10, 20)

coordinates[0] = 99  
# This Will Raise A TypeError Because Tuples Are Immutable
# Trying To Change An Element - Raises TypeError:
# 'tuple' Object Does Not Support Item Assignment
# coordinates[0] = 99 <- This Would Crash

coordinates.append(30)
# This Will Raise An AttributeError Because Tuples Are Immutable
# Trying To Append - Raises AttributeError:
# 'tuple' Object Has No Attribute 'append'
# coordinates.append(30) <- This Would Crash

# Correct Way: Convert To List, Modify, Convert Back
temp = list(coordinates)
temp[0] = 99
temp.append(30)
coordinates = tuple(temp)
print("Modified Coordinates:", coordinates)