from math import pow

OPERATIONS = ["add","rest","multiply","divide","modulus","exponents", "quit"]


# Add method
def add(a: int, b: int) -> int:
    """Sums two numbers.

    Args:
        a (int): Number one.
        b (int): Number two.

    Returns:
        int: Returns the sum of two numbers.
    """
    return a + b


# Rest method
def rest(a: int, b: int) -> int:
    """Rest two numbers.

    Args:
        a (int): Number one.
        b (int): Number two.

    Returns:
        int: Returns the rest of two numbers.
    """
    return a - b


# Multiplyy method
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a (int): Number one.
        b (int): Number two.

    Returns:
        int: Returns the multiplication of two numbers.
    """
    return a * b


# Divide method
def divide(a: int, b: int) -> float:
    """Divide two numbers.

    Args:
        a (int): Number one.
        b (int): Number two.

    Returns:
        int: Returns the division of two numbers.
    """
    return a / b


# Remainder method
def modulus(a: int, b: int) -> int:
    """Calculates the remainder of a division between two numbers.

    Args:
        a (int): Number one.
        b (int): Number two.

    Returns:
        int: Returns the remainder of a division between two numbers.
    """
    return a % b


# Power of number method
def exponents(a: int, b: int) -> int:
    """Calculates the power of a number

    Args:
        a (int): Base number.
        b (int): Exponent.

    Returns:
        int: Returns the power of base number elevated to exponent number.
    """
    return int(pow(a,b))


# Main loop
def main():
    print("\033c", end="")
    while True:
        print("\n...::: BASIC CALCULATOR :::...\n")
        print(f"Operations allowed: {', '.join(OPERATIONS)}\n")
        operation = input("Choose operation: ")
        if operation == "quit":
            break
        elif operation not in OPERATIONS:
            print("Invalid operation.")
            continue
        else:
            try:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))
                match operation:
                    case "add":
                        print(f"\nResult: {add(first_number, second_number)}")
                    case "rest":
                        print(f"\nResult: {rest(first_number, second_number)}")
                    case "multiply":
                        print(f"\nResult: {multiply(first_number, second_number)}")
                    case "divide":
                        print(f"\nResult: {divide(first_number, second_number)}")
                    case "modulus":
                        print(f"\nResult: {modulus(first_number, second_number)}")
                    case "exponents":
                        print(f"\nResult: {exponents(first_number, second_number)}")
            except ValueError:
                print("Please use integers numbers only.")
                continue
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
                continue
    

if __name__ == "__main__":
    main()