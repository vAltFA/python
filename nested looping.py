digit = int(input('Enter your number: '))
for block in range(1, digit + 1):
    for line in range(1, block * 2):
        for stars in range(1, (block + line) * 2):
            print('*', end= '')
        print('*')
    print('\n')
