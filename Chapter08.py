# global
dlevel = 0  # manage nesting level


def main():
    # Task 01
    # Lists and Tuple
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1])
    print(game[1:3])
    print(game[1:5:2])  # work like range(start, end, step)
    i = game.index('Paper')
    print(i)
    print_list(game)
    game.append('Computer')
    print(game)
    game.insert(1, 'Keyboard')
    print(game)
    game.remove('Spock')
    print(game)
    x = game.pop()
    print('popped item: {}'.format(x))
    print(game)
    del game[1]
    print(game)
    print(', '.join(game))
    print('length of game: {}'.format(len(game)))
    # A tuple work exact like a list except it is immutable

    # Task 02
    # Dictionary
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    # key on the left, value on the right
    # key must be immutable
    print_dict(animals)
    animals02 = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr')
    print(id(animals))
    print(id(animals02))
    print_dict(animals02)
    print_dict2(animals02)
    print_dict_keys(animals02)
    print_dict_values(animals02)
    print(animals02['lion'])
    animals02['monkey'] = 'haha'
    print_dict2(animals02)
    print('lion' in animals02)
    print('human' in animals02)
    print('found!' if 'alien' in animals02 else 'Alien is not an animal!')
    print(animals02.get('alien'))

    # Task 03
    # Sets
    a = set("We're gonna need a bigger boat.")  # A set not allowed duplicate
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    print_set(sorted(a))
    print_set(sorted(b))
    print_set(a - b)
    print(a - b)
    print_set(a | b)
    print(a | b)
    print_set(a ^ b)
    print(a ^ b)
    print_set(a & b)
    print(a & b)

    # Task 04s
    # List Comprehension
    seq = range(11)
    print_list(seq)
    seq2 = [x ** 2 for x in seq]
    print_list(seq2)
    seq3 = [x for x in seq if x % 3 != 0]
    print_list(seq3)
    seq4 = [(x, x ** 2) for x in seq]
    print_list(seq4)
    seq5 = [(x, x ** 3) for x in seq if x % 3 != 1]
    print_list(seq5)
    from math import pi
    seq6 = [round(pi, i) for i in seq]
    print_list(seq6)
    seq7 = {x: x ** 3 for x in seq}
    print(seq7)
    seq8 = {x for x in 'qweasdzxc' if x not in 'plmqaz'}
    print(seq8)

    # Task 05
    # Mixed Structure
    r = range(11)
    l = [1, 'two', 3, {'4': 'four'}, 5]
    t = ('one', 'two', None, 'four', 'five')
    s = set("It's a bird! It's a plane! It's Superman!")
    d = dict(one=r, two=l, three=s)
    mixed = [l, r, s, d, t]
    disp(mixed)


# Task 01
# Lists and Tuple
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


# Task 02
# Dictionary
def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


def print_dict2(o):
    # more readable
    for k, v in o.items():
        print(f'{k}: {v}')


def print_dict_keys(o):
    for k in o.keys():
        print(k)


def print_dict_values(o):
    for v in o.values():
        print(v)


# Task 03
# Sets
def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')


# Task 04
# List Comprehension

# Task 05
# Mixed Structure
def disp(o):
    global dlevel

    dlevel += 1
    if isinstance(o, list):
        print_listm(o)
    elif isinstance(o, range):
        print_listm(o)
    elif isinstance(o, tuple):
        print_tuplem(o)
    elif isinstance(o, set):
        print_setm(o)
    elif isinstance(o, dict):
        print_dictm(o)
    elif o is None:
        print('Nada', end=' ', flush=True)
    else:
        print(repr(o), end=' ', flush=True)
    dlevel -= 1

    if dlevel <= 1: print()  # newline after outer


def print_listm(o):
    print('[', end=' ')
    for x in o: disp(x)
    print(']', end=' ', flush=True)


def print_tuplem(o):
    print('(', end=' ')
    for x in o: disp(x)
    print(')', end=' ', flush=True)


def print_setm(o):
    print('{', end=' ')
    for x in sorted(o): disp(x)
    print('}', end=' ', flush=True)


def print_dictm(o):
    print('{', end=' ')
    for k, v in o.items():
        print(k, end=': ')
        disp(v)
    print('}', end=' ', flush=True)


if __name__ == '__main__': main()
