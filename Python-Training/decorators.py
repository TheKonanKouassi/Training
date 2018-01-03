# Decorators

import time
import logging
from functools import wraps

# def out_function(msg: str):
#
#     def inner_function():
#
#         print(msg + ' Ange')
#
#     return inner_function
# hi_func = out_function('hi')
# bye_func = out_function('bye')
#
# hi_func()
#
# bye_func()

def decorator_function(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):

        print(f'wrapper executed this before {original_function.__name__}')

        return original_function(*args, **kwargs)

    return wrapper_function

# class decorator_class(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print(f'call method executed this before {self.original_function.__name__}')
#         return self.original_function(*args, **kwargs)
#
# @decorator_function
# def display():
#
#     print('display function ran')
#
# @decorator_function
# def display_info(name: str, age: int):
#     print(f'display_info ran with arguments ({name}, {age})')
#
# display()
#
# display_info('Ange', 26)

#
# Practical examples
#

def my_logger(orig_func):

    logging.basicConfig(filename = f'{orig_func.__name__}', level = logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):

        logging.info(msg = f'Ran with args: {args}, and kwargs: {kwargs}')

        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):

        t1 = time.time()

        result = orig_func(*args, **kwargs)

        t2 = time.time() - t1

        print(f'{orig_func.__name__} ran in : {t2} sec')

        return result

    return wrapper

# @my_logger
@my_timer
def display_info(name: str, age: int):
    print(f'display_info ran with arguments ({name}, {age})')

#display_info('Konan', 26)

# ====================================================================================================== #
# Decorators with arguments


def prefix_decorator(prefix):

    def decorator_function(original_function):

        @wraps(original_function)
        def wrapper_function(*args, **kwargs):

            print(prefix, f'Wrapper executed before {original_function.__name__}')

            result = original_function(*args, **kwargs)

            print(prefix, f'Wrapper executed after {original_function.__name__} \n')

            return result

        return wrapper_function

    return decorator_function

@prefix_decorator('TESTTING:')
def display_info(name: str, age: int):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Ange', 26)






