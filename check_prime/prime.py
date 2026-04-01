import datetime

# Main method for find if a number is prime
def check_prime(number: int) -> bool:
    """Checks if the number passed is a prime.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if is prime False otherwise.
    """
    prime = True
    if number < 2:
        return False
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            prime = False
    return prime

# Method for check a range of numbers using check_prime()
def prime_in_range(number: int) -> list[int]:
    """Checks all prime until given number.

    Args:
        number (int): Number given.

    Returns:
        list[int]: List of all primes until given number.
    """
    primes = []
    for n in range(2,number):
        if check_prime(n):
            primes.append(n)
    return primes

# Method for check single number.
def is_prime(number: int) -> bool:
    """Check for single number.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if prime False otherwise.
    """
    return True if check_prime(number) else False

# Method for user input to check multiple numbers in one run
def user_choice(numbers: str) -> None:
    """Checks for multiple numbers provided by the user, if user chooses to save the results it will create a file named 'results.txt' and store the result.

    Args:
        numbers (str): Numbers given by the user. Ex: 1, 5, 11, 97
    """
    nums = numbers.split(',')
    records = []
    try:
        for a in nums:
            records.append(f"{a} - {is_prime(int(a))}\n")
        print(*[rec for rec in records])
        save_primes = input("Do you want to save the results (Y/n): ").lower()
        if save_primes == 'y':
            with open('results.txt', 'a') as foperation:
                for item in records:
                    foperation.write(item)
                foperation.close()
            print("Results save to 'results.txt'")
    except ValueError:
        print("Use only integer numbers.")
    
# Main loop
def main():
    while True:
        print("\n::: Prime Checks :::\n")
        print("1- Check if number is prime.")
        print("2- All prime numbers up to given number.")
        print("3- Check different numbers at once.")
        print("q- Exit.\n")
        user_input = input("Choice your option: ")
        if user_input == "1":
            number = int(input("Input a number: \n"))
            print(is_prime(number))
        elif user_input == "2":
            number = int(input("Input number: "))
            print(*prime_in_range(number))
        elif user_input == "3":
            nums = input("Input numbers to check separated by commas. Ex: 3,5,97: ")
            user_choice(nums)
        elif user_input == "q":
            break
        else:
            print("Invalid choice, please make sure you are selecting an existing choice")


if __name__ == "__main__":
    main()