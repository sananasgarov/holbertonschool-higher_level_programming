#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    t = []
    for x in my_list:
        if x % 2 == 0:
            t.append(True)
        if x % 2 != 0:
            t.append(False)
    return t
