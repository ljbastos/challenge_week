import re

# Most common stop words according to some website from Google.
STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Manage files operations like read and save
def file_operation(path_of_file: str, mode: int, data=None):
    """Read file to extract text if mode=0, if mode=0 write 'data' to file.

    Args:
        path_of_file (str): Path to file to read and extract text.
        mode (int): 0 for read from file, 1 for write results to 'result.txt'.
        data (str, optional): _description_. Data to be writed in case of 'mode' = 1.
    """
    text = []
    try:
        if mode == 0:
            with open(path_of_file, 'r', encoding="utf-8") as file:
                text = file.read()
                file.close()
                return text
        elif mode == 1 and data != None:
            with open('result.txt', 'a') as file:
                file.write(f"{str(data)}\n\n")
                file.close()
                print("Saved succesfully")
        else:
            print("Empty result or invalid mode.")
    except FileNotFoundError:
        print(f"No such file '{path_of_file}', check file exist.")
    except PermissionError:
        print("Permission denied")

# Clean non-alpha
def clean_text(text: list[str]) -> list[str]:
    """Replace non-alpha characters.

    Args:
        text (list[str]): List to clean.

    Returns:
        list[str]: Normalized list whitout non-alpha characters.
    """
    raw_text = [a.lower() for a in text]
    special_chars = r"[^a-zA-Z]"
    clean_text = [re.sub(special_chars, '', tx) for tx in raw_text]
    return clean_text

# Removes stop words
def clean_stop_words(text: list[str]) -> list[str]:
    """Removes common stop words in the list.

    Args:
        text (list[str]): List to remove stop words.

    Returns:
        list[str]: Normalize list without stop words.
    """
    clean_text = []
    clean_text.extend([tx for tx in text if tx not in STOP_WORDS])
    return clean_text

# Methods for count words
def word_count(text: list[str]) -> dict[str,int]:
    """Count how many time a word repeats in the text.

    Args:
        text (list[str]): List to count words.

    Returns:
        dict[str,int]: Dictionary sorted by the highest repeated word to the lowest.
    """
    raw_text = text.split()
    normalized = clean_text(raw_text)
    nstop_words = clean_stop_words(normalized)
    result = {key: nstop_words.count(key) for key in nstop_words}
    return dict(sorted(result.items(), key=lambda item:item[1], reverse=True))


# main loop
def main():
    while True:
        print("\nWord Count\n")
        print("1. User text input.")
        print("2. Import text from file.")
        print("3. View saved counts.")
        print("4. Exit.\n")
        choice = input("Select choice: ")
        if choice in ["1","2","3","4"]:
            match choice:
                case "1":
                    user_text = input("Type|paste text to process: ")
                    result = word_count(user_text)
                    print(f"\nResult: {result}\n")
                    save = input("\nDo you wish to save results? (Y/n): ").lower()
                    file_operation('results.txt', 1, result) if save == "y" else exit()
                case "2":
                    file_path = input("\nName of file to import: ")
                    raw_text = file_operation(file_path, 0)
                    result = word_count(raw_text)
                    print(f"\nResult: {result}\n")
                    save = input("\nDo you wish to save results? (Y/n): ").lower()
                    file_operation('results.txt', 1, result) if save == "y" else exit()
                case "3":
                    raw_text = file_operation('result.txt', 0)
                    print(raw_text) if raw_text != None else None
                case "4":
                    break
        else:
            print("\nInvalid choice.")
        


if __name__ == "__main__":
    main()