import datetime


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        else:
            self._score = value


class C(object):

    @property
    def x(self):
        "I am the 'x' property"
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class S(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        elif value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100!')
        else:
            self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError('Birth must a integer!')
        if value > datetime.datetime.today().year:
            raise ValueError('Birth error')
        self._birth = value

    @property
    def age(self):
        year = datetime.datetime.today().year
        return year - self.birth


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height
