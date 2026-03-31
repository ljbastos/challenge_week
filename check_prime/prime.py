import datetime

def check_prime(number: int) -> bool:
    prime = True
    if number <= 1:
        return False
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            prime = False
    return prime


def prime_in_range(number: int) -> list[int]:
    primes = []
    for n in range(2,number):
        if check_prime(n):
            primes.append(n)
    return primes


def is_prime(number: int) -> bool:
    return True if check_prime(number) else False


def user_choice(numbers: str) -> None:
    nums = numbers.split(',')
    records = []
    try:
        for a in nums:
            records.append(f"{a} - {is_prime(int(a))} - {datetime.date.today()}\n")
        save_primes = input("Do you want to save the results (Y/n): ").lower()
        if save_primes == 'y':
            with open('results.txt', 'a') as foperation:
                for item in records:
                    foperation.write(item)
                foperation.close()
            print("Results save to 'results.txt'")
    except ValueError:
        print("Use only integer numbers.")
    

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