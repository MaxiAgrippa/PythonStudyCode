def main():
    # Task 01
    # Creating a Class

    donald = Duck()
    donald.quack()
    print(donald.sound)
    donald.move()

    # Task 02
    # Constructing an Object

    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))
    print_animal(Animal02(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal02())

    # Task 03
    # Class Methods

    a0 = Animal03(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal03(type='duck', name='donald', sound='quack')
    a2 = Animal03(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)
    a2.sound('bark')
    print(a2)

    # Task 04
    # Object data

    a0 = Animal04(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal04(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)
    print('a0.x: {}'.format(a0.x))  # Python don't have private type
    a0.x[0] = 100
    print('a1.x: {}'.format(a1.x))  # Python don't have private type

    # Task 05
    # Inheritance

    a0 = Kitten05(name='fluffy', sound='rwar')
    a1 = Duck05(name='donald', sound='quack')
    print_animal05(a0)
    print_animal05(a1)
    a0.kill('humans')

    hello = RevStr('Hello, World.')
    print(hello)

    # Task 06
    # Iterator

    for n in inclusive_range(25):
        print(n, end=' ')
    print()
    for n in inclusive_range(2, 24, 3):
        print(n, end=' ')
    print()


# Task 01
# Creating a Class

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


# Task 02
# Constructing an Object

class Animal:
    def __init__(self, type, name, sound):  # Constructor of the class
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):  # getter
        return self._type

    def name(self):  # getter
        return self._name

    def sound(self):  # getter
        return self._sound


class Animal02:
    def __init__(self, **kwargs):  # Constructor of the class
        self._type = kwargs['type'] if 'type' in kwargs else 'type'
        self._name = kwargs['name'] if 'name' in kwargs else 'name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'sound'

    def type(self):  # getter
        return self._type

    def name(self):  # getter
        return self._name

    def sound(self):  # getter
        return self._sound


def print_animal(o):
    if isinstance(o, Animal):
        print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))
    elif isinstance(o, Animal02):
        print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))
    else:
        raise TypeError('print_animal(): requires an Animal or Animal02')


# Task 03
# Class Methods

class Animal03:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t=None):  # Setter & Getter
        if t: self._type = t
        return self._type

    def name(self, n=None):  # Setter & Getter
        if n: self._name = n
        return self._name

    def sound(self, s=None):  # Setter & Getter
        if s: self._sound = s
        return self._sound

    def __str__(self):  # works like override toString()
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


# Task 04
# Object data

class Animal04:
    x = [1, 2, 3]  # Python don't have private type

    # Notice: Distinct class variables and object variables

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


# Task 05
# Inheritance

class Animal05:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t=None):
        if t: self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n: self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s: self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None


class Duck05(Animal05):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


class Kitten05(Animal05):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will kill all {s}!')


def print_animal05(o):
    if not isinstance(o, Animal05):
        raise TypeError('print_animal05(): requires an Animal05')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')


class RevStr(str):
    def __str__(self):
        return self[::-1]


# Task 06
# Iterator

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


if __name__ == '__main__': main()
