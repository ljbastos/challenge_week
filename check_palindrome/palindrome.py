import re

# Clean string
def re_clean(text: str) -> str:
    """
    Eliminate all non-alphanumeric characters using regular expresions.

    Args:
        text (str): String to clean.
    Returns:
        text (str): String without non-alphanumeric characters.
    """
    text = re.sub(r"\W", "", text)
    return text

# Transform text to lowercase
def normalize_string(text: str) -> str:
    """
    Transform the string to lowercase.
    Args:
        text (srt): String to transform to lowercase.
    Returns:
        text (srt): Lowercase string.
    """
    p1 = re_clean(str(text)).lower()
    return p1

# Solution for reverse the string using slicing
def reverse_string(text: str) -> str:
    """
    Method for reverse a string using slicing.

    Args:
        text (str): String to reverse.
    Returns:
        text (str): Reversed string.
    Examples:
        Given string "asd" will return "dsa".
    """
    return text[::-1]

# Check if string is palindrome
def is_palindrome(text: str) -> str:
    """
    Check if the given string is a palindrome.
    Args:
        text (srt): String to check.
    Returns:
        bool: True if palindrome False otherwise.
    """
    check_str = normalize_string(text)
    return "Yes, it's a palindrome!" if check_str == reverse_string(check_str) else "Not a palindrome"

# Main loop
def main():
    """
    Main loop.
    """
    print("...::: Checking Palindromes :::...\nType /q for exit.\n")
    while True:
        user_input = input("Type your text: ")
        if user_input == "/q":
            break
        print(is_palindrome(user_input))

if __name__ == "__main__":
    main()