VOWELS = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", 
          "a", "e", "i", "o", "u", "y"]


def count_vowels(word, vowels=VOWELS):
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(count_vowels("young"))
    print(count_vowels("Молодой"))
