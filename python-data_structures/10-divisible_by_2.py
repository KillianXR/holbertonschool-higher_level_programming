#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return (None)

    else:
        new_list = list(my_list)
        for count in range(len(my_list)):
            if my_list[count] % 2 == 0:
                new_list[count] = True
            else:
                new_list[count] = False
        return new_list
