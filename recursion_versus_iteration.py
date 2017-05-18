
""" most of the time, recursion functions can be replaced by iteration
    the following function pairs are some of them I implemented
"""


def sum_of_digits_recur(num):
    """ return the sum of all decimal digits using recursion"""
    if num // 10 == 0:    # base case
        return num
    else:
        return sum_of_digits_recur(num // 10) + num % 10


def sum_of_digits_iter(num):
    """ returns the sum of all decimal digits using iteration"""
    total = 0  # total stores intermediate sum
    while num // 10 != 0:
        total += num % 10
        num //= 10
    return total + num


def sum_of_digits_test():
    print(sum_of_digits_recur(12345))
    print(sum_of_digits_iter(12345))


def is_even_recur(num):
    """ return true if the parameter is even number using recursion"""
    if num == 0:             # base case
        return True
    else:
        return not is_even_recur(num-1)


def is_even_iter(num):
    """ return true if the parameter is even number using iteration"""
    result, i = True, 0   # base case, 0 is even number
    i += 1
    while i <= num:
        result = not result    # switch the result, n and n-1 is opposite of each other
        i += 1
    return result


def is_even_test():
    print("7 is even? ", is_even_recur(7))
    print("7 is even? ", is_even_iter(7))
    print("100 is even? ", is_even_recur(100))
    print("100 is even? ", is_even_iter(100))
    print("0 is even? ", is_even_recur(0))
    print("0 is even? ", is_even_iter(0))


def factorial_recur(num):
    """calculate factorial of num using recursion"""
    if num == 1:
        return 1
    else:
        return num * factorial_recur(num - 1)


def factorial_iter(num):
    """calculate factorial of num using iteration"""
    result, i = 1, 1
    while i <= num:
        result *= i
        i += 1
    return result


def factorial_test():
    print("factorial of 5", factorial_recur(5))
    print("factorial of 5", factorial_iter(5))


def fibonacci_recur(num):
    """calculates fibonacci of number using recursion"""
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)


def fibonacci_iter(num):
    """calculates fibonacci of number using iteration"""
    pre, cur, i = 1, 1, 3
    while i <= num:
        # this is idiomatic python, right hand expressions will be evaluated first
        # before the assignment
        pre, cur = cur, pre + cur
        i += 1
    return cur


def fibonacci_test():
    print("fibonacci of 7: ", fibonacci_recur(7))
    print("fibonacci of 7: ", fibonacci_iter(7))

if __name__ == "__main__":
    sum_of_digits_test()
    is_even_test()
    factorial_test()
    fibonacci_test()