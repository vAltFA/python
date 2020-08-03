"""The program use one library is time.
Also using for looping"""
import time
digit = int(input('Enter your digit: '))
for i in range(digit, 0, -1):
    print(i, end= '')
    for j in range(0, i):
        print('*', end= '')
    print()
    time.sleep(1)
print('Blast off!')
