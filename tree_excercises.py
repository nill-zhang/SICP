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


def depth_first_using_stack_test(tree):
    values = depth_first_using_stack(tree)
    assert values == [1, 2, 6, 8, 9, 7, 3, 4, 5], "depth_first test failed"


def dfs_using_stack(t):
    trees = [t]
    traversed_values = []
    while trees:
        t = trees.pop()
        traversed_values.append(t.value)
        # if it has children, push all the children
        # to the stack. the first children on the top of stack
        # it is traversed next after the current parent node
        for child in t.children[::-1]:
            trees.append(child)
    return traversed_values


def dfs_using_stack_test(tree):
    values = dfs_using_stack(tree)
    print("dfs:", values)
    assert values == [1, 2, 6, 8, 9, 7, 3, 4, 5], "dfs_test failed"


def bfs_using_queue(t):
    trees = [t]
    traversed_values = []
    while trees:
        t = trees.pop(0)
        traversed_values.append(t.value)
        # breadth-first traverse level by level, left to right.
        # if a node has children, put all the children to
        # the end of the queue, they will be traversed after
        # the current parent node's siblings
        trees.extend(t.children)
    return traversed_values


def bfs_using_queue_test(tree):
    values = bfs_using_queue(tree)
    print("bfs:", values)
    assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9], "bfs_test failed"


def in_order_using_stack(t):
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


def in_order_using_stack_test(tree):
    values = in_order_using_stack(tree)
    assert values == [9, 8, 6, 2, 7, 1, 3, 4, 5], "in_oder test failed"


def pre_order(t, traversed_values=[]):
    traversed_values.append(t.value)
    for child in t.children:
        pre_order(child, traversed_values)


def pre_order_test(tree):
    a = []
    pre_order(tree, a)
    assert a == [1, 2, 6, 8, 9, 7, 3, 4, 5], "pre_order test failed"


def in_order(t, traversed_values=[]):
    if t.children:
        in_order(t.children[0], traversed_values)
    traversed_values.append(t.value)
    # even if t.children == [], t.children[1:] is []
    # it will not raise an index out of range Error
    for child in t.children[1:]:
            in_order(child, traversed_values)


def in_order_test(tree):
    a = []
    in_order(tree, a)
    assert a == [9, 8, 6, 2, 7, 1, 3, 4, 5], "in_order failed"


def post_order(t, traversed_values=[]):
    for child in t.children:
        post_order_test(child)

    # the following code is ugly compared to the above two lines

    # if t.children:
    #     post_order(t.children[0],traversed_values)
    #     if len(t.children) > 1:
    #         for child in t.children[1:]:
    #             post_order(child, traversed_values)
    traversed_values.append(t.value)


def post_order_test(tree):
    a = []
    post_order(tree, a)
    assert a == [9, 8, 6, 7, 2, 3, 4, 5, 1], "post_order failed"



def run_tests():
    # a visualization of the testing_tree
    #            1
    #          / |\\
    #         2  3 45
    #        / \
    #       6   7
    #      /
    #     8
    #    /
    #   9
    testing_tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])

    depth_first_using_stack_test(testing_tree)
    in_order_using_stack_test(testing_tree)
    pre_order_test(testing_tree)
    in_order_test(testing_tree)
    post_order_test(testing_tree)
    dfs_using_stack_test(testing_tree)
    bfs_using_queue_test(testing_tree)


if __name__ == "__main__":
    run_tests()

