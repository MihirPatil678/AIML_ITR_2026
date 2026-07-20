# Importing Module
import math
print("Method 1 (import math) : math.pow(2, 4) =", math.pow(2, 4))
 
# Import Specific Function - Use Directly Without Prefix
from math import sqrt
print("Method 2 (from math import sqrt) : sqrt(25) =", sqrt(25))
 
# Import With Alias - Shorter Prefix, Useful For Long Module Names
import math as m
print("Method 3 (import math as m) : m.factorial(5) =", m.factorial(5))