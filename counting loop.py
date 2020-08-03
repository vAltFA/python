digit = int(input('Enter your digit: '))
digit_2 = int(input('Enter your second 2: '))
digit_3 = digit_2 + 1
for i in range(1, digit_3):
    print(digit, ' x ', i, ' = ', i * digit)
