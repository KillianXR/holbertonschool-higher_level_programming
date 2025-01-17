#!/usr/bin/python3
for ascii in range(0, 100):
    if ascii < 10:
        print("0{}, ".format(ascii), end="")
    else:
        print("{}, ".format(ascii), end="")
