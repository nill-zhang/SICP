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




