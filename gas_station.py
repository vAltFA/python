import random
buffer = int(random.randint(-5, 5))
next_station = 200
size_of_tank = int(input('How big is your tank, in litres?: '))
actually_tank = int(input('How full is your tank, in litres?: '))
km_per = int(input('How many km per liter does your car get?: '))
actually_tank_with_buffer = actually_tank + buffer
if actually_tank == actually_tank_with_buffer:
    percent_tank = actually_tank / size_of_tank * 100
    next_station_arrive = actually_tank * km_per
    if next_station_arrive > next_station:
        print('Size of tank: ' + str(size_of_tank) + '\n'
        + 'percent full: ' + str(percent_tank) + '\n'
        + 'km per liter: ' + str(km_per) + '\n'
        + 'You can go another ' + str(next_station_arrive) + ' km'
        + '\n' + 'The next gas station is 200 km away' + '\n'
        + 'You can wait for the next station')
    else:
        print('Size of tank: ' + str(size_of_tank) + '\n'
        + 'percent full: ' + str(percent_tank) + '\n'
        + 'km per liter: ' + str(km_per) + '\n'
        + 'You can go another ' + str(next_station_arrive) + ' km'
        + '\n' + 'The next gas station is 200 km away' + '\n'
        + 'You can gas now!')
else:
    percent_tank = actually_tank_with_buffer / size_of_tank * 100
    next_station_arrive = actually_tank_with_buffer * km_per
    if next_station_arrive > next_station:
        print('Buffer size: ' + str(buffer) +'\n'
        + 'Size of tank: ' + str(size_of_tank) + '\n'
        + 'percent full: ' + str(percent_tank) + '\n'
        + 'km per liter: ' + str(km_per) + '\n'
        + 'You can go another ' + str(next_station_arrive) + ' km'
        + '\n' + 'The next gas station is 200 km away' + '\n'
        + 'You can wait for the next station')
    else:
        print('Buffer size: ' + str(buffer) +'\n'
        + 'Size of tank: ' + str(size_of_tank) + '\n'
        + 'percent full: ' + str(percent_tank) + '\n'
        + 'km per liter: ' + str(km_per) + '\n'
        + 'You can go another ' + str(next_station_arrive) + ' km'
        + '\n' + 'The next gas station is 200 km away' + '\n'
        + 'You can gas now!')
