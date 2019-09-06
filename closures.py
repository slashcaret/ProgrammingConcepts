#############################################################################
''' Simple Definition: A closure is an INNER FUNCTION that remembers and has
access to variables in local scope in which it was created even after
the Outer Function has Finished Executing.'''

################################# Example 1 ##################################


def take_msg(message):

    edited_msg = message + ' edited by '

    def give_msg(name):
        print(edited_msg + name)  # accessing Varaible outside scope

    return give_msg  # Function being returned


print("Name of outer Function: ", take_msg.__name__)
print('-->Executing Outer Function')
result = take_msg('Python is Awesome')  # assigning returned function
for i in range(3):
    print('.')
print('-->Finished Executing Outer Function')
print('\n')
'''Here Outer Function has Finished Executing But Inner Function still has access
to variable craeted in its scope'''
print("Name of inner Function: ", result.__name__)
print('-->Executing Inner Function')
result('Nilesh Unde')
print('-->Finished Executing Inner Function\n')


################################# Example 2 ##################################
import logging

logging.basicConfig(filename='closures.log', level=logging.INFO)


def logger(func):

    def log_func(*args):
        logging.info('Runnning "{}" with arguments {}'.format(
            func.__name__, args))
        print(func(*args))

    return log_func


def add(*args):
    sum = 0

    for i in args:
        sum = sum + i
    return sum


def mul(*args):
    mul = 1

    for i in args:
        mul = mul * i
    return mul


add_logger = logger(add)
mul_logger = logger(mul)

add_logger(12, 4, 5, 87, 9, 32)
mul_logger(4, 78, 5, 8, 4)
