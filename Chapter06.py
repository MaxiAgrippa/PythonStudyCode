# Task 01
# While Loop

secret = 'swordfish'
pw = ''

# while pw != secret:
#    pw = input("What's the secret word? ")
secretIndex = 10
i = 0
while i != secretIndex:
    i += 1
    print('i = {}'.format(i))

# Task 02
# For Loop

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    print(pet)

for i in range(5):
    print(i)

# Task 03
# Additional Loop Controls

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    if count == 3:
        continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print('Authorized' if auth else 'Calling the FBI ...')


animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog':
        continue
    if pet == 'velociraptor':
        break
    print(pet)
else:
    print('That is all of the animals')
