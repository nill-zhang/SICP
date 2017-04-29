#/usr/env/python


class ATM(object):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "insufficient money"
        self.balance -= amount
        return self.balance


def rightOperand(y):
    def sub(x):
        if x > y:
            return x - y
        else:
            return y - x
    return sub

# No nonlocal statement is required to access a non-local name.like
# I did in rightOperand for non-local y
# By contrast, only after a nonlocal statement can a function
# change the binding of names in these frames. If I remove nonlocal balance from
# atm, an error will occur.
# This UnboundLocalError appears because balance is
# assigned locally in line 5, and so Python assumes
# that all references to balance must appear in the local frame
# as well. This error occurs before line 5 is ever executed,
# implying that Python has considered line 5 in some way before
# executing line 3
# note rightOperand VS atm, the only difference is I try to change
# the value of balance, to change the internal state


def atm(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "insufficient money"
        balance -= amount
        return balance
    return withdraw


def rightOperand_test():
    sub = rightOperand(5)
    print(sub(10))
    print(sub(2))


def atm_test():
    # wd is no-pure function, two identical inputs give two different outputs
    # when local frame for withdraw is removed, there is still an outside state kept, next
    # time when I call withdraw, it continues with that state, this state in our scenario
    # is the nonlocal balance which exists in function withdraw's parent environment
    wd = atm(1000)
    print(wd(550))
    print(wd(550))


def ATM_test():
    wd = ATM(1000)
    print(wd.withdraw(550))
    print(wd.withdraw(550))


if __name__ == "__main__":

   atm_test()
   ATM_test()
   rightOperand_test()

# Note: for dictionary, you don't need to use nonlocal, if you only change its keys and values
# if you change the dictionary itself you need nonlocal
#
# >>> def a(b):
# ...     def c(x):
# ...         b["sfzhang"] += x
# ...         return b
# ...     return c
# ...
# >>>
# >>> a({"sfzhang":"sfzhang","xlyang":"xlyang"})("xxxxxxxxx")
# {'sfzhang': 'sfzhangxxxxxxxxx', 'xlyang': 'xlyang'}
#
#
# >>> def a(b):
# ...     def c(x):
# ...         if x > b["sfzhang"]:
# ...             b = x
# ...         return b
# ...     return c
# ...
# >>>
# >>> a({"sfzhang":4,"xlyang":"xlyang"})(8)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     a({"sfzhang":4,"xlyang":"xlyang"})(8)
#   File "<input>", line 3, in c
#     if x > b["sfzhang"]:
# UnboundLocalError: local variable 'b' referenced before assignment
#
#
# >>> def a(b):
# ...     def c(x):
# ...         if x > b["sfzhang"]:
# ...             b["sfzhang"] = x
# ...         return b
# ...     return c
# ...
# >>>
# >>> a({"sfzhang":4,"xlyang":"xlyang"})(8)
# {'sfzhang': 8, 'xlyang': 'xlyang'}




