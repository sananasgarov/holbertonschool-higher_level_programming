#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = value / 1
        print(value)
    except:
        print("{} is not an integer".format(value))
