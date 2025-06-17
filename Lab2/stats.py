def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2

def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    for key in frequency:
        if frequency[key] == max_freq:
            return key  # Return the first mode encountered

def main():
    # Sample list for testing
    sample = [4, 1, 2, 2, 3, 5, 4, 4]
    print("Sample List:", sample)
    print("Mean:", mean(sample))
    print("Median:", median(sample))
    print("Mode:", mode(sample))

if __name__ == "__main__":
    main()