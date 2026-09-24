import re
from collections import Counter


def count_word_frequency(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    words = re.findall(r"[а-яёa-z]+", text.lower())
    return Counter(words)


if __name__ == "__main__":
    freq = count_word_frequency("test.txt")
    for word, count in freq.most_common():
        print(f"{word}: {count}")
