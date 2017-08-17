def selectionSort(seq):
    length = len(seq)
    count = 0
    for i in range(length - 1, 0, -1):
        pom = 0
        for j in range(1, i + 1):
            if seq[pom] < seq[j]:
                pom = j
        seq[i], seq[pom] = seq[pom], seq[i]
        count = count + 1
    print(count)
    return seq


if __name__ == '__main__':
    seq = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selectionSort(seq))
