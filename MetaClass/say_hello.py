class SayMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # attrs['say_' + name] = lambda self, value, saying=name: print(
        #     f'{saying},{value}!')
        attrs['say_' + name] = lambda self, value: print(f'{name}, {value}!')
        return type.__new__(cls, name, bases, attrs)


class Hello(object, metaclass=SayMetaclass):
    pass


hello = Hello()

hello.say_Hello('World')


class Nihao(object, metaclass=SayMetaclass):
    pass


nihao = Nihao()

nihao.say_Nihao("中国")
