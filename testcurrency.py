"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Travis Harris
Date:   April 14, 2023
"""

import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")
       
    result = currency.before_space("hello world")
    introcs.assert_equals('hello', result)

    result = currency.before_space('a b c')
    introcs.assert_equals('a', result)

    result = currency.before_space('  ')
    introcs.assert_equals('', result)

    result = currency.before_space(' ')
    introcs.assert_equals('', result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    result = currency.after_space("hello world")
    introcs.assert_equals('world', result)

    result = currency.after_space('a b c')
    introcs.assert_equals('b c', result)

    result = currency.after_space('   ')
    introcs.assert_equals('  ', result)

    result = currency.after_space(' ')
    introcs.assert_equals('', result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "B C" D E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "" "D')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes('"A  D"')
    introcs.assert_equals('A  D', result)   


def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')

    result = currency.get_src('{"success": true, "src": "2 United States ' + 
        'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)   

    result = currency.get_src('{"success":false,"src":"","dst":"","error":' +
        '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_src('{"success":true, "src":"2 United States' +
        ' Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src('{"success":false,"src": "","dst":"","error":' +
        '"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')

    result = currency.get_dst('{"success": true, "src": "2 United States ' + 
        'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)   

    result = currency.get_dst('{"success":false,"src":"","dst":"","error"' +
        ':"Source currency code is invalid."}')
    introcs.assert_equals('', result)   

    result = currency.get_dst('{"success": true, "src":"2 United States ' + 
        'Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)   

    result = currency.get_dst('{"success":false,"src":"","dst": "","error"' +
        ':"Source currency code is invalid."}')
    introcs.assert_equals('', result)  


def test_has_error():
    """Test procedure for has_error"""
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    print('Testing has_error')

    result = currency.has_error('{"success": true, "src": "2 United States ' + 
        'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)  

    result = currency.has_error('{"success":false,"src":"","dst":"","error"' +
        ':"Source currency code is invalid."}')
    introcs.assert_true(result)   

    result = currency.has_error('{"success":true, "src":"2 United States ' + 
        'Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(result)   

    result = currency.has_error('{"success": false,"src": "","dst": "","error"' +
        ': "Source currency code is invalid."}')
    introcs.assert_true(result)  


def test_service_response():
    """Test procedure for service_response"""
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    print('Testing service_response')

    result = currency.service_response('USD','EUR', 2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United ' + 
        'States Dollars", "dst": "2.2160175 Euros", "error": ""}', result)
    
    result = currency.service_response('AAA', 'BBB', 2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":' + 
        ' "The rate for currency AAA is not present."}', result)
    
    result = currency.service_response('USD', 'BBB', -2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":' + 
        ' "The rate for currency BBB is not present."}', result)
    
    result = currency.service_response('EUR','USD', -2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 Euros", "dst": ' + 
        '"-2.8203748390976155 United States Dollars", "error": ""}', result)
    

def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')

    introcs.assert_true(currency.iscurrency('USD'))
    introcs.assert_false(currency.iscurrency('AAA'))


def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')

    result = currency.exchange('USD', 'EUR', 2.5)
    introcs.assert_floats_equal(2.2160175, result)
    
    result = currency.exchange('USD', 'EUR', -2.5)
    introcs.assert_floats_equal(-2.2160175, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully")