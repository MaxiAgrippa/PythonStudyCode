import time


# Task 01
# Function Basic


def main():
    # Task 01
    x = kitten(5, 6, 7)
    kitten(5, 6, 7, 8)
    print(x)

    # Notice Python is tricky in call-by-value function
    # when it's about immutable, the function is call by value
    print('Notice Python is tricky in call-by-value function')
    y = 5
    callbyvalue(5)
    z = y
    callbyvalue(z)
    print('id of y is {}'.format(id(y)))
    print('id of z is {}'.format(id(z)))
    z = 4
    print('change z')
    print('id of y is {}'.format(id(y)))
    print('id of z is {}'.format(id(z)))

    # when it's about mutable, the function is call by reference
    y = [5]
    z = y
    z[0] = 3
    print('id of y is {}'.format(id(y)))
    print('id of z is {}'.format(id(z)))
    print('value of y {}'.format(y))
    print('value of z {}'.format(z))
    callbyvalue2(z)
    print('value of y {}'.format(y))
    print('value of z {}'.format(z))

    # Task 02
    # Arguments List
    t = ('meow', 'grrr', 'purr', 'world')
    argumentslist('meow', 'grrr', 'purr', 'world')
    print('t is a tuple')
    argumentslist(*t)

    # Task 03
    # Keyword Arguments
    d = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    keywordargements(Buffy='meow', Zilla='grr', Angel='rawr')
    print('d is a dictionary')
    keywordargements(**d)

    # Task 04
    # Return Value
    v = returnvalue()
    print(type(v), v)

    # Task 05
    # Generators
    for i in inclusive_range(25):
        print(i, end=' ')
    print()

    # Task 06
    # Decorators
    f4(f3)
    big_sum()


def kitten(n, a, b, c=0):  # Notice Any argument with default mush after any argument without default.
    print(f'{n} Meow.')
    print(a, b, c)
    return 'Meow.'


# when it's about immutable, the function is call by value
def callbyvalue(n):  # Notice Python is tricky in call-by-value function
    print('id of n before change it: {}'.format(id(n)))
    n = 0
    print('id of n before change it: {}'.format(id(n)))


# when it's about mutable, the function is call by reference
def callbyvalue2(n):  # Notice Python is tricky in call-by-value function
    n[0] = 0


# Task 02
# Arguments List

def argumentslist(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


# Task 03
# Keyword Arguments

def keywordargements(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')


# Task 04
# Return Value

def returnvalue():
    print('Meow.')
    return dict(x=1, y=3, z=7)


# Task 05
# Generators

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


# Task 06
# Decorators

def f1(f):
    def f2():
        print('this is f2')
        print('this is before the function call')
        f()
        print('this is after the function call')

    return f2


def f3():
    print('this is f3')


def f4(f3):
    f3 = f1(f3)
    f3()


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')

    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')


if __name__ == '__main__':
    main()
