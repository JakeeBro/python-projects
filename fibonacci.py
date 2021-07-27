import math
from performance import performance


#@performance
def fibonacci_formula(index):
    phi = (1 + math.sqrt(5)) / 2

    for i in range(0, index + 1):
        num = (math.pow(phi, i) - math.pow((-1/phi), i)) / math.sqrt(5)
        print(float(num))
        #print(len(str(int(num))))


#fibonacci_formula(0)

#@performance
def fibonacci_generator(index):
    a = 0
    b = 1
    for i in range(index + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fibonacci_generator(20):
    print(type(x))
