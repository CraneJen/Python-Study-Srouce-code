def shortBubble(seq):
    exchange = True
    length = len(seq) - 1
    count = 0
    while length > 0 and exchange:
        exchange = False
        for i in range(length):
            if seq[i] > seq[i + 1]:
                exchange = True
                count = count + 1
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
            # print(seq)
        length = length - 1
    print(count)
    return seq


if __name__ == '__main__':
    seq = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(shortBubble(seq))
