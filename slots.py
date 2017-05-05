class Student(object):
    __slots__ = ('name', 'age')


class GStudent(object):
    __slots__ = ('__dict__', 'name', 'age')
