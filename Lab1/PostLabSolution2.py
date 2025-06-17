def read_file(filename):
    """
    Attempts to open and read the specified file.
    Returns a list of lines from the file if successful; otherwise, returns None.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def prompt_line_number(max_lines):
    """
    Prompts the user for a line number.
    Returns an integer line number, or None if input is invalid.
    """
    user_input = input(f"Enter a line number [1-{max_lines}, 0 to quit]: ")
    if user_input == '0':
        return 0
    try:
        number = int(user_input)
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def main():
    """
    Main function that handles file input and user interaction.
    Displays specific lines from the file based on user input.
    """
    filename = input("Enter the input file name: ")
    lines = read_file(filename)

    if lines is None:
        return  # Exit if file could not be read

    total_lines = len(lines)
    print(f"\nThe file has {total_lines} lines.")

    while True:
        choice = prompt_line_number(total_lines)

        if choice == 0:
            print("Exiting program.")
            break
        elif choice is None:
            continue  # Invalid input, retry
        elif 1 <= choice <= total_lines:
            print(f"{choice}: {lines[choice - 1].strip()}\n")
        else:
            print(f"Line number must be between 1 and {total_lines}.")

if __name__ == "__main__":
    main()
