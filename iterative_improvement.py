def improve(update, close, guess=1):
    """a general function keeps updating a number
       based on two func parameters """
    while not close(guess):
        guess = update(guess)
    return guess


def approximate_equal(x, y, tolerance=1e-3):
    """ true if the absolute difference between the two params less than the tolerance"""
    return abs(x-y) < tolerance


def golden_ratio_update(guess):
    return (1 / guess) + 1


def golden_ratio_close(guess):
    return approximate_equal(guess * guess, guess + 1)


def golden_ratio_test():
    print("golden ratio: {}".format(improve(golden_ratio_update, golden_ratio_close)))


def sqrt(a):
    # functions will extend its local environment
    # to its parent environments when they are called
    # the functions average, square_update, square_close can see
    # a and each other, because these names are in its parent environment(sqrt)
    def average(x, y):
        return (x + y) / 2

    def square_update(guess):
        return average(guess, a/guess)

    def square_close(guess):
        return approximate_equal(guess * guess, a)
    return improve(square_update, square_close)


def sqrt_test():
    result = sqrt(256)
    print("square root of 256: {}".format(result))


def newton_update(f, df):
    def update(guess):
        return guess - f(guess)/df(guess)  # get the next point
    return update


def newton_close(f):
    def close(guess):
        return approximate_equal(f(guess), 0)
    return close


def newton_square(num):

    def f(x):        # function value at point x
        return x * x - num

    def df(x):       # derivative of function at point x
        return 2 * x

    return improve(newton_update(f, df), newton_close(f))


def newton_cube(num):

    def f(x):
        return x * x * x - num

    def df(x):
        return 3 * x * x

    return improve(newton_update(f,  df), newton_close(f))


def newton_test():
    square_root_of49 = newton_square(49)
    print("square root of 49 is {}".format(square_root_of49))
    cubic_root_of27 = newton_cube(27)
    print("cubic root of 27 is {}".format(cubic_root_of27))

# initially, I write the following code, its not elegant at all
# although it has the sam functionality
# I hard coded the numbers, these numbers can be used as closure like
# I did in the above refactored code.


# def square(x):            # can be replaced by lambda
#     return x * x - 49
#
#
# def square_df(x):
#     return 2 * x
#
#
# def cube(x):
#     return x * x * x - 27
#
#
# def cube_df(x):
#     return 3 * x * x
#
#
# def newton_test():
#     square_root_of49 = improve(newton_update(square, square_df), newton_close(square))
#     print("square root of 49 is {}".format(square_root_of49))
#     cubic_root_of27 = improve(newton_update(cube, cube_df), newton_close(cube))
#     print("cubic root of 27 is {}".format(cubic_root_of27))


if __name__ == "__main__":
    golden_ratio_test()
    sqrt_test()
    newton_test()
