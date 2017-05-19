def linked_list(val, nex):
    assert is_linked_list(nex), "next should be linked list"
    return [val] + [nex]


def isEmpty(lst):
    return lst == []


def value(lst):
    assert is_linked_list(lst), "parameter is not a linked list"
    return lst[0]


def next(lst):
    assert is_linked_list(lst), "parameter is not a linked list"
    return lst[1]


def join_linked_lists(lst1, lst2):
    assert is_linked_list(lst1) and is_linked_list(lst2),"not all operands are linked lists"
    a = lst1
    while not isEmpty(a):
        a = next(a)
    # a = a + lst2
    a += lst2
    return lst1


def getItem(lst):
    pass


def setItem(lst):
    pass


def _extreme(lst):
    assert not isEmpty(lst), "linked list is empty!"
    minimum = value(lst)
    maximum = value(lst)
    cur = next(lst)
    while not isEmpty(cur):
        if value(cur) < minimum:
            minimum = value(cur)
        if value(cur) > maximum:
            maximum = value(cur)
        cur = next(cur)
    return minimum, maximum


def min(lst):
    return _extreme(lst)[0]


def max(lst):
    return _extreme(lst)[1]


def insert(lst):
    pass


def delete(l):
    pass


def flatten(lst):
    assert is_linked_list(lst), "parameter is not a linked list"
    if isEmpty(lst):
        return []
    return [value(lst)] + flatten(next(lst))


def linked_list_from_list(lst):
    assert type(lst) == list, "parameter is not a list"
    if not lst:       # lst == []
        return []
    return lst[:1]+[linked_list_from_list(lst[1:])]


def apply_to_all(f, lst):
    assert is_linked_list(lst), "second parameter is not a linked list"
    if isEmpty(lst):
        return lst
    else:
        new_value = f(value(lst))
        new_next = apply_to_all(f, next(lst))
        return linked_list(new_value, new_next)


def keep_if(f, lst):
    assert is_linked_list(lst), "second parameter is not a linked list"
    if isEmpty(lst):
        return lst
    else:
        if not f(value(lst)):
            return keep_if(f, next(lst))
        else:
            new_value = value(lst)
            new_next = keep_if(f, next(lst))
            return linked_list(new_value, new_next)


def is_linked_list(lst):
    if type(lst) != list or len(lst) != 2:
        return False
    if next(lst):
        return is_linked_list(next(lst))
    return True


def linked_list_test():
    pass


if __name__ == "__main__":
    linked_list_test()
