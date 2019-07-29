def insertsort(seq):
    n = len(seq)
    count = 0

    for i in range(1, n):
        key = seq[i]
        j = i - 1

        while j >= 0 and key < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
            count += 1

        seq[j + 1] = key

    print(count)
    return seq


if __name__ == '__main__':
    seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insertsort(seq))
