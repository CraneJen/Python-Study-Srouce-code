def fn(x):
    return x * x


L = [x for x in range(1, 11)]
print(L)

r = map(fn, L)
s = map(float, L)
# print(list(map(int, n)))
print(list(r))
print(list(s))


# print(r)
# print(next(r))
# print(next(r))
