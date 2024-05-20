#!/usr/bin/python3
'''
This script determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Returns True if data is a valid UTF-8 encoding, else return False
    '''

    try:
        byte_data = bytes(data)
        byte_data.decode('utf-8')
        return True
    except ValueError:
        return False
