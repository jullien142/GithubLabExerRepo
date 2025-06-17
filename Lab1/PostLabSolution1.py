# stats_cli.py

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def get_numbers():
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        try:
            return [float(num) for num in user_input.strip().split()]
        except ValueError:
            print("❌ Invalid input. Please enter only numbers.\n")

def main():
    print("📊 Welcome to the Stats Calculator 📊")
    numbers = get_numbers()

    while True:
        print("\nWhat would you like to do?")
        print("1 - Calculate Mean")
        print("2 - Calculate Median")
        print("3 - Calculate Mode")
        print("4 - Enter New Numbers")
        print("5 - Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print(f"✅ Mean: {mean(numbers)}")
        elif choice == "2":
            print(f"✅ Median: {median(numbers)}")
        elif choice == "3":
            result = mode(numbers)
            print(f"✅ Mode: {result}")
        elif choice == "4":
            numbers = get_numbers()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
