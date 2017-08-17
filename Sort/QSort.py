def qsrot(seq):
    if seq == []:
        return []
    else:
        p = seq[0]
        lesser = qsrot([x for x in seq[1:] if x < p])
        greater = qsrot([x for x in seq[1:] if x > p])
    return lesser + [p] + greater


if __name__ == '__main__':
    seq = [5, 33, 4, 78, 3, -65, 12]
    print(seq)
    print('Result:{}'.format(qsrot(seq)))
