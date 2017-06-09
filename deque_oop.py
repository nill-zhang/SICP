class Deque(object):

    def __init__(self, size):
        self.maxlen = size
        self.ds = []

    def popleft(self):
        pass

    def pop(self):
        pass

    def extend(self, iter):
        pass

    def extendleft(self, iter):
        pass

    def index(self, value):
        pass

    def append(self):
        if len(self.ds) == self.maxlen:
            self.append()
        pass

    def appendleft(self):
        pass

    def clear(self):
        pass

    def count(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        pass

    def rotate(self, i):
        pass