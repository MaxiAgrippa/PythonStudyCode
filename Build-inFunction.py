# Numeric Functions
x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

y = float(x)
print(f'y is {type(y)}')
print(f'y is {y}')

x = -46
y = abs(x)
print(f'y is {type(y)}')
print(f'y is {y}')

x = 46
y = divmod(x, 3)
print(f'y is {type(y)}')
print(f'y is {y}')

y = complex(x, 3)
print(f'y is {type(y)}')
print(f'y is {y}')

# String Functions
s = 'Hello, World.'
print(repr(s))


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 🐎'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


s = Bunny(56)
print(repr(s))
print(str(s))
print(ascii(s))
print(chr(128406))
print(ord('🖖'))

# Container Function

x = (1, 2, 3, 4, 5)
y = len(x)
print(x)
print(y)
y = reversed(x)
print(y)
y = list(reversed(x))
print(y)
y = sum(x)
print(y)
y = sum(x, 10)
print(y)
y = max(x)
print(y)
x = (0, 0, 1, 0)
y = any(x)
print(y)
y = all(x)
print(y)
x = (1, 2, 3, 4, 5)
y = ('a', 'b', 'c', 'd', 'e')
z = zip(x, y)
print(list(z))
print(list(enumerate(y)))

# Object and Class Function
x = 42.0
y = isinstance(x, int)
print(y)
print(id(x))
