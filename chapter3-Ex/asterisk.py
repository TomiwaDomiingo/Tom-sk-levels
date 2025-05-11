row = 0
for i in range(1, 11):
   
    print('*' * row, end='   ')

    print('*' * (11 - row), end='   ')

    print(' ' * (row - 1) + '*' * (11 - row), end='   ')

    print(' ' * (10 - row) + '*' * row)