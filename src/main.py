
PROGRAM_TITLE = "Python Calculator"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def get_number():
    while True:
        try:
            return float(input("Enter number: "))
        except ValueError:
            print("Invalid number")


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5


if __name__ == "__main__":
    print(PROGRAM_TITLE)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")

    choice = input("Choose operation: ")

    if choice == "6":
        number = get_number()
        try:
            print("Result:", square_root(number))
        except ValueError as error:
            print(error)
    else:
        a = get_number()
        b = get_number()

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            try:
                print("Result:", divide(a, b))
            except ValueError as error:
                print(error)
        elif choice == "5":
            print("Result:", power(a, b))
        else:
            print("Invalid choice")
