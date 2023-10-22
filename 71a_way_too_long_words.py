#!/usr/bin/python3

number_of_words = int(input())
words = []

for i in range(number_of_words):
    word = input()
    words.append(word)

for word in words:
    if len(word) <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
