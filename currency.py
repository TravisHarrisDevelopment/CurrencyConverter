"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Travis Harris
Date:   April 14, 2023
"""

import introcs
from myconfig import *

#APIKEY = 'cprwwbIIcuf2ImJsxrUAUxEgql3Zv0pucTJb15ruErAe'
print(APIKEY)

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s)==str
    found = ' ' in s
    assert found == True

    spaceIndex = introcs.find_str(s, ' ')
    return s[0:spaceIndex]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s)==str
    found = ' ' in s
    assert found == True

    spaceIndex = introcs.find_str(s, ' ')
    return s[spaceIndex+1:]
