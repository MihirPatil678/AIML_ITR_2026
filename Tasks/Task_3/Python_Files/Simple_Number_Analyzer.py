# Function To Get A Number From The User
def get_number():
    return int(input("\nEnter A Number (0 To Exit):"))

# Function To Check If A Number Is Even
def is_even(num):
    return num % 2 == 0

# Function To Calculate Power (Default Exponent Is 2)
def power(base, exp=2):
    return base**exp

# Function To Display The Result
def show_result(num):
    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")

    print("Square Of", num, ":65", power(num))


while True:
    number = get_number()

    if number == 0:
        print("Program Terminated.")
        break

    show_result(number)