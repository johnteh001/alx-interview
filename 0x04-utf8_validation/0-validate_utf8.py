#!/usr/bin/python3
"""UTF-8 Validator"""


def validUTF8(data):
    """Function validates utf-8"""
    counter = 0
    for elem in data:
        if counter == 0:
            if elem & 128 == 0:
                counter = 0
            elif elem & 224 == 192:
                counter = 1
            elif elem & 240 == 224:
                counter = 2
            elif elem & 248 == 240:
                counter = 3
            else:
                return False
        else:
            if elem & 192 != 128:
                return False
            counter -= 1
    if counter == 0:
        return True
    return False
