def main():
    try:
        # Lambda Function To Compute The Square Of A Number
        square = lambda x: x ** 2
        squares=[]

        # Generate Numbers 1 To 20 & Store Their Squares
        for n in range(1,21):
            squares.append(square(n))
        print(f"Squares Of Numbers 1-20: {squares}")

        # Filter & Print Only The Even Squares
        even_squares=[]
        for s in squares:
            if s % 2 == 0:
                even_squares.append(s)
        print(f"Even Squares: {even_squares}")

    except Exception as e:
        # General Exception Handling In Case Something Unexpected Occurs
        print(f"An Error Occurred: {e}")


if __name__ == "__main__":
    main()