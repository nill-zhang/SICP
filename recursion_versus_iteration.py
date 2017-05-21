
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


def greatest_common_divisor_recur(num_a, num_b):
    """ calculates the greatest common divisor using recursion"""
    if num_a % num_b == 0:
        return num_b
    else:
        num_a, num_b = num_b, num_a % num_b
        return greatest_common_divisor_recur(num_a, num_b)


def greatest_common_divisor_iter(num_a, num_b):
    """ calculates the greatest common divisor using iteration"""
    while num_a % num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return num_b


def gcd_test():
    print("the gcd of %d and %d is %d" % (93, 31, greatest_common_divisor_recur(93, 31)))
    print("the gcd of %d and %d is %d" % (81, 126, greatest_common_divisor_recur(81, 126)))
    print("the gcd of %d and %d is %d" % (93, 31, greatest_common_divisor_iter(93, 31)))
    print("the gcd of %d and %d is %d" % (81, 126, greatest_common_divisor_iter(81, 126)))


def base_converter_recur(num, base):
    assert base in range(1, 17), "base should be in the range [1, 16]"
    # I don't want mapping to be defined and used in
    # every recursion, so I defined it in the high
    # order function and make it visible through closure
    # all the recursions can use it.
    mapping = "0123456789ABCDEF"

    def f():

        if num // base == 0:                                   # base case, I did not use nonlocal, why?
            yield mapping[num % base]
        else:
            yield from base_converter_recur(num//base, base)   # this will resolve to base case eventually
            yield mapping[num % base]
    return ''.join(f())                                        # concatenate the generator


def base_converter_iter(num, base):

    assert base in range(1, 17), "base should be in the range [1, 16]"
    mapping = "0123456789ABCDEF"

    def f():
        nonlocal num                  # use the outside num
        while num // base != 0:
            yield mapping[num % base]
            num = num // base
        yield mapping[num % base]
    return "".join(list(f())[::-1])      # reverse and then concatenate the generated list


def base_converter_test():
    result1 = base_converter_recur(65501, 16)
    result2 = base_converter_iter(65501, 16)
    result3 = base_converter_recur(248, 2)
    result4 = base_converter_iter(248, 2)
    result5 = base_converter_recur(23412548, 10)
    result6 = base_converter_iter(23412548, 10)
    print("result1: ", result1)
    print("result2: ", result2)
    print("result3: ", result3)
    print("result4: ", result4)
    print("result5: ", result5)
    print("result6: ", result6)


def prime(n):
    """ get the all the prime numbers less than n"""
    from math import floor, sqrt
    for i in range(2, n+1):
        for j in range(2, floor(sqrt(i)+1)):
            if i % j == 0:
                break
        else:            # enter else clause when loop terminates normally
            yield i


def prime_test():
    print("prime numbers less than 30: \n", ' '.join(map(str, prime(30))))


if __name__ == "__main__":
    sum_of_digits_test()
    is_even_test()
    factorial_test()
    fibonacci_test()
    gcd_test()
    prime_test()
    base_converter_test()