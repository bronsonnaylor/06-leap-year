# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap(year):
    bool = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return bool

from test import testEqual

testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
