def triangles():
    L = [1]
    while True:
        # print(L)
        yield L
        L = [L[0]] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [L[-1]]
        # L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


x = int(input('Input: '))
n = 0
for t in triangles():
    print(n, end=' ')
    print(t)
    n += 1
    if n == x:
        break


# def triangles(n):
#     L = [1]
#     for i in range(n):
#         print(i, end=' ')
#         yield L

#         # L = [L[0]] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [L[-1]]
#         L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# n = int(input("Input level: "))
# for data in triangles(n):
#     print(data)


# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]


# n = 0
# for t in triangles():
#     print(n, end=' ')
#     print(t)
#     n += 1
#     if n == 10:
#         break
