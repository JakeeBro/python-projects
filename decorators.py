# Decorator

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(greeting="Hello", emoji=":)"):
    print(greeting + " " + emoji)


hello("hey")
