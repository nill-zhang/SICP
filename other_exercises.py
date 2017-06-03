import copy

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
    """reverses a list"""
    def f(x):
        return lst[len(lst)-1-lst.index(x)]
    return list(map(f, lst))


def reverse_test():
    a = [1, 2, 3, 4, 5, 6, 7]
    assert reverse(a) == [7, 6, 5, 4, 3, 2, 1]
    print(a)
    print(reverse(a))


def permutation(lst):
    """return a list of all permutations of the provided lst."""
    if len(lst) == 1:
        # base case, if only one element exists, there is only one permutation for the list
        return [lst]
    else:
        # make a deep copy of the previous permutation result
        cpy = [copy.deepcopy(p) for p in permutation(lst[1:])]
        perm = []
        for j in range(len(lst)):
            # make len(lst) deep copies of the previous permutation
            # because each permutations in the previous result
            # has a length of len(lst[1:]), so it has len(lst[1:])+1 ways
            # to insert the new element, for each permutation, add a new
            # element will generate len(lst[1:])+1 new permutations
            # len(lst[1:])+1 = len(lst)
            perm.extend(copy.deepcopy(cpy))
        for i in range(len(perm)):
            # for the first group of previous permutation, insert the new element at index 0
            # for the second group of previous permutation, insert the new element at index 1
            # ......
            perm[i].insert((i // len(perm[i])), lst[0])
        return perm


def permutation_test():
    a = [1, 2, 3]
    b = permutation(a)
    print(b)
    assert b == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1]], "permutation_test failed"


def pizza_distributor(tpl):
    """given a tuple of numbers, which represent the sizes of pizza slices,
       distributes the slices among two people as even as possible"""
    tpl = list(tpl)
    tpl.sort()
    # get the first half of the sorted pizza slices list
    fhalf = [tpl[i] for i in range(len(tpl)//2)]
    # get the second half of the list
    shalf = [tpl[i] for i in range(len(tpl)//2, len(tpl))]
    fswapping_element = -1
    sswapping_element = -2

    def rebalance(lst1, lst2):
        """moves the minimum element from lst1 to lst2"""
        swapping_element = lst1.pop()
        lst2.append(swapping_element)
        lst2.sort()
        lst2.reverse()
        return swapping_element

    while True:
        # first half and second half have the same size
        if sum(fhalf) == sum(shalf):
            break
        # second half is greater than the first half
        # need to move the minimum element from second half to first half
        elif sum(shalf) > sum(fhalf):
            sswapping_element = rebalance(shalf, fhalf)
        # on the contrary, move a minimum element from first half to second half
        else:
            fswapping_element = rebalance(fhalf, shalf)

        # means that there is no need to further rebalance the two groups
        # if what had been swapped is swapped back
        if sswapping_element == fswapping_element:
            break
    return tuple(fhalf), tuple(shalf)


def pizza_distributor_test():
    a = (2, 4, 6, 1, 8, 9, 10, 7, 15, 8)
    Alice, Bob = pizza_distributor(a)
    print("Alice got: ", Alice)
    print("Bob   got: ", Bob)
    assert sum(Alice) == 35, "pizza_divider_test failed"


def stair(num):
    """return number of ways to walk n steps, if you can choose to take 1 or 2
    steps at a time"""
    if num <= 2:
        return num
    if num == 3:
        return 4
    else:
        return stair(num-1)+stair(num-2)+stair(num-3)


def stair_test():
    a = stair(5)
    b = stair(10)
    print("{} ways to climb 5 steps of stair, one or two steps at a time".format(a))
    print("{} ways to climb 10 steps of stair, one or two steps at a time".format(b))
    assert a == 13, "stair_test failed"
    assert b == 274, "stair_test failed"


def stair_ksteps(num, k):
    """gives the number of ways to climb n steps, at each step,
       you can choose to take 1, 2, ... k-2, k-1 or k steps"""

    def base(k):
        """returns how to climb k steps using up to k steps"""
        # two base case,
        # 0 is taking one k-steps to climb k steps, only one way
        # 1 is taking one step at a time to climb k steps, only one way
        if k in (0, 1):
            return 1
        else:
            # base(1)+base(2)+base(3)+...base(k-1)+base(0)
            sum_base = sum([base(i) for i in range(k)])
            return sum_base
    if num <= k:
        return base(num)
    else:
        sum_stair = sum([stair_ksteps(num-i, k) for i in range(1, k+1)])
        return sum_stair


def stair_ksteps_test():
    a = stair_ksteps(5, 2)
    b = stair_ksteps(5, 5)
    c = stair_ksteps(10, 5)
    print(a, b, c)
    assert a == 8, "stair_ksteps_test failed"
    assert b == 16, "stair_ksteps_test failed"
    assert c == 464, "stair_ksteps_test failed"


if __name__ == "__main__":
    replace_with_sum_test()
    matrix_product_test()
    reverse_test()
    permutation_test()
    pizza_distributor_test()
    stair_test()
    stair_ksteps_test()

