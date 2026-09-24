def find_min_in_list(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


if __name__ == "__main__":
    print(find_min_in_list([35, 4, 6, 10, 5]))
    print(find_min_in_list([5925, 83, 5792, 930, 253, 5903, 592]))
