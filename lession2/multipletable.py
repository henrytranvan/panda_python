number = input('Enter a number: ')

for index  in range(1, 11) :
    multy = int(number) * index
    print(number + ' x ' + str(index) + ' = ' + str(multy))