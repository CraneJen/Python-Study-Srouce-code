def selectionsort0(seq):
    n = len(seq)
    count = 0
    for i in range(n - 1, 0, -1):
        pom = 0
        for j in range(1, i + 1):
            if seq[pom] < seq[j]:
                pom = j
        seq[i], seq[pom] = seq[pom], seq[i]
        count = count + 1
    print(count)
    return seq


def selectionsort1(seq):
    n = len(seq)
    count = 0

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] > seq[i]:
                min_index = j
                seq[j], seq[i] = seq[i], seq[j]
                count += 1

    print(count)
    return min_index, seq


if __name__ == '__main__':
    seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(selectionsort0(seq))
    print(selectionsort1(seq))
