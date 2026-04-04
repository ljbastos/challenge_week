from datetime import datetime

TIME = datetime.now()

# For file operation
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
            with open('log.txt', 'a') as file:
                file.write(f"{str(data)}\n")
                file.close()
                print("Saved succesfully")
        else:
            print("Empty result or invalid mode.")
    except FileNotFoundError:
        print(f"No such file '{path_of_file}', check file exist.")
    except PermissionError:
        print("Permission denied")

# Main loop
def main():
    curr_time = f"[{TIME.strftime("%Y-%m-%d %H:%M:%S")}]"
    while True:
        print("\nLog APP\n")
        print("1. Create Log.")
        print("2. View Logs.")
        print("3. Delete Logs.")
        print("4. Exit.\n")
        choice = input("Select choice: ")
        if choice in ["1","2","3","4"]:
            match choice:
                case "1":
                    user_log = input("\nUser input: ")
                    user_category = input("Choose category: ").upper()
                    if len(user_log) < 1 and len(user_category) < 1:
                        print("Message and category can't be empty.")
                        continue
                    else:
                        message_log = f"Written to file as: {curr_time} [{user_category}] {user_log}"
                        try:
                            file_operation('log.txt', 1, message_log)
                        except Exception as e:
                            print(e)
                case "2":
                    messages = file_operation('log.txt', 0)
                    print(messages) if messages else print("No logs found.")
                case "3":
                    with open('log.txt', 'w') as file:
                        file.close()
                        pass
                    print("Log Cleared.")
                case "4":
                    break
        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()