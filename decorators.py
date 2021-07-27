def custom_decorator(func):
    def wrap_func(*args, **kwargs):
        print('======')
        func(*args, **kwargs)
        print('======')
    return wrap_func


@custom_decorator
def hello(greeting='Hello', emoji=':)'):
    print(greeting + ' ' + emoji)


hello(emoji=':/', greeting='hey')
