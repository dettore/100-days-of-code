#!/usr/bin/env python3

import math


# Check if a given string is a palindrome

# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards

# Examples: madam and racecar

# TODO: make a list of words and loop through them

letters = "madam"


if __name__ == "__main__":
    if letters == letters[::-1]:
        print(f"{letters} is a palindrome")
    else:
        print(f"{letters} is not a palidrome")
