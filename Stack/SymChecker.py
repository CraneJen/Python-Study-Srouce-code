from Stack import Stack

lefts = '{[(<'
rights = '}])>'


def symChecker(symbolString):
    index = 0
    balenched = True
    s = Stack()

    while index < len(symbolString) and balenched:
        symbol = symbolString[index]
        if symbol in lefts:
            s.push(symbol)
        else:
            if s.isEmpty():
                balenched = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balenched = False
        index += 1

    if balenched and s.isEmpty():
        return True
    else:
        return False


def matches(left, right):
    return lefts.index(left) == rights.index(right)


print(matches('<', '>'))
print(symChecker('{{<()>}}'))
print(symChecker('{{([][])}()}'))
print(symChecker('[{()]'))
