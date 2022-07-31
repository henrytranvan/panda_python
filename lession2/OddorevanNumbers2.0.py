number = input('Enter a number: ')
max = int(number)

sumevent = 0
sumodd = 0

for index  in range(1, max +1) :
    if (index % 2) == 0:
        sumevent = sumevent + index
        
    else:
        sumodd = sumodd + index

print('Even number is ' + str(sumevent))
print('Odd number is ' + str(sumodd))