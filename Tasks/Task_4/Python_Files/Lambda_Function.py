# Lambda Function
# Lambda: square = lambda x: x ** 2  -> Single-Line, No Name Needed Internally
# Use lambda For Short, Throwaway Operations (e.g., Inside Map/Filter/Sorted).
square = lambda x: x ** 2
 
# Normal def Function For Comparison
# Def: def square_def(x): -> Multi-Line, Readable
# Use def For Anything Reusable, Complex, Or That Needs Documentation.
def square_def(x):
    return x ** 2

number = int(input("Enter A Number:"))

print("Square (lambda):", square(number))
 
print("Square (def):", square_def(number))


