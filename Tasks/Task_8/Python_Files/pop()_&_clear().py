s = {100, 200, 300, 400, 500}
print("Original set:", s)

# pop() Removes & Returns An Arbitrary Element (Unpredictable Which One)
popped = s.pop()
print("Popped Element:", popped)
print("Set After pop():", s)

# clear() Removes All Elements From The Set
s.clear()
print("Set After clear():", s)

# Differences:
# remove(x) -> Removes Element x; Raises KeyError If x Is Not Found
# discard(x) -> Removes Element x; Does Nothing If x Is Not Found
# pop() -> Removes & Returns A Random Element; Raises KeyError If Set Is Empty