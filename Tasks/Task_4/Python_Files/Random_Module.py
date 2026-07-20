import random  # Built-In Module For Generating Pseudo-Random Numbers
 
print("Random Module Demo:")
 
# Generate 5 Random Integers Between 1 & 100
print("5 Random Integers (1–100):")
for _ in range(5):
    print(random.randint(1, 100))
 
# One Random Integer Between 50 & 150
print("Random Integer (50–150):", random.randrange(50, 150))
 
# Random Float Between 0 & 1
print("Random Float (0–1):", random.random())