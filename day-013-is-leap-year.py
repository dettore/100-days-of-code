#!/usr/bin/env python3

import calendar

# Check if a year is a leap year.

year = 2024

if __name__ == "__main__":
    if calendar.isleap(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
