class Tree(object):
    def __init__(self, value, children=[]):
        self.value = value
        # the following is a faulty statement, extend() always return None, it did the change in-place
        # self.children = [].extend(children)
        self.children = children


def depth_first_using_stack(t):
    stack = []
    traversed_values = []
    while t:
        print(t.value)
        traversed_values.append(t.value)
        if t.children:
            if len(t.children) > 1:
                # push other children to the stack for later traversal
                # why I changed from t.children[1::-1] to t.children[1:][::-1]?
                # because
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
    # a visualization of my tree
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
    stack = []
    traversed_values = []
    while t:
        if t.children:
            stack.append(t.children[1:])
            stack.append(t)
            t = t.children[0]
        else:
            print(t.value)
            traversed_values.append(t.value)
            while True:
                if len(stack) == 0:
                    t = None
                    break
                t = stack.pop()
                if t is not None:
                    print(t.value)
                    traversed_values.append(t.value)
                other_children = stack.pop()
                if len(other_children) >= 1:
                    t = other_children[0]
                    if len(other_children) > 1:
                        stack.append(other_children[1:])
                        stack.append(None)
                    break

    return traversed_values


def breadth_first_using_stack_test():
    tree = Tree(1, [Tree(2, [Tree(6, [Tree(8, [Tree(9)])]), Tree(7)]), Tree(3), Tree(4), Tree(5)])
    values = breadth_first_using_stack(tree)
    assert values == [9, 8, 6, 2, 7, 1, 3, 4, 5], "breadth_first test failed"

if __name__ == "__main__":
    depth_first_using_stack_test()
    breadth_first_using_stack_test()
