#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [[number, replace][number == search]for number in my_list]
