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


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s)==str
    firstQuote = introcs.find_str(s, '"')
    secondQuote = introcs.find_str(s,'"',firstQuote+1)
    assert firstQuote > -1 and secondQuote > -1
    return s[firstQuote+1:secondQuote]


