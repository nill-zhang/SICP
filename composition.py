
def compound1(func1, func2, func3):
    def wrap(x):
        return func1(func2(func3(x)))
    return wrap


def compound2(prompt):
    def square(x):
        print(prompt)
        return x * x

    def triple(x):
        print(prompt)
        return 3 * x

    def inc(x):
        print(prompt)
        return x + 1
    # define local functions
    # use the global compound 1 to do calculation
    return compound1(inc, triple, square)


def inc(x):
    print()
    return x + 1


def square(x):
    return x * x


def triple(x):
    return 3 * x


def compound_test():
    # let construct f(x) = 3*power(x,2) + 1
    y = compound1(inc, triple, square)
    print(y(6))
    print("#" * 80)
    z = compound2("inside compound2")
    print(z(6))
    print("#" * 80)


def curry(a):
    def takeb(b):
        def takec(c):
            def taked(d):
                def takee(e):
                    return sum([a, b, c, d, e])
                return takee
            return taked
        return takec
    return takeb


def curry1(f):
    """takes a function f, return function g,  g(x)(y)(z) == f(x, y, z)"""
    def g(x):
        def h(y):
            def k(z):
                return f(x, y, z)
            return k
        return h
    return g


def uncurry1(f):
    """takes a function f, returns function g, g(x, y, z) == f(x)(y)(z)"""
    def g(x, y, z):
        return f(x)(y)(z)
    return g


def curry_test():
    summation = curry(1)(2)(3)(4)(5)
    print(summation)
    curry1(print)("a")("b")("c")
    uncurry1(curry1(print))("a", "b", "c")


if __name__ == "__main__":
    compound_test()
    curry_test()