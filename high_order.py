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
    print("before: ", a)
    replace_with_sum(a)
    print("after: ", a)


def matrix_product(2dlst1, 2dlst2):

    assert len(2dlst1[0]) == len(2dlst2)




if __name__ == "__main__":
    replace_with_sum_test()