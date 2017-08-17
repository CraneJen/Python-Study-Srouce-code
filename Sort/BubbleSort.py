def bubble(seq):
    length = len(seq)
    count = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
                count = count + 1
        print(seq)
    print(count)
    return seq


if __name__ == '__main__':
    seq = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble(seq))
