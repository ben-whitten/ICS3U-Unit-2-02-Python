#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find the area and perimeter or a rectangle.


# This is what finds the area and perimeter of the rectangle.
# Replace numbers on lines 11 and 12 with the dimensions of the rectangle.

dimension_1 = 2
dimension_2 = 18


def main():
    print("If a rectangle has the dimensions:")
    print(dimension_1, "cm x", dimension_2, "cm")
    print("")
    print("Then the area is {}cm^2" .format(dimension_1*dimension_2))
    print("and the perimeter is {}cm" .format(2*(dimension_1+dimension_2)))


if __name__ == "__main__":
    main()
