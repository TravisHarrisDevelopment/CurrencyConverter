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


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    srcStart = introcs.find_str(json, 'src":')
    #print(srcStart)
    substring = first_inside_quotes(json[srcStart+5:])
    #print(substring)
    return substring


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    dstStart = introcs.find_str(json, 'dst":')
    #print(srcStart)
    substring = first_inside_quotes(json[dstStart+5:])
    #print(substring)
    return substring
