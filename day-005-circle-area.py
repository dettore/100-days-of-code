#!/usr/bin/env python3

import math

# Calculate the area of a circle
# area = pi * (radius**2)

if __name__ == "__main__":
    radius = 3
    pi = math.pi
    area = pi * (radius**2)

    print('Area: ' + str(round(area, ndigits=2)) + ' meters squared.')
