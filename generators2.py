def generator_function(num):
    for i in range(num):
        yield i*2


# for item in generator_function(5):
#     print(item + 1)


g = generator_function(100)
next(g)
next(g)
print(next(g))
