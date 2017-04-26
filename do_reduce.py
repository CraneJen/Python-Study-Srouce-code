from functools import reduce

print('=== Reduce ===')


def fn(x, y):
    return x * 10 + y


result = reduce(fn, [1, 3, 5, 7, 9])
result1 = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])
print("Result: {result}".format(result=result))
print("Result1: {result1}".format(result1=result1))
# result: 13570

print("=== Reduce & Map ===")


def char2int(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


s = '1234'
result2 = reduce(fn, map(char2int, s))
print("Result2: {result2}".format(result2=result2))

print("=== Palindrome ===")


def is_palindrome(n):
    # n = str(n)
    # return n == n[::-1]
    lsn = list(str(n))
    # ls = lsn[:]
    # ls = list(lsn)
    ls = lsn * 1
    lsn.reverse()
    return ls == lsn


output = filter(is_palindrome, range(1, 1000))
print(list(output))
# print(range(1, 1000))

print(list(filter(lambda n: str(n) == str(n)[::-1], range(1, 1000))))
