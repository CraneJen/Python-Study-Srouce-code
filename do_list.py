print([x * x for x in range(2, 10) if x % 3 == 0])

D = {'x': 'A', 'y': 'B', 'z': 'C'}
for x, y in D.items():
    print("{x} = {y}".format(x=x, y=y))
print([x + '=' + y for x, y in D.items()])


L = ['Hello', 'World', 'IBM', 'Apple']
L1 = [l.lower() for l in L]
print(L1)

LN = ['Hello', 'World', 77, 'Apple', None]
LN1 = []
for ln in LN:
    if isinstance(ln, str):
        # print(ln.lower())
        LN1.append(ln.lower())
    else:
        LN1.append(ln)
print(LN1)

print([ln.lower() for ln in LN if isinstance(ln, str)])
