marks = [45, 78, 65, 90, 34, 82, 71]
print("Original Marks:", marks)

# sort() Rearranges Elements In Ascending Order By Default
marks.sort()
print("Ascending Order:", marks)

# sort(reverse=True) Rearranges Elements In Descending Order
marks.sort(reverse=True)
print("Descending Order:", marks)

# Reset To Original, Then Reverse()
marks = [45, 78, 65, 90, 34, 82, 71]
marks.reverse()
print("Reversed (No Sort):", marks)

# Difference:
#   sort() -> Reorders Elements By Value (Ascending or Descending)
#   reverse() -> Simply Flips The Current Order, Regardless Of Values