"""
Built-in Functions: 

    ord()
        Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
    str.join(iterable)
        Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.
    .lower()
        Python string method lower() returns a copy of the string in which all case-based characters have been lowercased.
    .isalpha()
        Python string method isalpha() checks whether the string consists of alphabetic characters only.
        - Return Value:
            This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.

"""


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())



print("The sunset sets at twelve o' clock. = " +alphabet_position("The sunset sets at twelve o' clock."))
print("The narwhal bacons at midnight. = " + alphabet_position("The narwhal bacons at midnight."))

