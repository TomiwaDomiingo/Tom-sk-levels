for stars in range(10):
    for space in range(stars + 1):
        print('*', end='')
    print()  
print()
for stars in range(10):
    for space in range(10 - stars):
        print('*', end='')
    print()
print()
for stars in range(10):
    for space in range(10 - stars):
        print(' ', end='') 
    for space in range(stars + 1):
        print('*', end='')
    print()
print()

for stars in range(10):
    for space in range(stars):
        print(' ', end='') 
    for space in range(10 - stars):
        print('*', end='')
    print()
