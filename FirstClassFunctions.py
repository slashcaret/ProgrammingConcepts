# First Class Functions:
# First class Function is an entity in or a Function() that is treated
# as First Class CItizen in Python or any other Programming Language.
##############################################################################
# First class citizen means The entity that supports all the operations supported
# by any other Entities. These Opearations typically include being passed as an
# argument , being returned by a function or being assigned to variable.
##############################################################################

# In Short A First Class Function is availability provided by some
# programming languages, by which a Function can be assigned to a variable or
# it can be passed as an argument to any other Function (Ex. Python map() Function)
# or it can be returned by another Function.

##############################################################################
# For Example:

###################### Asigning A Function a Variable ########################

print(' Asigning A Function a Variable '.center(70, '='))
print("\n")


def multiply(a, b):
    return a * b


assign_mul = multiply

print(multiply)
print(assign_mul)

print(multiply(21, 3))
print(assign_mul(21, 3))

print("\n")
print(' returning A function by a function '.center(70, '='))
print("\n")


def outer_func():
    msg = 'Nilesh'

    def inner_func():
        print("Hello,{}".format(msg))
    return inner_func()  # Function being returned.


abc = outer_func  # returned Function being assigned.
abc()  # returned function by outer_func() being executed.


print("\n")
print(' Passing A function as an ARGUMENT to another function '.center(70, '='))
print("\n")

# Implementation of Mapper map() function.


def square(x):
    return x * x


def myMapper(func, arg_list):

    output_list = []
    for each in arg_list:
        output_list.append(func(each))

    return output_list


arguments = [12, 4, 6, 3, 76]

print(myMapper(square, arguments))
