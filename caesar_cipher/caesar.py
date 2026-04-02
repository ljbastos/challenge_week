ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Converts from letter to index position in alphabet
def to_ord(letter: str, shift: int, ed: int = 0) -> tuple:
    """Convert letter to index position of alphabet and shift position
       acording to user input value.

    Args:
        letter (str): Letter to find index position.
        shift (int): Amount of shifting, can be positive or negative.
        ed (int, optional): Flag that allows use this method for encode or decode. Defaults to 0 to encode, to 1 to decode.

    Returns:
        tuple: Returns the index of the letter and True if uppercase otherwise False. Ex: (12, True)
    """
    upper_case = True if letter.isupper() else False
    current_index = ALPHABET.index(letter.lower())
    if ed == 0:
        new_index = (current_index + shift) % 26
    elif ed == 1:
        new_index = (current_index - shift) % 26
    return new_index, upper_case

# Converts from index position of alphabet to letter
def to_chr(letter: int, upper_case: bool) -> str:
    """Converts alphabet index to letter.

    Args:
        letter (int): Index of letter in alphabet.
        upper_case (bool): Flag for uppercase or lowercase.

    Returns:
        str: Returns letter, uppercase if flag 'upper_case' True otherwise lowercase.
    """
    if upper_case:
        return ALPHABET[letter].upper()
    else:
        return ALPHABET[letter]

# Method to encode text
def caesar_cipher(text: str, shift: int) -> list[str]:
    """Encode a given text using 'shift' parameter for the amount of shifting.

    Args:
        text (str): Text to encode.
        shift (int): Amount of positions to shift.

    Returns:
        list[str]: Returns text encoded.
    """
    encoded = []
    for letter in text:
        if letter.isalpha():
            s_coded = to_ord(letter, shift)
            h_coded = to_chr(*s_coded)
            encoded.append(h_coded)
        else:
            encoded.append(letter)
    return encoded

# Method for decode
def decode(text: str, shift: int) -> list[str]:
    """Decode given text using 'shift' parameter for the amount of shifting.

    Args:
        text (str): Text to decode.
        shift (int): Amount of positions to shift.

    Returns:
        list[str]: Returns decoded text.
    """
    decoded = []
    for letter in text:
        if letter.isalpha():
            s_decoded = to_ord(letter, shift, ed=1)
            h_decoded = to_chr(*s_decoded)
            decoded.append(h_decoded)
        else:
            decoded.append(letter)
    return decoded

# Method for save message to file
def save_file(message: str) -> None:
    """Save encoded message to file 'messages.txt'

    Args:
        message (str): Encoded message to save.
    """
    try:
        with open('messages.txt', 'a') as file:
            file.write(message + '\n')
            file.close()
            print("Message saved.")
    except PermissionError:
        print("Permission denied to create file")

# Main loop method
def main():
    user_text = input("\nMessage to encode: ")
    try:
        user_shift = input("Shifting number: ")
        encoded = ''.join(caesar_cipher(user_text, int(user_shift)))
        save_file(encoded)
        print(f"\nMessage: {encoded}\n")
    except ValueError:
        print("For 'shift' use only integer numbers. Exiting.")
    
        
if __name__ == "__main__":
    main()