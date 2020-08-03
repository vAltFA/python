names = ['Tony' ,'Paul','Nick' ,'Michael' ,'Kevin']
print('Enter 5 names ')
for i in names:
    print(i)
print('The names are', names[0], names[1], names[2], names[3], names[4])
n_names = names[:]
while True:
    replace = int(input('Replace one name. Which one? (1-5): '))
    if replace != 0 and replace <= 5:
        new_name = str(input('Enter new name: '))
        if new_name != n_names[replace - 1]:
            del n_names[replace - 1]
            n_names.insert(replace - 1, new_name)
            print('New name: ', new_name)
            print('The names are', n_names[0], n_names[1], n_names[2], n_names[3], n_names[4])
        else:
            print('Error: This name is the same like it was')
    else:
        print('Error: Choose correct number')
    
