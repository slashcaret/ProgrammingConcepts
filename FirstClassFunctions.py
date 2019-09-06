'''First Class Functions:
   First class Function is an entity in or a Function() that is treated
   as First Class CItizen in Python or any other Programming Language.'''
#############################################################################
'''First class citizen means The entity that supports all the operations supported
    by any other Entities. These Opearations typically include being passed as an
    argument , being returned by a function or being assigned to variable.'''
##############################################################################

'''In Short A First Class Function is availability provided by some
programming languages, by which a Function can be assigned to a variable or
it can be passed as an argument to any other Function (Ex. Python map() Function)
or it can be returned by another Function.'''


'''Properties of first class functions:

A first class function can be treated as an object.
It posseses following properties.
1) We can create instance of FCF.
2) We can pass it as a Parameter to another function.
3) It can be returned by a function.
4) they can be stored in data structures such as lists, dictionaries and what not'''
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
print(' Example 1 '.center(70, '='))


def square(x):
    return x * x


def myMapper(func, arg_list):

    output_list = []
    for each in arg_list:
        output_list.append(func(each))

    return output_list


arguments = [12, 4, 6, 3, 76]

print(myMapper(square, arguments))


''' All Python Functions are FCFs. It can be said-Python Functions are Objects '''


############################# Another Example #########################
print(' Example 2 '.center(70, '='))


def take_msg(message):

    edited_msg = message + ' edited by '

    def give_msg(name):
        print(edited_msg + name)  # accessing Varaible outside scope

    return give_msg  # Function being returned


print(take_msg.__name__)
assignment = take_msg  # Instance of a function is created
print(assignment.__name__)

result = take_msg('Python is Awesome')  # assigning returned function
print(result.__name__)
result('Nilesh Unde')
