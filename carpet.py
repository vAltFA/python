print('Enter the 1st side: ')
a = input()
a_int = int(a)
print('Enter the 2nd side: ')
b = input()
b_int = int(b)
rectangular_room_feet = (a_int + b_int) * 2
rectangular_room_yards = (a_int + b_int) * 2 * 9
total_carpet = rectangular_room_feet * rectangular_room_yards
print(rectangular_room_feet)
print(rectangular_room_yards)
print(total_carpet)
