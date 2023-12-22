#!/usr/bin/env python3

# Find the largest of three numbers.

# TODO: use rand to generate list

nums = [23, 45, 4]

if __name__ == "__main__":
    nums.sort()  # sort the list of numbers
    print(str(nums[-1]))
