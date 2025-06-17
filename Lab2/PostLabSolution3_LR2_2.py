def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return

    total_lines = len(lines)
    print(f"The file has {total_lines} lines.")

    while True:
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if line_number == 0:
            print("Exiting program.")
            break
        elif 1 <= line_number <= total_lines:
            print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
        else:
            print(f"Invalid line number. Please enter a number between 1 and {total_lines}.")


if __name__ == "__main__":
    main()
