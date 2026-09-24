def get_factorial(number):
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    print(get_factorial(5))
    print(get_factorial(10))