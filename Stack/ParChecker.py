# from pythonds.basic.stack import Stack
from Stack import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


S = Stack()
S.push('J')
print(S.peek())
print(parChecker('((()))'))
print(parChecker('(())(('))
