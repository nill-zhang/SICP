from math import gcd
"""
An abstraction barrier violation occurs whenever a part of the program
that can use a higher level function instead uses a function in a lower level.
For example, a function that computes the square of a rational number is best implemented
in terms of mul_rational, which does not assume anything about the implementation
of a rational number.

Abstraction barriers make programs easier to maintain and to modify.
The fewer functions that depend on a particular representation,
the fewer changes are required when one wants to change that representation.
All of these implementations of square have the correct behavior,
but only the first is robust to future changes.
The square function would not require updating even if we altered
the representation of rational numbers. By contrast, square_bad
would need to be changed whenever the selector or constructor signatures changed,
and square_toobad would require updating whenever the implementation of rational numbers changed

"""


def rational(nume, denom):
    g = gcd(nume, denom)
    return nume//g, denom//g


def numerator(num):
    return num[0]


def denominator(num):
    return num[1]


def multiply(rat1, rat2):
    new_nume = numerator(rat1)*numerator(rat2)
    new_denom = denominator(rat1)*denominator(rat2)
    return rational(new_nume, new_denom)


def add(rat1, rat2):
    new_nume = numerator(rat1) * denominator(rat2) + (numerator(rat2) * denominator(rat1))
    new_denom = denominator(rat1) * denominator(rat2)
    return rational(new_nume, new_denom)


def equal(rat1, rat2):
    return numerator(rat1) * denominator(rat2) == numerator(rat2) * denominator(rat1)


def string(rat):
    return numerator(rat) + "/" + denominator(rat)


def square(rat):
    return multiply(rat, rat)


def square_bad(rat):
    new_nume = numerator(rat) * numerator(rat)
    new_denom = denominator(rat) * denominator(rat)
    return rational(new_nume, new_denom)


def square_toobad(rat):
    return rational(rat[0] * rat[0], rat[1] * rat[1])


def square_veryverybad(rat):
    new_nume = rat[0] * rat[0]
    new_denom = rat[1] * rat[1]
    g = gcd(new_nume, new_denom)
    return new_nume//g, new_denom//g


def rational_test():
    a = rational(2, 14)
    b = rational(4, 7)
    print("rational a:{0}, rational b:{1}".format(a, b))
    print("multiply {0} by {1} :{2}".format(a, b, multiply(a, b)))
    print("add {0} and {1}: {2}".format(a, b, add(a, b)))
    print("{0} == {1} ? {2} ".format(a, b, equal(a, b)))
    print("square of {0}: {1}".format(b, square(b)))
    print("square of {0}: {1}".format(b, square_bad(b)))
    print("square of {0}: {1}".format(b, square_toobad(b)))
    print("square of {0}: {1}".format(b, square_veryverybad(b)))


if __name__ == "__main__":
    rational_test()

# we can make it more abstract instead of using tuple

# def rational(nume, denom):
#     g = gcd(nume, denom)
#     return pair(nume//g, denom//g)
#

# def pair(x, y):
#     def getitem(i):
#         if i == 0:
#             return x
#         elif i == 1:
#             return y
#     return getitem
#
#
# def select(f, index):
#     return f(index)
#
#
# def numerator(rat):
#     return select(rat, 0)
#
#
# def denominator(rat):
#     return select(rat, 1)

