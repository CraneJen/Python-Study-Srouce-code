def bubble(seq):
    length = len(seq)
    count = 0
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if seq[j + 1] < seq[j]:
                seq[j + 1], seq[j] = seq[j], seq[j + 1]
                count = count + 1
    print(count)
    return seq


if __name__ == '__main__':
    seq = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(seq)
    print(bubble(seq))
