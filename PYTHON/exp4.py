try:
    print(1/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")

# index error
try:
    print([1,2,3][3])
except IndexError:
    print("IndexError")

# key error
try:
    print({'a':1,'b':2}['c'])
except KeyError:
    print("KeyError")

# overflow error
try:
    print(1e1000)
except OverflowError:
    print("OverflowError")

# type error
try:
    print(1 + 'a')
except TypeError:
    print("TypeError")

# floating point error
try:
    print(1.0/0.0)
except FloatingPointError:
    print("FloatingPointError")

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
 
try:
    raise Networkerror("Error")
 
except Networkerror as e:
    print(e.args)
