def linked_list(val, nex):
    """constructs a linked list given its value and next"""
    assert is_linked_list(nex), "next should be linked list"
    return [val] + [nex]


def is_empty(lst):
    """ returns True if it is a linked list """
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
    assert is_linked_list(lst1) and is_linked_list(lst2),"not all operands are linked lists"
    a = lst1
    while not isEmpty(a):
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
    assert is_empty(lst), 'linked list is empty!'
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
    # how would you change a linked list inplace, or build and return
    # new linked list
    assert idx in range(length(lst)),"linked list index out of range"
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
    lst = linked_list(-12, linked_list(33, linked_list(900, linked_list(-2))))
    assert minimum(lst) == -12, "minimum function failed"


def maximum_test():
    lst = linked_list(-12, linked_list(33, linked_list(900, linked_list(-2))))
    assert maximum(lst) == 900, "maximum function failed"


def is_linked_list_test():
    lst = []
    assert is_linked_list(lst),"is_linked_list failed"
    lst = linked_list(3,[])
    assert is_linked_list(lst),"is_linked_list failed"


def linked_list_test():
    list_a = linked_list(13, linked_list(9, linked_list(42, linked_list(5, linked_list(3, [])))))
    list_b = linked_list(93, linked_list(900, linked_list(22, [])))
    list_c = linked_list_from_list([4.0, 2.1, 0.12, 5.6, 7.7, 2.5])
    print("lnklst a: ", list_a)
    print("lnklst b: ", list_b)
    print("lnklst c: ", list_c)
    join_linked_lists(list_a, [-0.11, [-0.111, []]])
    print("lnklst a: ", list_a)
    list_a = keep_if(lambda x: x > 0, list_a)
    print("positive elements in lnklst a: ", list_a)
    list_b = apply_to_all(lambda x: x + 1000, list_b)
    print("add 1000 to every elements in lnklst b:", list_b)
    list_d = flatten(list_c)
    print("flattened list_c:", list_d)
    list_e = reverse(list_a)
    print("list_a reversed: ", list_e)
    print("is [] a linked list ? ", is_linked_list([]))


if __name__ == "__main__":
    linked_list_test()
