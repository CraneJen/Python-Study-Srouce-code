import datetime
# import functools
from functools import wraps


def log(func):
    print(type(func))

    def wrapper(*args, **kwargs):
        print("call {name}()...".format(name=func.__name__))
        func(*args, **kwargs)
        print("end {name}()...".format(name=func.__name__))
    return wrapper


@log
def today():
    print(datetime.date.today())


today()


def log(text):
    print(type(text))

    def decorator(func):
        print(type(func))
        # @functools.wraps(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("{text} {name}()...".format(text=text, name=func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log("execute")
def tomorrow():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    print(tomorrow)


tomorrow()
print(tomorrow.__name__)
