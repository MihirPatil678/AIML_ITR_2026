"""
This Program Calculates The Area & Perimeter Of A Rectangle.
The Results Help Us Understand The Size Of The Rectangle And The
Distance Around Its Boundary.
"""

# Taking Input As Float Allows Users To Enter Decimal Values If Needed
length = float(input("Enter The Length Of The Rectangle:"))
width = float(input("Enter The Width Of The Rectangle:"))

# Area Is Useful For Measuring The Space Inside The Rectangle
area = length * width

# Perimeter Is Useful For Finding The Total Distance Around The Rectangle
perimeter = 2 * (length + width)

# Displaying The Results In A Clear And User-Friendly Format
print("Area Of The Rectangle:", area)

# Showing The Perimeter Separately Makes The Output Easier To Read
print("Perimeter Of The Rectangle:", perimeter)