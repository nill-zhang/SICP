def replace_with_sum(lst1):
    """replaces each element of a list with the sum of the
       two largest numbers after it. Use -1 if there are not enough numbers"""
    def sum_rest(lst2):
        lst2.sort()              # list.sort() returns none and makes changes in place
        return sum(lst2[-2:])
    for i in range(len(lst1)):
        if len(lst1)-i <= 2:
            lst1[i] = -1
        else:
            lst1[i] = sum_rest(lst1[i+1:])


def replace_with_sum_test():
    a = [10, 9, 8, 7, 6, 5, 4]
    replace_with_sum(a)
    assert a == [17, 15, 13, 11, 9, -1, -1]   # because I did the change in-place


def matrix_product(matrix1, matrix2):
    """ multiplies two matrices A and B together"""
    # todo add evaluation make sure the two params are matrices
    def sum_of_vector(list1, list2):
        return sum([list1[j] * list2[j] for j in range(len(list1))])
    total = 0
    for i in range(len(matrix1)):
        lst2 = [lst[i] for lst in matrix2]
        total += sum_of_vector(matrix1[i], lst2)
    return total


def matrix_product_test():
    a = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
    b = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(matrix_product(a, b))
    assert matrix_product(a, b) == 70, "matrix_product_test failed"


def reverse(lst):
    def f(x):
        return lst[len(lst)-1-lst.index(x)]
    return list(map(f, lst))


def reverse_test():
    a = [1, 2, 3, 4, 5, 6, 7]
    assert reverse(a) == [7, 6, 5, 4, 3, 2, 1]
    print(a)
    print(reverse(a))










if __name__ == "__main__":
    replace_with_sum_test()
    matrix_product_test()
    reverse_test()

