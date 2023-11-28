#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    print(number % 10, end="")
    last_digit = number % 10
    return last_digit
