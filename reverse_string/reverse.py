# reverse.py
import time

# Testing list for assignment, feel free to modify.
testing_list: list = ["Man2ca", "Gr+-avill4", "4be,ja", "beg.g1ng", "a.sf3e", "pure", 234, 0.42]

# Removes al non alphanumeric characters
def clean_text(text: str) -> str:
    """
    Cleans given text of alphanumeric characters and returns a string.
    Params:
        text(str): Text to clean.
    Returns:
        text(str): Text without non alphanumeric characters.
    """
    clean_text = ''.join(ch for ch in text if ch.isalpha())
    return clean_text

# Solution when a list is passed as a parameter it will return a string after concatenating al chars in it.
def reshape(list_text: list[str]) -> str:
    """
    Method for concatenate a given list into a single string.
    
    Args:
        list_text (list): List to concatenate into a single string.
    Returns:
        list_text (str): Returns a single string.
    """
    return ''.join(str(ch) for ch in list_text)

# Method to be used as a decorator for measure the performance. (First time using decorators, be nice :-)
# Still need to figure how to do the docstrings on this. Tricky...
def performance(func):
    """
    Method for calculate the time it takes a function to complete.
    Args:
        function (function): The function to  be run.
    Returns:
        result_function (tuple): Returns the result of the passed function.
    """
    def perf(text) -> tuple:
        """
        Runs the given function as a parameter and returns a tuple with str and elapsed time ffrom start to end.
        Args:
            text (str): String to reverse.
        Returns:
            result (tuple): Returns a tuple with str and the time it took to complete.
        Example:
            reverse("asd") it will return ("dsa, 0.000002).
        """
        start = time.perf_counter()
        result = func(text)
        end = time.perf_counter() - start
        return result, end
    return perf

# Solution for reverse the string using slicing, also using a decorator for measure runtime.
@performance
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

# Solution for reverse the string using for loop, also using a decorator for measure runtime.
@performance
def reverse_string_loop(text: str) -> str:
    """
    Method for reverse a string using a for loop.

    Args:
        text (str): String to reverse.
    Returns:
        text (str): Reversed string.
    Examples:
        Given string "asd" will return "dsa".
    """
    size = len(text) - 1
    rev_text = ''
    for _ in range(len(text)):
        rev_text += text[size]
        size -= 1
    return rev_text

# Main loop where the magic happens.
def main():
    """
    Main loop of program.
    """
    print(f"\nList for testing: {testing_list}\n")
    user_input = input("Input text: ")
    
    clean_input = clean_text(user_input)
    result_reverse = reverse_string(clean_input)
    print(f"\nReverse using slicing: {result_reverse[0]} | {result_reverse[1]:.6f}s\n")
    result_loop = reverse_string_loop(clean_input)
    print(f"Reverse using loop:    {result_loop[0]} | {result_loop[1]:.6f}s\n")
    
    
    list_input = clean_text(reshape(testing_list))
    reverse_list = reverse_string(list_input)
    print(f"\nReverse list using slicing: {reverse_list[0]} | {reverse_list[1]:.6f}s\n")
    reverse_loop_list = reverse_string_loop(list_input)
    print(f"Reverse list using loop:    {reverse_loop_list[0]} | {reverse_loop_list[1]:.6f}s\n")

if __name__ == "__main__":
    main()