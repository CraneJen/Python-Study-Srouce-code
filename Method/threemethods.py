class A(object):

    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @classmethod
    def cprint(*args):
        print('Class {}'.format(args))

    @staticmethod
    def sprint(*args):
        print('Static {}'.format(args))
