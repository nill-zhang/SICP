
def tree(rt, branches=[]):
    """ constructor for a tree ADT"""
    assert type(branches) == list, 'branches must be list'
    for each in branches:
        assert is_tree(each), 'sub branches must be trees'
    return [rt] + list(branches)


def root(t):
    """root selector selects a root node of the tree"""
    if is_tree(t):
        return t[0]


def branch(t):
    """branch selector selects tree's branches"""
    if is_tree(t):
        return t[1:]


def is_tree(t):
    if len(t) < 1 or type(t) != list:
        return False
    elif len(t) == 1 and type(t) == list:  # one node tree(only has root node)
        return True
    else:
        return is_tree(t[1:])              # recursively evaluate its branches


def is_leaf(t):
    """ returns true if a tree is a leaf(branches is empty)"""
    if is_tree(t) and len(t) == 1:
        return True
    else:
        return False


def count_leaves(t):
    """ gets the number of leaves in the tree"""
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaves(x) for x in branch(t))  # get the sum of leaves in all the subtrees in branch


def fibonacci_tree(n):
    """fibonacci_tree builds the tree top-down using tree abstraction"""
    if n in (0, 1):
        return tree(n)
    else:
        left_child, right_child = fibonacci_tree(n-1), fibonacci_tree(n-2)
        nroot = root(left_child) + root(right_child)
        return tree(nroot, [left_child, right_child])


def tree_test():
    a = tree(90, [tree(1, [tree(2, [tree(4)])])])
    b = tree(24, [tree(73, [tree(21)])])
    c = tree(28, [a, b])
    d = tree(19, [tree(44), tree(55), tree(51), tree(76)])
    print("is a a tree? {0}".format(is_tree(a)))
    print("is b a tree? {0}".format(is_tree(b)))
    print("is c a tree? {0}".format(is_tree(c)))
    print("is d a tree? {0}".format(is_tree(d)))
    print("tree a {0}".format(a))
    print("root of tree a: {0}".format(root(a)))
    print("branches of tree a: {0}".format(branch(a)))
    print("tree c: {0}".format(c))
    print("leaves in tree c :{0}".format(count_leaves(c)))
    print("leaves in tree d :{0}".format(count_leaves(d)))
    print("fibonacci tree of 10:\n{0}".format(fibonacci_tree(8)))
    print("leaves in fibonacci tree 8: {0}".format(count_leaves(fibonacci_tree(8))))


if __name__ == "__main__":
    tree_test()