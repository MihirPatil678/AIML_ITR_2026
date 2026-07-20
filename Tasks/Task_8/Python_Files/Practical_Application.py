scores = [85, 92, 78, 92, 85, 88, 95, 78]
print("Original List:", scores)

# Convert List To Set - Duplicates Removed Automatically
unique_scores = set(scores)
print("Unique Scores (Set):", unique_scores)

# Convert Back To A Sorted List
sorted_scores = sorted(list(unique_scores))
print("Sorted Unique Scores:", sorted_scores)
print("Total Unique Scores:", len(sorted_scores))