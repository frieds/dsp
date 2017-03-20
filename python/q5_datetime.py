from datetime import datetime

# a)
a_date_start = '01-02-2013'
a_date_stop = '07-28-2015'

# b)
b_date_start = '12312013'
b_date_stop = '05282015'

# c)
c_date_start = '15-Jan-1994'
c_date_stop = '14-Jul-2015'


def days_between(two_dates, original_date_format):
    """
    Converts list of two dates into datetime objects from their original date format and returns the dates' difference
    :param two_dates: list with two dates
    :param original_date_format: C library’s strftime() format
    :return: absolute difference between two dates in days
    """
    dates = []
    for date in two_dates:
        dates.append(datetime.strptime(date, original_date_format))
    return abs((dates[1]-dates[0]).days)

print("Days between 'a' dates: {0}".format(days_between([a_date_start, a_date_stop], "%m-%d-%Y")))
print("Days between 'b' dates: {0}".format(days_between([b_date_start, b_date_stop], "%m%d%Y")))
print("Days between 'c' dates: {0}".format(days_between([c_date_start, c_date_stop], "%d-%b-%Y")))