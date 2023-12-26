#!/usr/bin/env python3

# Count the number of vowels in a string

word = "winter"
vowels = ["a", "e", "i", "o", "u"]

# TODO: count the number of repeated vowels

if __name__ == "__main__":
    letters = list(word)
    common = list(set(letters).intersection(vowels))
    number_of_vowels = len(common)

    print(f"The number of vowels in {word} is {number_of_vowels}")
