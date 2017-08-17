class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        print(self.day, self.month, self.year)

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1


class D(Date):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

        print(self.day, self.month, self.year)

    def s(self, *args):
        return super(D, self).from_string(*args)


d = D.from_string('11-12-2012')
