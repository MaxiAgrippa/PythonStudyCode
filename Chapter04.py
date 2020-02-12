
# Task 01
# Arithmetic
x = 5
y = 3
z = x + y
print(f'result is {z}')
z = x / y
print(f'result is {z}')
z = x // y
print(f'result is {z}')
z = x % y
print(f'result is {z}')
z = -z
print(f'result is {z}')
z = +z
print(f'result is {z}')
x = -y
z = +x
print(z)

# Task 02
# Bitwise
x = 0x0a
y = 0x02
z = x & y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
x = 0x0d
y = 0x0a
z = x | y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
z = x ^ y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
y = 0x01
z = x << y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
y = 0x01
z = x >> y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# Task 03
# Comparision Operator

x = 42
y = 73
a = x <= y
b = x >= y
c = x == y
d = x != y

if x < y:
    print('comparison is true')
else:
    print('comparison is false')
print(a, b, c, d)

# Task 04
# Boolean Operator

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')
if not b:
    print('not b is true')
if y in x:
    print('y in x')
if 'tree' in x:
    print('"tree" in x')
print(id(y))
print(id(x[0]))
if x is not y:
    print('x is not y')

# Task 05
# Operator

x = 2
y = 3 ** x
print(y)

