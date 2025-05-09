for i in range(1, 11):
   
print('*' * row, end='   ')

   # Pattern (b)
print('*' * (11 - row), end='   ')

    # Pattern (c)
print(' ' * (row - 1) + '*' * (11 - row), end='   ')

    # Pattern (d)
print(' ' * (10 - row) + '*' * row)