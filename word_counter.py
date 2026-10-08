from collections import Counter
import string

print("===== WORD COUNTER =====")

filename = input("Enter the text file name: ")

try:
    with open(filename, "r") as file:
        text = file.read().lower()

    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    word_frequency = Counter(words)

    print("\nTotal number of words:", len(words))
    print("\nWord Frequency:")

    for word, count in word_frequency.items():
        print(word, ":", count)

except FileNotFoundError:
    print("File not found. Please check the file name.")