from Stack import Stack
# from pythonds.basic.stack import Stack


def divideBy2(num):
    remstack = Stack()

    while num > 0:
        rem = num % 2
        remstack.push(rem)
        num = num // 2

    # binString = ''
    # while not remstack.isEmpty():
    #     binString = binString + str(remstack.pop())

    # return binString


print(divideBy2(40))
