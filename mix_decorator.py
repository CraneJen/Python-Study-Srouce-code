from functools import wraps
# import types
import datetime


def log(arg):
    # if isinstance(arg, types.FunctionType):
    if not type(arg) == str:
        @wraps(arg)
        def wrapper(*args, **kwargs):
            print('start {name}()...'.format(name=arg.__name__))
            arg(*args, **kwargs)
            print('end {name}()...'.format(name=arg.__name__))
        return wrapper

    else:
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print('{arg} {name}()...'.format(arg=arg, name=func.__name__))
                func(*args, **kwargs)
                print('end {name}()...'.format(name=func.__name__))
            return wrapper
        return decorator


@log  # today=log(today)
def today():
    print(datetime.date.today())


@log('Execute')  # tomorrow=log('Execute')(tomorrow)
def tomorrow():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    print(tomorrow)


today()
print('\n')
tomorrow()
