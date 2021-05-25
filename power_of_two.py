#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 25, 2021
# This program asks the user to input a number and then
# displays the square of all numbers from 0 to that number

def main():
    # ask the user to input a whole number
    number_as_string = input("Enter a whole number: ")

    try:
        # convert from string to integer
        number_as_int = int(number_as_string)

        if (number_as_int < 0):
            # check if number is negative
            print("{} is not a whole number.". format(number_as_int))
        else:
            # calculate the square of the numbers in range
            for counter in range(number_as_int + 1):
                square = counter ** 2
                print("{0}^2 = {1}". format(counter, square))
                counter = counter + 1

    except ValueError:
        # error message
        print("{} is not a whole number.". format(number_as_string))


if __name__ == "__main__":
    main()
