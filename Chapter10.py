# Exception

import sys


def main():
    # Task 01
    # Handling Exceptions

    try:
        a = {'v', 'a'}
        d = a + 1
        a = 3 + 3
        # b = 5 / 0
        # x = int('foo')
    except ValueError:
        print('I captured an Value Error')
    except ZeroDivisionError:
        print('I captured a Zero Division Error')
    except:
        print(f'Unknown Error {sys.exc_info()}')
    else:
        print('No Error')

    # Task 02
    # Reporting Errors
    try:
        for i in inclusive_range():
            print(i, end=' ', flush=True)
        print()
    except TypeError as e:
        print(f'Range Error: {e}')


# Task 02
# Reporting Errors

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


if __name__ == '__main__':
    main()
