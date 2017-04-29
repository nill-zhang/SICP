# /usr/env/python
# -*-coding:utf-8-*-
from operator import add


def keep_if(f, seq):
    """ keep_if filters those elements in seq
        which makes f true, return them in a list
        """

    return [x for x in seq if f(x)]


def map_all(f, seq):
    """ map_all apply each elements in seq by f and return
        a list contains those results
        """
    return [f(x) for x in seq]


def reduce(oper, seq, init):
    """high order function reduce reduces sequence seq
       through calling oper repeatedly
       """
    reduced = init
    for x in seq:
        reduced = oper(reduced, x)
    return reduced


def divisors(n):
    """
    divisors returns a list of positive integers which can be divided by n
    """
    return [x for x in range(1, n) if n % x == 0]


def test():
    fmtStr = "the sum of 45's divisors{0} is {1}"
    print(fmtStr.format(divisors(45), reduce(add, divisors(45), 0)))
    # calculate minimum perimeter of a rectangle with integer side lengths, given its area
    perimeters = [2*(x+864//x) for x in divisors(864) if x*x <= 864]
    print(divisors(864), "\n", perimeters)
    minPerimeter = reduce(min, perimeters[1:], perimeters[0])
    fmtStr = "the minimum perimeter of this rectangle is {0}"
    print(fmtStr.format(minPerimeter))


if __name__ == '__main__':
    test()


