#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program generate random number and find the smallest


import random


def smallest_number(numbers):
    # This is finds smallest number in a list

    last_number = 100

    for number in numbers:
        if number < last_number:
            smallest = number
            last_number = number

    return smallest


def main():
    # This is generate 10 random numbers
    smallest = 0

    # This is a list holding the random numbers
    numbers = []

    # process
    for repeater in range(0, 10):
        number = random.randint(0, 100)
        numbers.append(number)
        # output
        print(numbers[repeater])

    smallest = smallest_number(numbers)

    # output
    print("The smallest number is " + str(smallest))


if __name__ == "__main__":
    main()
