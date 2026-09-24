import random


def guess_the_number():
    print(
        "Это игра «Угадай число»!\n"
        "Я загадываю число от 1 до 100, а вам необходимо отгадать.\n"
        "После каждой попытки я буду говорить, "
        "ваше число больше или меньше загаданного."
    )
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Нужно ввести целое число.")
            continue

        attempts += 1
        if guess > number:
            print("Ваше число больше загаданного")
        elif guess < number:
            print("Ваше число меньше загаданного")
        else:
            print(f"Вы угадали! Число попыток: {attempts}")
            break


if __name__ == "__main__":
    guess_the_number()
