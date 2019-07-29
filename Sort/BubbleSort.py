def bubblesort0(seq):
    n = len(seq)
    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
                count = count + 1
    print(count)
    return seq


def bubblesort1(seq):
    n = len(seq)
    count = 0

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if seq[j] < seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                count += 1

    print(count)
    return seq


def bubblesort2(seq):
    n = len(seq)
    count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                count += 1

    print(count)
    return seq


if __name__ == '__main__':
    seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubblesort0(seq))
    print(bubblesort1(seq))
    print(bubblesort2(seq))
