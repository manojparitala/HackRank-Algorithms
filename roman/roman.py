'''
In Roman numerals, there are seven characters that are repeated and combined in various ways to represent numbers.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

for more information about roman numericals go to http://www.diveintopython3.net/regular-expressions.html#romannumerals
'''
class Roman(object):
    roman_numeral_map = (('M', 1000),
                         ('CM', 900),
                         ('D', 500),
                         ('CD', 400),
                         ('C', 100),
                         ('XC', 90),
                         ('L', 50),
                         ('XL', 40),
                         ('X', 10),
                         ('IX', 9),
                         ('V', 5),
                         ('IV', 4),
                         ('I', 1))

    def to_roman(self, n):
        if not ((n < 4000) and (n > 0)) :
            raise OutOfRangeError('number should be in range of 1 to 3999')

        if isinstance(n, float):
            raise NotIntegerError('number should be an integer') 

        result = ''
        for numeral, integer in Roman.roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result

class OutOfRangeError(Exception):
    pass

class NotIntegerError(Exception):
    pass
