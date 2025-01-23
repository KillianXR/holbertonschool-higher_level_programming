#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    bigger_contenair = None
    bigger_containt = 0

    for contenair, containt in a_dictionary.items():
        if containt > bigger_containt:
            bigger_containt = containt
            bigger_contenair = contenair
    return bigger_contenair
