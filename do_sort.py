L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(s):

    return s[0]
    # return s[0].lower()


def by_score(s):
    return s[1]


print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))

# lambda
print("Simple by lambda:")
print(sorted(L, key=lambda s: s[0].lower()))
print(sorted(L, key=lambda s: s[1], reverse=True))


# def by_name_score():
#     t = sorted(L, key=by_name)
#     for i in range(len(t) - 1):
#         alist = [t[i]]
#         for j in range(len(t))


# bns = by_name_score()


# def order(t):
#     t = sorted(t, key=by_name)
#     for i in range(len(t) - 1):
#         alist = [t[i]]
#         print(alist)
#         for j in list(range(len(t)))[i + 1:]:
#             print(j)
#             if t[i][0][0] == t[j][0][0]:
#                 alist.append(t[j])
#         L = sorted(alist, key=by_score, reverse=True)
#         t = t[: i] + L + t[i + len(L):]
#     return t


# L2 = order(L)
# print(L2)
