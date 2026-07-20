def manage_marks():
    marks = []  # List To Store The 5 Subject Marks
    subjects = 5

    # Loop Until We Collect 5 Valid Numeric Marks
    i = 1
    while i <= subjects:
        try:
            value = float(input(f"Enter Marks For Subject {i}: "))
            marks.append(value)
            i += 1  # Only Move To Next Subject If Input Was Valid
        except ValueError:
            # Handle Non-Numeric Input Gracefully & Re-Prompt
            print("Invalid Input! Please Enter A Numeric Value.")

    # Calculate Average, Highest, & Lowest Using Built-In Functions
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"\nMarks Entered: {marks}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")

    # Sort The List In Descending Order
    marks.sort(reverse=True)
    print(f"Marks Sorted In Descending Order: {marks}")


if __name__ == "__main__":
    manage_marks()