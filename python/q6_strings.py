import logging
from logger import setup_logger
setup_logger()
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.DEBUG)  # sets the logging level for this script


# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

    if count >= 10:
        ret_value = 'Number of donuts: many'
    else:
        ret_value = 'Number of donuts: ' + str(count)
    return ret_value


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        ret_value = ''
    else:
        ret_value = s[0:2] + s[len(s)-2:]
    return ret_value


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_character = s[0]
    new_string = ""
    skip_count = 0
    for letter in s:
        if letter == first_character and skip_count == 0:
            skip_count += 1
            new_string += letter
        elif letter == first_character and skip_count >= 1:
            new_string += "*"
        else:
            new_string += letter
    return new_string


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    return b[0:2] + a[2:] + " " + a[0:2] + b[2:]


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if s[len(s)-3:] == "ing":
        ret_value = s + "ly"
    elif len(s) >= 3:
        ret_value = s + "ing"
    else:
        ret_value = s
    return ret_value


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    not_index = s.find("not")
    bad_index = s.find("bad")
    if bad_index > not_index:
        new_string = s[0:not_index] + "good" + s[bad_index + len("bad"):]
        return new_string
    else:
        return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    def evaluate_front(word):
        """
        Gets the proper front half of a word
        :param word:
        :return: part_front
        """
        if len(word) % 2 == 0:
            part_front = word[0:int(len(word)/2)]
        else:
            part_front = word[0:int(len(word)/2)+1]
        return part_front

    def evaluate_back(original, front_word):
        """
        Gets the proper back half of a word
        :param original:
        :param front_word:
        :return: back_half of a word
        """
        return original[original.find(front_word[-1])+1:]

    a_front = evaluate_front(a)
    b_front = evaluate_front(b)
    a_back = evaluate_back(a, a_front)
    b_back = evaluate_back(b, b_front)
    return a_front + b_front + a_back + b_back
