#!usr/bin/env python3
import platform

# test 01

# print test
print('Hello Wrold !')
print('This is running on python version: {}'.format(platform.python_version()))

# test 02

# main and comment

def main():
    message()

# comment01
##comment02
#comment03
#123
# 123



def message():
    print('the version of currently using python is {}'.format(platform.python_version()))

# test 03

# this line execute the main func.
# python need to define function first, and then run it
# putting this line in the end of the file is to let the interpreter read all the lines in the file before run it.
# you will get alert in Pycharm due to loss typing style
if __name__=='__main__':
    main()

printValueTest=print('abcd')

print(printValueTest)

# test 04

# Test format in string
# There is no different when an announcement is in a block of code or not.

print('there is a format: {}'.format('format'))

x = 42
y = 73

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
    z=999
    print('three values {}, {}, {}'.format(x,y,z))

print(z)

# test 05

# there is no switch case in python
# use If Else to place switch case
isTrue = True

if isTrue:
    print('False')
elif isTrue:
    print('True')
else:
    print('final else')

# test 06

# loops

words = ['one', 'two', 'three', 'four', 'five']
i = 0
while i < 5:
    print(words[i])
    i += 1

a = 0
b = 1
while b < 1000:
    print(b, end = ' ', flush = True)
    c = a + b
    a = b
    b = c

print()

for j in words:
    print(j)

# test 07
print()
print('Test 07')
print()
# function


def function(x = 1):
    print(x)


function()
function('func')


def function2(x = 2):
    print(x)
    return x*2


function2()
fc=function2('func2')
print(fc)

# test 08

# class


class Duck:
    sounds = 'Quaaack!'
    walking = 'Walks like a duck.'
    swim = 'swim'

    def quack(self):
        print('Quaaack!')
        print(self.sounds)

    def walk(self):
        print('Walks like a duck.')
        print(self.walking)

    def swim(x):
        print('swim')
        #print(self.swim)


donald = Duck()
donald.quack()
donald.walk()
donald.swim()

"""
-----------------------------------------------------------
Chapter 02
-----------------------------------------------------------
"""

# Task 01
# String

x = 7
print('x is {}'.format(x))
print(type(x))
x = 7.0
print('x is {}'.format(x))
print(type(x))
x = 'abc'
print('x is {}'.format(x))
print(type(x))
x = "def"
print('x is {}'.format(x))
print(type(x))
x = '''

multi-line-string
'''
print('x is {}'.format(x))
print(type(x))
x = """

another style of multi-line-string
"""
print('x is {}'.format(x))
print(type(x))
x = True
print('x is {}'.format(x))
print(type(x))
x = None
print('x is {}'.format(x))
print(type(x))

# you can directly use double quotes in single quote string or single quotes in double quote string
x = "test String 001 '{1:<09}', {0:>9}"
print(x)
x2 = x.capitalize()
print(x2)
x2 = x.upper()
print(x2)
x2 = x.format('a', 2)
print(x2)

# Test 02
# Numeric
x = 7
print('x is {}'.format(x))
print(type(x))
x = 7.0
print('x is {}'.format(x))
print(type(x))
x = 7 * 3.0
print('x is {}'.format(x))
print(type(x))
# Notice
x = 7 * 2.99999999999999999999999999999999999999999999999999999
print('x is {}'.format(x))
print(type(x))
x = 7 / 3
print('x is {}'.format(x))
print(type(x))
x = 7 // 3
print('x is {}'.format(x))
print(type(x))
x = .1 + .1 - .2
print('x is {}'.format(x))
print(type(x))
# The result of this won't be 0
x = .1 + .1 + .1 - .3
print('x is {}'.format(x))
print(type(x))

# use decimal to avoid it
from decimal import *

x1 = Decimal('.1')  # ATTENTION potential ERROR
x2 = Decimal('.3')  # ATTENTION potential ERROR
x = x1 + x1 + x1 - x2
print('x is {}'.format(x))
print(type(x))

x1 = Decimal('.10')  # ATTENTION potential ERROR
x2 = Decimal('.30')  # ATTENTION potential ERROR
x = x1 + x1 + x1 - x2
print('x is {}'.format(x))
print(type(x))

# Task 03
# bool

t = True
print('t is {}'.format(t))
print(type(t))
t = 7 < 3
print('t is {}'.format(t))
print(type(t))
t = None  # Notice
if t:
    print("None is True")
else:
    print("None is False")
t = 0  # Notice
if t:
    print("0 is True")
else:
    print("0 is False")
t = ''  # Notice
if t:
    print("'' is True")
else:
    print("'' is False")

# Task 04
# Sequence

x = [1, 2, 3, 4, 5]
for i in x:
    print('i is {}'.format(i))

aTuple = (1, 2, 3, 4, 5)  # Notice tuple can not be changed after it's initialized
# aTuple[2] = 0 # ERROR
for i in x:
    print('i is {}'.format(i))

y = []
for i1 in range(10):
    y.append(i1)
print(y)

y = range(2, 7)
print(y)
for i in y:
    print('i is {}'.format(i))

y = range(5, 50, 5)  # Parameters: Start, End, Step by
# y[2] = 0 # ERROR
for i in y:
    print('i is {}'.format(i))

y = list(range(2, 7))
print(y)
y[2] = 0
for i in y:
    print('i is {}'.format(i))

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
d['three'] = 555
for i in d:
    print('i is {}'.format(i))
for i, j in d.items():
    print('i: {}, j: {}'.format(i, j))

# Task 05
# type() & id()

x = [1, 2, 3, 4, 5]
print('x is {}'.format(x))
print(type(x))
x = (1, 2, 3, 4, 5)
print('x is {}'.format(x))
print(type(x))
x = (1, 2.0, 'three', [0, 'one'], 5)
y = (1, 2.0, 'three', [0, 'one'], 5)
print('x is {}'.format(x))
print(type(x[1]))
print(id(x))
print(id(x[2]))
print(id(y[2]))
if x[0] is y[0]:
    print('They are Same Object')
else:
    print('They are Different Object')

if x is y:
    print('They are Same Object')
else:
    print('They are Different Object')

if isinstance(x, tuple):
    print("x is tuple")
elif isinstance(x, list):
    print("x is list")
else:
    print('x is not tuple')





# test final


print()


print('Alert, no new line in the end of code.')