import random

# Random lists for testing purposes
numbers: list = [random.randint(-10, 10) for _ in range(10)]
n_floats: list = [round(random.uniform(-10.0, 10.0), 2) for _ in range(10)]
# Extending integers list to add floats list
numbers.extend(n_floats)

# Check for invalid values
def check_values(numbers: list) -> bool:
    """ Check given list does not contain invalid values.

    Args:
        numbers (list): List of numbers to check.

    Returns:
        bool: False if is instance of (str) or (bool) otherwise True.
    """
    for num in numbers:
        if isinstance(num, str) or isinstance(num, bool):
            return False
    return True


# Find the max value
def find_max(numbers: list) -> None:
    """Find max value in list.

    Args:
        numbers (list): List containing integers and floats.
    """
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    print(f"Max number using FOR LOOP is:    {max_value} and index value is: {numbers.index(max_value)}\n")


def find_max_wh(numbers: list) -> None:
    max_value = numbers[0]
    run_times = len(numbers)
    step = 0
    while step < run_times:
        if numbers[step] > max_value:
            max_value = numbers[step]
        step += 1
    print(f"Max number using WHILE LOOP is:  {max_value} and index value is: {numbers.index(max_value)}")


# Main loop
def main():
    """
    Main loop.
    """
    if check_values(numbers):
        try:
            find_max(numbers)
            find_max_wh(numbers)
        except IndexError:
            print("Exiting...\tList cannot be empty")
    else:
        print("Make sure that all values in the list are Integers or Floats")


if __name__ == "__main__":
    main()
