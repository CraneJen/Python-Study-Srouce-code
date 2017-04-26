L = [x for x in range(1, 11)]
print(L)
G = (x for x in range(1, 11))
print(G)
# print(next(G))
for n in G:
    print(n)

print('Fib:')


def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)


def fib_0(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'


f0 = fib_0(7)
for f in f0:
    print(f)

f1 = fib_0(7)
while True:
    try:
        print("g: {next}".format(next=next(f1)))
    except StopIteration as e:
        print("Genetor return value: {value}".format(value=e.value))
        break
