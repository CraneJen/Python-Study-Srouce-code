class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
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


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def fib3(max):
    a, b, n = 0, 1, 0
    while n < max:
        print(b, end=' ')
        a, b = b, a + b
        n = n + 1


# yield


def fib4(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
