from Queue import Queue


def hotPotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for n in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 15))
