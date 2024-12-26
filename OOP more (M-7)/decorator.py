# decorator is a nested function
# """
# decorator
def timer(func):
    def inner():
        print('time started')
        # print(func)
        func()
        print('time ended')
    return inner

# timer()()


@timer  # calling decorator
def get_timer():
    print('doing something')

get_timer()

# timer(get_timer)()    <-----instead of this, use @timer

# """

import math
import time

def timer2(func):
    def inner(*args, **kwargs):
        
        print('time started')
        start = time.time()

        func(*args, **kwargs)

        print('time ended')
        end = time.time()
        print(f'total time taken {end - start}')

    return inner

@timer2
def get_factorial(n):
    result = math.factorial(n)
    print(f'the factorial of {n} is: {result}')

get_factorial(n=5)
# get_factorial(5)  <--OR