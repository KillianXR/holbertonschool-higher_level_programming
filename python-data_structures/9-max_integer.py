#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        top = my_list[0]
        for count in range(len(my_list)):
            if my_list[count] > top:
                top = my_list[count]
    return (top)
