def count():
    def fn(i):
        def g():
            return i * i
        return g
    L = []
    for i in range(1, 4):
        L.append(fn(i))
    return L


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
