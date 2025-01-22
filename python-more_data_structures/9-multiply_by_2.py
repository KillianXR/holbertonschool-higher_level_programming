#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdictionnary = a_dictionary.copy()
    for travel, age in newdictionnary.items():
        newdictionnary[travel] = age * 2
    return newdictionnary
