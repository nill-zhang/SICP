def linked_list(val, nex):
    """constructs a linked list given its value and next"""
    assert is_linked_list(nex), "next should be linked list"
    return [val] + [nex]


def is_empty(lst):
    """ returns True if the linked list is empty """
    return lst == []


def value(lst):
    """ value selector selects current node's value"""
    assert is_linked_list(lst), "parameter is not a linked list"
    return lst[0]


def next(lst):
    """  next selects the next node the current node points to"""
    assert is_linked_list(lst), "parameter is not a linked list"
    return lst[1]


def join_linked_lists(lst1, lst2):
    """ joins the second linked list to the end of  the first one"""
    assert is_linked_list(lst1) and is_linked_list(lst2), "not all operands are linked lists"
    a = lst1
    while not is_empty(a):
        a = next(a)
    # a = a + lst2 there is indeed a difference between this line and the next
    a += lst2
    return lst1


def length(lst):
    """ returns the size of the linked list"""
    assert is_linked_list(lst), "parameter is not a linked list"
    size = 0
    while not is_empty(lst):
        size += 1
        lst = next(lst)
    return size


def get(lst, idx):
    """ return the value at index idx"""
    assert not is_empty(lst), 'linked list is empty!'
    assert idx in range(length(lst)), 'linked list index out of range'
    # range(length(lst)) will be executed once and only once
    # although lst is rebound later to its next
    for i in range(length(lst)):
        if i == idx:
            val = value(lst)
            break
        lst = next(lst)
    return val


def set(lst, idx, val):
    """ resets the value at idx"""
    # the design behind this function is to think about
    # how would you change a linked list in place, or build and return
    # new linked list
    assert idx in range(length(lst)), "linked list index out of range"
    for i in range(length(lst)):
        if idx == i:
            lst[0] = val
            break
        lst = next(lst)
    return None


def index(lst, val):
    """return first index of value"""
    for i in range(length(lst)):
        if val == value(lst):
            return i
        lst = next(lst)
    return None


def _extreme(lst):
    """ a helper function returns (min, max)"""
    assert not is_empty(lst), "linked list is empty!"
    mini = value(lst)
    maxi = value(lst)
    cur = next(lst)
    while not is_empty(cur):
        if value(cur) < mini:
            mini = value(cur)
        if value(cur) > maxi:
            maxi = value(cur)
        cur = next(cur)
    return mini, maxi


def reverse(lst):
    """ reverse a linked list"""
    lst = flatten(lst)
    lst = lst[::-1]
    return linked_list_from_list(lst)


def minimum(lst):
    """return the minimum value"""
    return _extreme(lst)[0]


def maximum(lst):
    """ return the maximum value"""
    return _extreme(lst)[1]


def flatten(lst):
    """ returns a list contains all the values of the given linked list
        reduce the nested linked list to flat list
    """
    assert is_linked_list(lst), "parameter is not a linked list"
    if is_empty(lst):
        return []
    return [value(lst)] + flatten(next(lst))


def linked_list_from_list(lst):
    """ constructs a linked list from a regular list"""
    assert type(lst) == list, "parameter is not a list"
    if not lst:       # lst == []
        return []
    return lst[:1]+[linked_list_from_list(lst[1:])]


def apply_to_all(f, lst):
    """ apply f to every element in lst"""
    assert is_linked_list(lst), "second parameter is not a linked list"
    if is_empty(lst):
        return lst
    else:
        new_value = f(value(lst))
        new_next = apply_to_all(f, next(lst))
        return linked_list(new_value, new_next)


def keep_if(f, lst):
    """ keeps all the elements in lst which makes f(x) ==  True"""
    assert is_linked_list(lst), "second parameter is not a linked list"
    if is_empty(lst):
        return lst
    else:
        if not f(value(lst)):
            return keep_if(f, next(lst))
        else:
            new_value = value(lst)
            new_next = keep_if(f, next(lst))
            return linked_list(new_value, new_next)


def is_linked_list(lst):
    """returns True if lst is a linked list"""
    if type(lst) != list or not len(lst) in (0, 2):
        return False

    if len(lst) == 0:  # base case [x,[]]
        return True
    else:
        return is_linked_list(lst[1])   # lst[1] is different from lst[1:]


def minimum_test():
    lst = linked_list(-12, linked_list(33, linked_list(900, linked_list(-2, []))))
    assert minimum(lst) == -12, "minimum function failed"


def maximum_test():
    lst = linked_list(-12, linked_list(33, linked_list(900, linked_list(-2, []))))
    assert maximum(lst) == 900, "maximum function failed"


def is_linked_list_test():
    lst = []
    assert is_linked_list(lst), "is_linked_list failed"
    lst = linked_list(3, [])
    assert is_linked_list(lst), "is_linked_list failed"


def length_test():
    a = []
    assert length(a) == 0, "length_test failed"
    b = [4, a]
    assert length(b) == 1, "lengt)_test failed"


def set_test():
    a = [1, [5, [19, [111, []]]]]
    set(a, 2, 9999)
    assert a == [1, [5, [9999, [111, []]]]], "set_test failed"


def get_test():
    a = [4, [1, [3.4, []]]]
    b = get(a, 2)
    assert b == 3.4, "get_test failed"


def index_test():
    a = []
    assert index(a, 11) is None, "index_test failed"

    b = [1, [2, [3, [90, [888, [131, []]]]]]]
    assert index(b, 888) == 4, "index_test failed"


def reverse_test():
    a = [5, [4, [3, [2, [1, []]]]]]
    b = reverse(a)
    assert b == [1, [2, [3, [4, [5, []]]]]]


def min_test():
    a = [0.1, [0.44, [0.1122, [0.42112, [0.428, [-0.1232, [-2, [31, [-1,[]]]]]]]]]]
    assert minimum(a) == -2, "minimum_test failed"


def max_test():
    a = [0.1, [0.44, [0.1122, [0.42112, [0.428, [-0.1232, [-2, [31, [-1, []]]]]]]]]]
    assert maximum(a) == 31, "maximum_test failed"


def flatten_test():
    a = []
    assert flatten(a) == [], "flatten_test failed"
    b = [1, [3, [0.22, [-22, []]]]]
    assert flatten(b) == [1, 3, 0.22, -22]


def linked_list_from_list_test():
    a = linked_list_from_list([])
    assert is_linked_list(a), "linked_list_from_list failed"
    b = linked_list_from_list(['a', 'c', 'd'])
    assert is_linked_list(b), "linked_list_from_list failed"


def apply_to_all_test():
    a = linked_list_from_list([1, 2, 3, 4, 5, 6])
    b = apply_to_all(lambda x: x**2, a)
    assert b == [1, [4, [9, [16, [25, [36, []]]]]]], "apply_to_all_test failed"


def keep_if_test():
    a = linked_list_from_list([3, 4, 12, 13, 0.1])
    b = keep_if(lambda x: x**2 >= 144, a)
    assert b == [12, [13, []]], "keep_if_test failed"


def join_linked_lists_test():
    a = linked_list_from_list([1, 2])
    b = linked_list_from_list(['a', 'b'])
    assert join_linked_lists(a, b) == [1, [2, ['a', ['b', []]]]]


if __name__ == "__main__":
    join_linked_lists_test()
    minimum_test()
    maximum_test()
    set_test()
    get_test()
    is_linked_list_test()
    linked_list_from_list_test()
    keep_if_test()
    apply_to_all_test()
    index_test()
    reverse_test()
    flatten_test()
    length_test()
