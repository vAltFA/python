print('Enter your digit: ')
x = int(input())
print('Enter second digit: ')
y = int(input())
if x != y:
    print('Your digit is not equel')
elif x < y:
    print('Your first digit is lower')
elif x > y:
    print('Your first digit is higher')
else:
    print('Your first digit is equel')
