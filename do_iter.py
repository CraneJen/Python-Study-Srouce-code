from collections import Iterable, Iterator

print(isinstance('abc', Iterable))
print(isinstance('abc', Iterator))
print(isinstance((x * x for x in range(10)), Iterable))
print(isinstance((x * x for x in range(10)), Iterator))
