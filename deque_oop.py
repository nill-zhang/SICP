class Deque(object):

    def __init__(self, size):
        self.maxlen = size
        self.ds = []

    def pop_left(self):
        return self.ds.pop(0)

    def __len__(self):
        return len(self.ds)

    def pop(self):
        return self.ds.pop()

    def extend(self, iter):
        for item in iter:
            self.append(item)

    def extend_left(self, iter):
        for item in iter:
            self.appendleft(item)

    def index(self, value):
        pass

    def append(self, val):
        if len(self.ds) >= self.maxlen:
            self.popleft()
        self.ds.append(val)

    def append_left(self, val):
        if len(self) >= self.maxlen:
            self.pop()
        self.ds.insert(0, val)

    def clear(self):
        self.ds.clear()

    def count(self, val):
        return self.ds.count(val)

    def remove(self):
        pass

    def reverse(self):
        def rever():
            if len(self) == 2:


    def rotate(self, i):

