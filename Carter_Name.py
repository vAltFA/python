for i in range(5):
    for j in range(6):
        if i == 0 or i == 4 and j != 3:
            print(j, end= ' ')
        else:
            print('*')
