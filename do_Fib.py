class Fib(object):

    def __init__(self, max):
        self.a, self.b = 0, 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.max:
            raise StopIteration()
        return self.a


class Fib1(object):

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


class Fib2(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if step is None:
                step = 1
            if start is None:
                start = 0
            a, b = 1, 1
            L_slice = []
            L_step = []
            for x in range(stop):
                if x >= start:
                    L_slice.append(a)
                a, b = b, a + b
            for x in L_slice[::step]:
                L_step.append(x)
            return L_step


def fib1(max):
    a, b = 0, 1
    while b < max:
        print(b, end=' ')
        a, b = b, a + b


def fib2(max):
    result = []
    a, b = 0, 1
    while b < max:
        result.append(b)
        a, b = b, a + b
    return result


def fib3(max):
    a, b = 0, 1
    while max > 0:
        print(b, end=' ')
        a, b = b, a + b
        max -= 1


# yield


def fib4(max):
    a, b = 0, 1
    while max > 0:
        yield b
        a, b = b, a + b
        max -= 1


print([i for i in fib4(10)])
