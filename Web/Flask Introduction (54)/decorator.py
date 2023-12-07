import time
import datetime
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(function_name, n1, n2):
    return function_name(n1,n2)

print(calculate(add,2,3))
print(calculate(multiply,2,3))

##Functions can be nested in other functions

def outer_function():
    print("I'm an outer function")
    
    def inner_function():
        print("I'm an inner function")
    
    inner_function()

outer_function()

## Functions can be returned from other functions


def outer_function_2():
    print("I'm an outer function 2")
    
    def inner_function():
        print("I'm an inner function 2")
    
    return inner_function

output_function = outer_function_2()
output_function()


## Python Decorator

def my_decorator(function):
    def wrapper_function():
        function()
    return wrapper_function

def delayed_decorator(function):
    def wrapper_function():
        # Do Something Before Function
        time.sleep(2)
        function()
        # Do Something After Function
    return wrapper_function

@delayed_decorator
def say_hello():
    print('Hello!')

@delayed_decorator
def say_bye():
    print('Bye!')

def say_greetings():
    print('Greetings!')
say_hello()
say_bye()
say_greetings()

decorated_function = delayed_decorator(say_greetings)
decorated_function()


def decorator_time_it(function):
    def timer():
        start_time = time.time()
        function()
        completed_seconds = time.time() - start_time
        print(f'{function.__name__} was completed in {completed_seconds} seconds')
    return timer

@decorator_time_it
def fast_function():
    for i in range(100000):
        i*i

@decorator_time_it
def slow_function():
    for i in range(1000000):
        i*i

fast_function()
slow_function()
