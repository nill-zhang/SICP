class Tree(object):
    def __init__(self, value, children=[]):
        self.value = value
        # the following is a faulty statement, extend() always return None, it did the change in-place
        # self.children = [].extend(children)
        self.children = children


def depth_first_using_stack(t):
    """ traverse a tree's elements depth first"""
    stack = []
    traversed_values = []
    while t:
        print(t.value)
        traversed_values.append(t.value)
        if t.children:
            if len(t.children) > 1:
                # push other children to the stack for later traversal
                # why I changed the following linke of code from t.children[1::-1] to t.children[1:][::-1]?
                # because t.children[1::-1] returns elements starting from the second element to
                # the first one
                # for child in t.children[1::-1]:
                for child in t.children[1:][::-1]:
                    stack.append(child)
            t = t.children[0]
        else:
            if len(stack) == 0:
                return traversed_values
            else:
                t = stack.pop()


def depth_first_using_stack_test():
    # a visualization of the tree
    #            1
    #          / |\\
    #         2  3 45
    #        / \
    #       6   7
    #      /
    #     8
    #    /
    #   9
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    values = depth_first_using_stack(tree)
    assert values == [1, 2, 6, 8, 9, 7, 3, 4, 5], "depth_first test failed"


def breadth_first_using_stack(t):
    """ traverses the tree breadth_first"""
    # using a list as a stack, list method append as push, pop as pop, respectively
    stack = []
    traversed_values = []
    while t:
        if t.children:
            # store the rest of children and the parent node
            stack.append(t.children[1:])
            stack.append(t)
            # go to its first child
            t = t.children[0]
        else:
            traversed_values.append(t.value)
            while True:
                if len(stack) == 0:
                    t = None
                    break
                # pop up the parent node
                t = stack.pop()
                # if t is a parent node
                if t is not None:
                    print(t.value)
                    traversed_values.append(t.value)
                # pop up other children of the parent node
                other_children = stack.pop()
                if len(other_children) >= 1:
                    # go to the second child
                    t = other_children[0]
                    if len(other_children) > 1:
                        # if a parent node has more than 2 children
                        # the parent node don't need to be pushed to the stack again
                        # for traversal,because it has already been traversed before the second child
                        # therefore, only the not yet traversed child needs to be pushed to the stack
                        stack.append(other_children[1:])
                        stack.append(None)
                    break

    return traversed_values


def breadth_first_using_stack_test():
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    values = breadth_first_using_stack(tree)
    assert values == [9, 8, 6, 2, 7, 1, 3, 4, 5], "breadth_first test failed"


def pre_order(t, traversed_values=[]):
    traversed_values.append(t.value)
    if t.children:
        pre_order(t.children[0], traversed_values)
        if len(t.children) > 1:
            for child in t.children[1:]:
                pre_order(child, traversed_values)


def pre_order_test():
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    a = []
    pre_order(tree, a)
    assert a == [1, 2, 6, 8, 9, 7, 3, 4, 5], "pre_order test failed"


def in_order(t, traversed_values=[]):
    if t.children:
        in_order(t.children[0], traversed_values)
    traversed_values.append(t.value)
    if len(t.children) > 1:
        for child in t.children[1:]:
            in_order(child, traversed_values)


def in_order_test():
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    a = []
    in_order(tree, a)
    assert a == [9, 8, 6, 2, 7, 1, 3, 4, 5], "in_order failed"


def post_order(t, traversed_values=[]):
    if t.children:
        post_order(t.children[0],traversed_values)
        if len(t.children) > 1:
            for child in t.children[1:]:
                post_order(child, traversed_values)
    traversed_values.append(t.value)


def post_order_test():
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    a = []
    post_order(tree, a)
    assert a == [9, 8, 6, 7, 2, 3, 4, 5, 1], "post_order failed"


if __name__ == "__main__":
    depth_first_using_stack_test()
    breadth_first_using_stack_test()
    pre_order_test()
    in_order_test()
    post_order_test()

