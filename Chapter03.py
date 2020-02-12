
'''
-----------------------------------------------------------
Chapter 03
-----------------------------------------------------------
'''

# Task 01
# Conditional

if True:
    print('if true')
elif False:
    print('elif true')
else:
    print('neither true')

hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'  # Notice: else clause is mandatory in this case
print(x)

