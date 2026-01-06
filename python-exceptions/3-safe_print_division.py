#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return print("Inside result: ",c)
    except(ValueError):
        return print("Inside result: None")
